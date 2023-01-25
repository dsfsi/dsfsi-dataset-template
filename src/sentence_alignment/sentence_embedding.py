import subprocess, os, numpy
from pathlib import Path

from laser_config import laser_path
from file_handler import root_path

embed_data_path = Path('data/embed')

def encode_sentences(edition_path, txt_path, lang_model):
    """
    ### Calls LASER task to encode a txt_file and outputs a raw_file that can be decoded into a sentece vector
    #### Example
    `hello` -> raw format
    #### Params:
        -   edition_path: the path_name to the dir for this edition to be created in data/embed (str)
        -   txt_path: the path_name for the raw output to be written to (str)
        -   lang_model: the lang model to be used in the encoding (str)
    """

    if not os.path.exists(Path(embed_data_path / edition_path)): # if data/embed/edition doesn't exist
        os.makedirs(Path(embed_data_path / edition_path)) # make it 
    output_path = Path(embed_data_path / edition_path / txt_path) # the path to output

    command = f'bash {laser_path}/tasks/embed/embed.sh ' # the command without params
    command += "{} {} {}".format(Path(embed_data_path / edition_path / txt_path), output_path, lang_model) # add params which are source text, output path & lang model
    subprocess.run(command, shell=True) # run the bash command using the shell
    
def decode_sentences(edition_path, txt_path):
    """
    ### Decodes the raw output into a sentence vector - the vector stores in the sentence meaning in computer terms
    #### Example
    raw format -> `[3, 4, ... ,5, 6]`
     #### Params:
        -   edition_path: the path_name to the dir for this edition (str)
        -   txt_path: the path_name for the raw output to be decoded (str)
    """
    dim = 1024 # dimensions
    path = Path(embed_data_path / edition_path / txt_path) # path to file
    vector_list = numpy.fromfile(path, dtype=numpy.float32, count=-1) # fancy numpy coding idk                                                               
    vector_list.resize(vector_list.shape[0] // dim, dim)  # more fancy
    return vector_list # return list of vectors
