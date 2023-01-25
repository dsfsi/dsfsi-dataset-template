import laser_config, file_handler, sentence_tokenisation, sentence_embedding, sentence_alignment, os, re, pathlib

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

    # setup laser
    laser_config.set_environ_var()
    laser_config.setup_laser()
    laser_config.download_laser_models(lang_mappings)
    laser_config.download_tokeniser()
    
    
    # create directories dictionary
    filepaths_dictionary = file_handler.build_filepaths_dictonary()
    last_date = file_handler.extract_latest_edition()
    edition_keys = file_handler.fetch_data_edition_filepaths(last_date);

    # perform tokenisation
    for edition in edition_keys:
        for lang in languages:
            if edition not in filepaths_dictionary[lang]:
                continue
            for txt in filepaths_dictionary[lang][edition]:
                text = file_handler.read_file_as_string(edition, txt)
                tokens = sentence_tokenisation.tokenise(text)
                file_handler.write_tokens_to_txt(edition, txt, tokens)

    # perform LASER encoding
    for edition in edition_keys:
        for lang in lang_mappings.keys():
            if edition not in filepaths_dictionary[lang]:
                continue
            for txt in filepaths_dictionary[lang][edition]:
                sentence_embedding.encode_sentences(edition, txt, lang_mappings[lang])

    # perform SA on LASER encoded sentences
    for first_lang in lang_mappings.keys():
        for sec_lang in lang_mappings.keys():
            if first_lang != sec_lang:
                for edition in edition_keys:
                    sentence_alignment.two_lang_alignment(first_lang, sec_lang, edition)


    # # perform basic sentece alignment on tokenised sentences
    for first_lang in languages:
        for sec_lang in languages:
            if first_lang != sec_lang:
                for edition in edition_keys:
                    sentence_alignment.simple_langs_alignment(first_lang, sec_lang, edition)

    # write last edition reviewed to file so as not to review in future
    file_handler.write_latest_edition(edition_keys[len(edition_keys)-1])
    


    # for directory in root_dirs:
    #     listdir = os.listdir("../../data/tokenised/{}".format(directory))
    #     for text_txt in listdir:
    #         match = re.search('nso|ssw|tsn|tso|xho|zul', text_txt)
    #         output = text_txt
    #         re.sub("\.txt","\.raw", output)
    #         if match:
    #             matched = match.group()
    #             if not os.path.exists('../../data/embed/{}'.format(directory)):
    #                 os.makedirs('../../data/embed/{}'.format(directory))
    #             sentence_embedding.embed_sentences(f'{directory}/{text_txt}', "../../data/embed/{}/{}".format(directory,output),lang_mappings[matched])

