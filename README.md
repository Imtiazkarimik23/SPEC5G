## Updates
* (August 8, 2023) Added annotator reasoning for a subset of examples of security classification.
* (Initial Release) The pretrained models are now available for download.

# SPEC5G

This repository contains the code and data of the paper titled [**"SPEC5G: A Dataset for 5G Cellular Network Protocol Analysis"**]("https://www.overleaf.com/project/6328efc563b20d4fea080ff8") which is accepted in AACL 2023.

SPEC5G is a dataset for the analysis of natural language specification of 5G Cellular network protocol specification. SPEC5G contains 3,547,587 sentences with 134M words, from 13094 cellular network specifications and 13 online websites. By leveraging large-scale pre-trained language models that have achieved state-of-the-art results on ML-based natural language processing (NLP) tasks, we have used this dataset for security-related text classification and summarization. Security-related text classification can be used to extract relevant security-related properties for protocol testing. On the other hand, summarization can help developers and practitioners understand the high level of the protocol, which is itself a daunting task.

SPEC5G is the first-ever public 5G dataset for NLP research on network security.



## Table of Contents

- [SPEC5G](#SPEC5G)
  - [Updates](#updates)
  - [Table of Contents](#table-of-contents)
  - [Datasets](#datasets)
  - [Models](#models)
  - [Dependencies](#dependencies)
  - [Training & Evaluation](#training--evaluation)


## Datasets
  Download the dataset from [here](https://drive.google.com/drive/folders/1Km1wdYnwjdGHiULFO0GL8JZFtDT5ZDb_?usp=sharing). This includes:
* Our original 134M Word training corpus (`Gold_5G_v4.0.zip`)
* 5GSum - Summarization Dataset (`simplification_dataset.csv`)
* 5GSC - Classification Dataset (`5GSC.csv`)
* 5GSC Annotator Reasoning - Annotator Explanation for Subset of 5GSC 

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
* [sentencepiece](https://github.com/google/sentencepiece) (`Install CLI`)
* [regex](https://pypi.org/project/regex/)
* [torchtext](https://pypi.org/project/torchtext) (`pip install torchtext==0.4.0`)

[//]: # (* [Cython]&#40;https://pypi.org/project/Cython/&#41;)


## Training & Evaluation
  * See [training and evaluation module.](model-training/)

[//]: # (  * Try out the models in [Google Colaboratory.]&#40;https://colab.research.google.com/&#41;)

[//]: # (## License)

[//]: # (Contents of this repository are licensed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License &#40;CC BY-NC-SA 4.0&#41;]&#40;https://creativecommons.org/licenses/by-nc-sa/4.0/&#41;. )

## Citation

If you use this dataset, models, or code modules, please cite the following paper:

```
@InProceedings{karim-EtAl:2023:findings,
  author    = {Karim, Imtiaz  and  Mubasshir, Kazi Samin  and  Rahman, Mirza Masfiqur  and  Bertino, Elisa},
  title     = {SPEC5G: A Dataset for 5G Cellular Network Protocol Analysis},
  booktitle      = {Proceedings of the 13th International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics},
  month          = {November},
  year           = {2023},
  address        = {Nusa Dua, Bali},
  publisher      = {Association for Computational Linguistics},
  pages     = {20--38},
  url       = {https://aclanthology.org/2023.findings-ijcnlp.3}
}
```
