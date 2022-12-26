# SPEC5G

This repository contains the code and data of the paper titled [**"SPEC5G: A Dataset for 5G Cellular Network Protocol Analysis"**]("https://www.overleaf.com/project/6328efc563b20d4fea080ff8") published in *The 17th Conference of the European Chapter of the Association for Computational Linguistics, 2023.*

## Updates

* The pretrained models are now available for download.


## Table of Contents

- [SPEC5G](#SPEC5G)
  - [Updates](#updates)
  - [Table of Contents](#table-of-contents)
  - [Datasets](#datasets)
  - [Models](#models)
  - [Dependencies](#dependencies)
  - [Training & Evaluation](#training--evaluation)
  - [License](#license)
  - [Citation](#citation)


## Datasets
  Download the dataset from [here](https://drive.google.com/drive/folders/11x0_IonTROgQOfH_DUyAJ2U3vabXa_Fn). This includes:
* Our original 134M Word training corpus (`Gold_5G_v3.0.zip`)
* 5GSum - Summarization Dataset (`simplification_dataset.csv`)
* 5GSC - Classification Dataset (`cf_dataset2.csv`)

## Models

The pretrained model checkpoints can be found below: 

* [BERT5G](https://drive.google.com/file/d/1Di-Tuoxmfjdu8JnNjHRts0g-rLDdNfsM/view?usp=share_link)
* [RoBERTa5G](https://drive.google.com/file/d/1R9eWnBArusiEv2NuFth5cC2O0sO0D6vy/view?usp=share_link)
* [XLNET5G](https://drive.google.com/file/d/1pMPNGKEyNzFDfZtpBluEIZAG_zyI3XvN/view?usp=share_link)

## Dependencies
* Python 3.7+
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
* [textract](https://pypi.org/project/textract/)
* [selenium](https://pypi.org/project/selenium/)
* [datasets](https://pypi.org/project/datasets/)
* [tokenizers](https://pypi.org/project/tokenizers/)
* [transformers](https://pypi.org/project/transformers/)
* [rouge_score](https://pypi.org/project/rouge_score/)
* [PyTorch](http://pytorch.org/)

[//]: # (* [Cython]&#40;https://pypi.org/project/Cython/&#41;)
* [sentencepiece](https://github.com/google/sentencepiece) (`Install CLI`)
* [regex](https://pypi.org/project/regex/)
* [torchtext](https://pypi.org/project/torchtext) (`pip install torchtext==0.4.0`)


## Training & Evaluation
  * See [training and evaluation module.](model-training/)

[//]: # (  * Try out the models in [Google Colaboratory.]&#40;https://colab.research.google.com/&#41;)

## License
Contents of this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/). 

## Citation
If you use this dataset or code modules, please cite the following paper:
```
@inproceedings{hasan-etal-2020-low,
    title = "SPEC5G: A Dataset for 5G Cellular Network Protocol Analysis",
    author = "Karim, Imtiaz  and
      Mubasshir, Kazi Samin  and
      Rahman, Mirza Masfiqur  and
      Bertino, Elisa",
    booktitle = "The 17th Conference of the European Chapter of the Association for Computational Linguistics",
    month = jan,
    year = "2023",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2023.eacl-main.207",
    doi = "10.18653/v1/2023.eacl-main.207",
    pages = "2612--2623",
    abstract = "5G is the 5th generation cellular network protocol. It is the state-of-the-art global wireless standard that enables an advanced kind of network--designed to connect virtually everyone and everything with increased speed and reduced latency. Therefore, its development, analysis, and security are critical. However, all approaches to the 5G protocol development and security analysis, e.g., property extraction, protocol summarization, and semantic analysis of the protocol specifications and implementations are completely manual. To reduce such manual efforts, in this paper, we curate SPEC5G the first-ever public 5G dataset for NLP research. The dataset contains 3,547,587 sentences with 134M words, from 13094 cellular network specifications and 13 online websites. By leveraging large-scale pre-trained language models that have achieved state-of-the-art results on NLP tasks, we use this dataset for security-related text classification and summarization. Security-related text classification can be used to extract relevant security-related properties for protocol testing. On the other hand, summarization can help developers and practitioners understand the high level of the protocol, which is itself a daunting task. Our results show the value of our 5G-centric dataset in 5G protocol analysis automation. We believe that SPEC5G will enable a new research direction into automatic analyses for the 5G cellular network protocol and numerous related downstream tasks.",
}
```