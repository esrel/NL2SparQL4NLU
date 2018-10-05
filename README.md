# NL2SparQL4NLU

This repository contains data derived from NL2SPARQL data set from Microsoft Research. The data has beed used for the [Language Understanding Systems](http://disi.unitn.it/~riccardi/page7/page13/page13.html) class of University of Trento from 2014.

## Data Description
The data is split into training and tests sets following the original split of NL2SparQL dataset. 
Everything that contains 'train' is for training, 'test' for testing; otherwise, the formats are the same.
There are 4 files per split, differentiated by extensions.

Specifically, extensions and contents are the following:


- `*.conll.txt` 
	token-per-line CONLL format with tokens & NLU concept tags;
	automatically extracted from SPARQL queries & manually inspected.

- `*.features.conll.txt`
	POS-tag and Lemmas in token-per-line CONLL format (with tokens on the first column); 
	produced automatically using TreeTagger.

- `*.utterances.txt`
	utterance only; in utterance-per-line format.

- `*.utterance.labels.txt`
	labels per utterance for intent/utterance classification; automatically extracted from SPARQL queries.

The data has been modified from the original with respect to tokenization of possessive apostrophes.

E.G:
original: find the female actress from the movie she s the man
modified: find the female actress from the movie she 's the man

(+ some other fixes)

## References
If you use this dataset for publication, please cite the following two papers:

1.  Yun-Nung Chen, Dilek Hakkani-Tur, and Gokan Tur. "Deriving local relational surface forms from dependency-based entity embeddings for unsupervised spoken language understanding". Spoken Language Technology Workshop (SLT), 2014 IEEE, pages 242–247, 2014.
2. Jacopo Gobbi, Evgeny A. Stepanov, and Giuseppe Riccardi. "Concept Tagging for Natural Language Understanding: Two Decadelong Algorithm Development". Fifth Italian Conference on Computational Linguistics, Turin, December 10-12, 2018.


