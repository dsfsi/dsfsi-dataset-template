import subprocess

def embed_sentences(txt_path, output_path, lang_model):
    command = f'bash ./LASER/tasks/embed/embed.sh '
    command += "{} {} {}".format(txt_path, output_path, lang_model)
    subprocess.run(command, shell=True)
    
    