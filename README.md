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

Licences
-------
* License for Data - [CC 4.0 BY SA](LICENSE.data.md)
* Licence for Code - [MIT License](LICENSE.md)
