import os, subprocess, nltk
from pathlib import Path


laser_path = Path(Path(os.path.abspath(__file__)).parent / 'LASER') # path to LASER module

def set_environ_var():
    """
    ### Sets enviroment variable for use within the LASER module
    """
    os.environ['LASER'] = str(laser_path)

def setup_laser():
    """
    ### Downloads configs for LASER repo
    """
    print('------------------------------------LASER setup------------------------------------')
    if (os.path.exists(f'{laser_path}/models')):
        print('LASER/models dir found, skipping installation')
    else: 
        command = f'bash {laser_path}/install_models.sh'
        subprocess.run(command, shell=True)
    if (os.path.exists(f'{laser_path}/tools-external')):
        print('LASER/tools-external dir found, skipping installation')
    else: 
        command = f'bash {laser_path}/install_external_tools.sh'
        subprocess.run(command, shell=True)


def download_laser_models(lang_mappings):
    """
    ### Downloads language models to perform sentence encoding
    #### Params:
        -   lang_mappings: a dictionary mapping langs to LASER models, eg. 'xho -> xho_Latn`. (dict)
    """
    print('-------------------------------LASER model download--------------------------------')
    command = f'bash {laser_path}/nllb/download_models.sh'
    for _,val in lang_mappings.items():
        command = "{} {}".format(command, val)
    subprocess.run(command, shell=True)


def download_tokeniser() -> None:
    print('---------------------------Download NLTK Tokeniser---------------------------------')
    nltk.download('punkt')