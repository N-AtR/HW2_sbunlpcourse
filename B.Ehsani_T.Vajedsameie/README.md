# Details for files in this folder

## sentences.py

sentences.py generates sentences for each condition for the models.
The genrated sentences are stored in "Generated Sentences" folder.

## main.py

main.py creates nGram objects which have n models in them, from 1-gram
to n-grams. This nGram class has methods to calculate the perplexity
of given text with the given model.

Probabilities for each model are calculated using maximum likelihood
estimate.
