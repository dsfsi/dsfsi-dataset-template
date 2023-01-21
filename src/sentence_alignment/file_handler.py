import os,re

data_path = '{}/data/processed/'.format(os.getcwd())
languages = ['afr', 'eng', 'nbl', 'nso', 'sep', 'ssw', 'tsn', 'tso', 'ven', 'xho', 'zul']

def fetch_data_root_filepaths(): # -> list[str]
    """
    ### Compiles a list of file directories present in the /data/processed folder
    """
    root_paths = os.listdir(data_path) #list the directories in /data/processed
    root_paths.remove('.gitkeep') 
    return root_paths

def fetch_lang_filepaths(lang): # -> dict[str, dict[str,list[str]]]
    """
    ### Creates a dict for each lang. 
    #### Example (eng)
    ```
    {
        'eng' : {
            '2020-09-ed1' : [
                '2020-09-ed1-vukuzenzele-eng-001.txt',  
                '2020-09-ed1-vukuzenzele-eng-002.txt',  
                '2020-09-ed1-vukuzenzele-eng-003.txt'  
            ]
        }
    }
    ```
    """
    lang_paths = {}
    root_paths = fetch_data_root_filepaths()
    for main_path in root_paths: # for each directory in data/processed
        edition_paths = os.listdir('{}/{}'.format(data_path, main_path)) # list the files in data/processed/edition
        for path in edition_paths:
            match = re.search(lang, path) # look for files with lang tag
            if match: # if lang found
                if main_path in lang_paths.keys(): # if edition path already exists
                    lang_paths[main_path].append(path) # append to existing list
                else: lang_paths[main_path] = [path] # else create new list for edition path

    return {lang : lang_paths} # return new dict with lang tag key

def compile_full_lang_dict(): # -> dict[str,dict[str,list[str]]]
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
    output_dict = {}
    for lang in languages:
        output_dict.update(fetch_lang_filepaths(lang))
    return output_dict

def read_file(edition_path, txt_path): # -> str
    """
    ### Reads file as a single string.
    """
    return open(data_path + edition_path + '/' + txt_path, 'r').read() 


def write_tokens_to_txt(edition_path, txt_path, tokens): # -> None
    if not os.path.isdir('./data/tokenised/{}'.format(edition_path)):
        os.mkdir('./data/tokenised/{}'.format(edition_path))
    new = open('./data/tokenised/{}/{}'.format(edition_path, txt_path),'w')
    for token in tokens:
        new.write(token)
        if not tokens[len(tokens)-1]==token:
            new.write('\n')

