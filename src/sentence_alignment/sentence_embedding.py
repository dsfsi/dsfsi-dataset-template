import subprocess


DATA_PATH = "../../data/tokenised/"


def embed_sentences(txt_path, output_path, lang_model):
    command = f'bash ./LASER/tasks/embed/embed.sh '
    command += "{} {} {}".format(f'{DATA_PATH}{txt_path}', output_path, lang_model)
    subprocess.run(command, shell=True)
    
    