import os, re, pandas
from pathlib import Path
from datetime import date

root_path = Path(os.path.abspath(__file__)).parent.parent.parent # vukuzenzele/

raw_data_path = Path(root_path / 'data' / 'processed') #data/processed - raw in terms of sentence alignment
token_data_path = Path(root_path  / 'data' / 'tokenised') #data/tokenised - the tokenised form
output_data_path = Path(root_path / 'data' / 'sentence_align_output') #data/sentence_align_output - SA using encoders
simp_out_data_path = Path(root_path / 'data' / 'simple_align_output')  #data/simple_align_output - plain SA, eg `hello` -> `hallo`

languages = ['afr', 'eng', 'nbl', 'nso', 'sep', 'ssw', 'tsn', 'tso', 'ven', 'xho', 'zul'] # List of SA languages


def extract_latest_edition():
    return open(
        Path(
            Path(os.path.abspath(__file__)).parent #src/sentence_alignment
            / 'last_edition_read.txt'
        ),'r').read()

def write_latest_edition(edition):
    open(
        Path(
            Path(os.path.abspath(__file__)).parent #src/sentence_alignment
            / 'last_edition_read.txt'
        ),'w').write(edition)

def build_date(edition):
    edition_date = re.search('^\d{4}-\d{2}', edition).group()
    edition_no = re.search('\d$',edition).group()

    year = re.search('^\d{4}', edition_date).group()
    month = re.search('\d{2}$', edition_date).group()
    day = edition_no

    return date(int(year), int(month), int(day))

def fetch_data_edition_filepaths(): # -> list[str]
    """
    ### Compiles a list of file directories present in the /data/processed folder after the date present in /last_edition_read.txt
    #### Example filepath: `2020-01-ed1`
    """
    last_date = extract_latest_edition()
    all_paths = os.listdir(raw_data_path) #list the directories in /data/processed
    all_paths.remove('.gitkeep') 

    edition_paths = []
    for path in all_paths:
        if build_date(path) > build_date(last_date):
            edition_paths.append(path)
    return edition_paths

def fetch_data_txt_filepaths(edition): # -> list[str]
    """
    ### Compiles a list of files present in the /data/processed/edition folder
    #### Example filepath: `2020-02-ed1-vukuzenzele-afr-01.txt`
    #### Params 
        -   `edition` is the different editions of the magazine stored in data/processed
    """
    txt_paths = os.listdir('{}/{}'.format(raw_data_path, edition)) #list the directories in /data/processed
    return txt_paths

def build_filepaths_dictonary():
    """
    ### Creates a dict for every lang. 
    #### Example
    ```
    {
        'eng' : {
            '2020-09-ed1' : [
                '2020-09-ed1-vukuzenzele-eng-001.txt',  
                '2020-09-ed1-vukuzenzele-eng-002.txt',  
                '2020-09-ed1-vukuzenzele-eng-003.txt'  
            ]
        }
        'afr' : {
            '2020-09-ed1' : [
                '2020-09-ed1-vukuzenzele-afr-001.txt',  
                '2020-09-ed1-vukuzenzele-afr-002.txt',  
                '2020-09-ed1-vukuzenzele-afr-003.txt'  
            ]
        }
    }
    ```
    """
    filepaths_dictionary = {}
    edition_paths = fetch_data_edition_filepaths()
    for edition in edition_paths:
        txt_paths = fetch_data_txt_filepaths(edition)
        for txt in txt_paths:
            lang = re.search('afr|eng|nso|nbl|sep|ssw|tsn|tso|ven|xho|zul', txt).group()
            if lang not in filepaths_dictionary.keys():
                filepaths_dictionary[lang] = {edition : [txt]}
            elif edition not in filepaths_dictionary[lang].keys():
                filepaths_dictionary[lang][edition] = [txt]
            else: 
                filepaths_dictionary[lang][edition].append(txt)

    return filepaths_dictionary

def read_file_as_string(edition_path, txt_path): # -> str
    """
    ### Reads file as a single string. 

    Generally used to feed a single line text to the tokeniser
    """
    file_path = Path(raw_data_path / edition_path / txt_path)
    return open(file_path, 'r').read() 

def read_file_as_array(edition_path, txt_path): # -> str
    """
    ### Reads file as an array.

    Generally used to read tokenised data for further processing
    """
    file_path = Path(token_data_path / edition_path / txt_path)
    return open(file_path, 'r').readlines() 


def write_tokens_to_txt(edition_path, txt_path, tokens): # -> None
    """
    ### Writes a token array to a .txt in the data/tokenised folder
    #### Params:
        -   edition_path: path_name representing the edition to create a new dir for the tokens
        -   txt_path: path_name to the sentence tokens to create a new txt file
        -   tokens: list of sentence tokens to be written to file
    """
    if not os.path.exists(Path(token_data_path / edition_path)): #if data/tokenised/edition does not exist
        os.makedirs((Path(token_data_path / edition_path))) # create it

    new = open((Path(token_data_path / edition_path / txt_path)),'w') # open a txt file in write mode
    for token in tokens: #for each tokem
        new.write(token) # write to new file
        if not tokens[len(tokens)-1]==token: # the tokens seem to be missing newlines so if token is not the last token,
            new.write('\n')  # write a newline

def append_to_final_csv(src_lang, src_sentences, src_vector, tgt_lang, tgt_sentences ,tgt_vector, sim_scores):
    """
    ### Appends to the ML aligned lang pairs .csv - creates it if it doesn't exist
    #### Params
        -   src_lang: source lang (str)
        -   src_sentences: source sentence tokens (list)
        -   src_vector: source sentence vectors (list)
        -   tgt_lang: target lang (str)
        -   tgt_sentences: target sentence tokens (list)
        -   tgt_vector: target sentence vectors (list)
        -   sim_scores: confidence scores between the pairing (list)
    """
    data = {
        src_lang : src_sentences,
        tgt_lang : tgt_sentences,
        '{}_vector'.format(src_lang) : src_vector,
        '{}_vector'.format(tgt_lang) : tgt_vector,
        'cosine_score' : sim_scores
    } # build a dictonary of the info

    df = pandas.DataFrame(data) #turn into a pandas DF

    csv_path = Path('aligned_{}_{}.csv'.format(src_lang, tgt_lang)) # Path of lang aligned csv
    if not os.path.exists(output_data_path): # if data/sentence_alignment doesnt exist
        os.makedirs(output_data_path) # create it 

    if os.path.exists(Path(output_data_path / csv_path)): # if .csv does exist
        df.to_csv(Path(output_data_path / csv_path), mode='a',header=False, index=False) # append with no headers
    else: 
        df.to_csv(Path(output_data_path / csv_path), mode='w',header=True, index=False) # create with headers


def append_to_simple_csv(src_lang, src_sentences, tgt_lang, tgt_sentences):

    data = {
        src_lang : src_sentences,
        tgt_lang : tgt_sentences,
    }
    df = pandas.DataFrame(data)

    csv_path = Path('aligned_{}_{}.csv'.format(src_lang, tgt_lang))
    if not os.path.exists(simp_out_data_path):
        os.makedirs(simp_out_data_path)

    if os.path.exists(Path(output_data_path / csv_path)):
        df.to_csv(Path(simp_out_data_path / csv_path), mode='a',header=False, index=False)
    else: 
        df.to_csv(Path(simp_out_data_path / csv_path), mode='w',header=True, index=False)