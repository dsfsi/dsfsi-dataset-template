# The Vuk'uzenzele South African Multilingual Corpus
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7598539.svg)](https://doi.org/10.5281/zenodo.7598539)

## About dataset
The dataset contains editions from the South African government magazine Vuk'uzenzele. Data was scraped from PDFs that have been placed in the [data/raw](data/raw/) folder.
The PDFS were obtatined from the [Vuk'uzenzele website](https://www.vukuzenzele.gov.za/).

The datasets contain government magazine editions in 11 languages, namely:

|  Language  | Code |  Language  | Code |
|------------|-------|------------|-------|
| English    | (eng) | Sepedi     | (sep) |
| Afrikaans  | (afr) | Setswana   | (tsn) |
| isiNdebele | (nbl) | Siswati    | (ssw) |
| isiXhosa   | (xho) | Tshivenda  | (ven) |
| isiZulu    | (zul) | Xitstonga  | (tso) |
| Sesotho    | (nso) |

### Number of Aligned Pairs with Cosine Similarity Score >= 0.65

| src_lang |trg_lang | num_aligned_pairs |
| -------- | ------- | ----------------- |
| ssw      |zul      |2161|
| eng      |tso      |2016|
| ssw      |xho      |1965|
| xho      |zul      |1895|
| eng      |zul      |1888|
| tso      |zul      |1758|
| eng      |nso      |1721|
| ssw      |tso      |1657|
| eng      |ssw      |1601|
| tsn      |tso      |1570|
| afr      |ssw      |1496|
| nso      |tso      |1491|
| tso      |xho      |1485|
| afr      |zul      |1384|
| eng      |tsn      |1380|
| afr      |eng      |1369|
| afr      |xho      |1363|
| eng      |xho      |1354|
| tsn      |zul      |1346|
| nso      |tsn      |1279|
| ssw      |tsn      |1263|
| nso      |xho      |1248|
| nso      |zul      |1247|
| tsn      |xho      |1209|
| sep      |ven      |1140|
| afr      |tso      |1139|
| nso      |ssw      |1132|
| afr      |tsn      |1076|
| afr      |nso      |962|
| nbl      |sep      |843|
| nbl      |ven      |657|
| afr      |sep      |394|
| afr      |nbl      |359|
| nso      |sep      |349|
| sep      |tso      |324|
| sep      |tsn      |302|
| afr      |ven      |281|
| sep      |xho      |279|
| eng      |sep      |276|
| nbl      |ssw      |264|
| nso      |ven      |262|
| tso      |ven      |256|
| eng      |ven      |243|
| tsn      |ven      |235|
| nbl      |zul      |227|
| sep      |zul      |223|
| sep      |ssw      |219|
| ssw      |ven      |217|
| ven      |xho      |215|
| nbl      |tso      |215|
| nbl      |xho      |204|
| ven      |zul      |186|
| eng      |nbl      |153|
| nbl      |nso      |151|
| nbl      |tsn      |140|


The dataset is present in several forms on the repo. 
Generally the dataset is split by edition, eg. `2020-01-ed1`  
The data directory is broken down as follows
```
./data
├── external                # Data external to this repo
├── interim                 # I am not really sure - looks like interim in regards to processed.
├── processed               # The data from scraping the raw pdfs
├── raw                     # The raw pdfs of the Vuk'uzenzele magazine
├── sentence_align_output   # The output (csv) of the sentence alignment with LASER language encoders
└── simple_align_output     # The output (csv) of a simple one to one sentence alignment
```
The dataset is split by edition in the [data/processed](data/processed/) folder.

Authors
-------
- Vukosi Marivate - [@vukosi](https://twitter.com/vukosi)
- Andani Madodonga
- Daniel Njini
- Richard Lastrucci
- Isheanesu Dzingirai
- Jenalea Rajab

Citation
--------
Preprint/Paper

[Preparing the Vuk'uzenzele and ZA-gov-multilingual South African  multilingual corpora](https://arxiv.org/pdf/2303.03750)

> @article{lastrucci2023preparing,
  title   = {Preparing the Vuk'uzenzele and ZA-gov-multilingual South African multilingual corpora},
  author  = {Richard Lastrucci and Isheanesu Dzingirai and Jenalea Rajab and Andani Madodonga and Matimba Shingange and Daniel Njini and Vukosi Marivate},
  year    = {2023},
  journal = {arXiv preprint arXiv: Arxiv-2303.03750}
}

Dataset

Vukosi Marivate, Andani Madodonga, Daniel Njini, Richard Lastrucci, Isheanesu Dzingirai, Jenalea Rajab. **The Vuk'uzenzele South African Multilingual Corpus**, 2023

> @dataset{marivate_vukosi_2023_7598540,
  author       = {Marivate, Vukosi and
                  Njini, Daniel and
                  Madodonga, Andani and
                  Lastrucci, Richard and
                  Dzingirai, Isheanesu
                  Rajab, Jenalea},
  title        = {The Vuk'uzenzele South African Multilingual Corpus},
  month        = feb,
  year         = 2023,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.7598539},
  url          = {https://doi.org/10.5281/zenodo.7598539}
}

Licences
-------
* License for Data - [CC 4.0 BY SA](LICENSE.data.md)
* Licence for Code - [MIT License](LICENSE.md)
