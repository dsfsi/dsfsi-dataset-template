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

| src_lang | trg_lang | num_aligned_pairs |
|----------|----------|-------------------|
| ven      | zul      | 186               |
| ssw      | xho      | 1965              |
| sep      | xho      | 279               |
| nbl      | zul      | 227               |
| nso      | tsn      | 1279              |
| nso      | tso      | 1491              |
| tsn      | zul      | 1346              |
| afr      | eng      | 1369              |
| eng      | ssw      | 1601              |
| afr      | ssw      | 1496              |
| nbl      | ssw      | 264               |
| tso      | zul      | 1758              |
| afr      | zul      | 1384              |
| eng      | zul      | 1888              |
| ssw      | tsn      | 1263              |
| sep      | tsn      | 302               |
| nso      | xho      | 1248              |
| sep      | tso      | 324               |
| ssw      | tso      | 1657              |
| tsn      | ven      | 235               |
| eng      | nbl      | 153               |
| nso      | sep      | 349               |
| afr      | nbl      | 359               |
| nbl      | ven      | 657               |
| eng      | ven      | 243               |
| afr      | ven      | 281               |
| tso      | ven      | 256               |
| ven      | xho      | 215               |
| eng      | tsn      | 1380              |
| afr      | tsn      | 1076              |
| nso      | ssw      | 1132              |
| eng      | tso      | 2016              |
| afr      | tso      | 1139              |
| xho      | zul      | 1895              |
| tsn      | xho      | 1209              |
| sep      | zul      | 223               |
| nbl      | xho      | 204               |
| ssw      | zul      | 2161              |
| afr      | xho      | 1363              |
| eng      | xho      | 1354              |
| tso      | xho      | 1485              |
| sep      | ssw      | 219               |
| nbl      | tso      | 215               |
| tsn      | tso      | 1570              |
| nso      | zul      | 1247              |
| nbl      | tsn      | 140               |
| eng      | sep      | 276               |
| afr      | sep      | 394               |
| ssw      | ven      | 217               |
| sep      | ven      | 1140              |
| afr      | nso      | 962               |
| eng      | nso      | 1721              |
| nbl      | nso      | 151               |
| nbl      | sep      | 843               |
| nso      | ven      | 262               |


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

Citation
--------
Vukosi Marivate, Andani Madodonga, Daniel Njini, Richard Lastrucci, Isheanesu Dzingirai
. **The Vuk'uzenzele South African Multilingual Corpus**, 2023

> @dataset{marivate_vukosi_2023_7598540,
  author       = {Marivate, Vukosi and
                  Njini, Daniel and
                  Madodonga, Andani and
                  Lastrucci, Richard and
                  Dzingirai, Isheanesu},
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
