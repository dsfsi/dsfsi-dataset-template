import config, file_handler, sentence_tokenisation, sentence_embedding, os, re

languages = ['afr', 'eng', 'nbl', 'nso', 'sep', 'ssw', 'tsn', 'tso', 'ven', 'xho', 'zul']

lang_mappings = {
                    # 'afr' : 'afr_Latn',
                    # 'eng' : 'eng_Latn',
                    # 'nbl' : 'nbl_Latn',
                    'nso' : 'sot_Latn',
                    # 'sep' : 'sep_Latn',
                    'ssw' : 'ssw_Latn',
                    'tsn' : 'tsn_Latn',
                    'tso' : 'tso_Latn',
                    # 'ven' : 'ven_Latn',
                    'xho' : 'xho_Latn',
                    'zul' : 'zul_Latn',
                } 


if __name__ == "__main__":
    # setup
    config.setup_laser()
    config.download_laser_models(lang_mappings)
    config.download_tokeniser()

    # create directories dictionary
    root_dirs = file_handler.fetch_data_root_filepaths()
    full_dict = file_handler.compile_full_lang_dict()

    # perform tokenisation
    for lang in languages:
        for directory in root_dirs:
            if directory not in full_dict[lang].keys():
                continue
            for edition in full_dict[lang][directory]:
                text = file_handler.read_file(directory, edition)
                tokens = sentence_tokenisation.tokenise(text)
                path = edition
                file_handler.write_tokens_to_txt(directory, path, tokens)

    for directory in root_dirs:
        listdir = os.listdir("../../data/tokenised/{}".format(directory))
        for text_txt in listdir:
            match = re.search('nso|ssw|tsn|tso|xho|zul', text_txt)
            output = text_txt
            re.sub("\.txt","\.raw", output)
            if match:
                matched = match.group()
                sentence_embedding.embed_sentences(text_txt, "../../data/embed/{}/{}".format(directory,output),lang_mappings[matched])
