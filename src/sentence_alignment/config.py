import os, subprocess, nltk

def setup_laser():
    """
    ### Downloads configs for LASER repo
    """
    print('------------------------------------LASER setup------------------------------------')
    os.environ['LASER'] = '{}/LASER'.format(os.getcwd())
    command = f'bash ./LASER/install_models.sh; bash ./LASER/remove_external_tools.sh; bash ./LASER/install_external_tools.sh'
    subprocess.run(command, shell=True)


def download_laser_models(lang_mappings):
    print('-------------------------------LASER model download--------------------------------')
    command = f'bash ./LASER/nllb/download_models.sh'
    for _,val in lang_mappings.items():
        command = "{} {}".format(command, val)
    subprocess.run(command, shell=True)


def download_tokeniser() -> None:
    print('---------------------------Download NLTK Tokeniser---------------------------------')
    nltk.download('punkt')