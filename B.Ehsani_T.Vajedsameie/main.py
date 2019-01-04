import hazm
from random import randint, random
from collections import defaultdict
from functions import punctuationOmitter, myNormalizer
from math import log2

sentences = ""
with open("train.txt", "r") as f:
    for line in f.readlines():
        to_add = " <s> " + line + " </s> "
        sentences += to_add

test = ""
with open("test.txt", "r") as f:
    for line in f.readlines():
        to_add = " <s> " + line + " </s> "
        test += to_add


def tokenize(text, conditions):
    tmp = text[:]
    tokens = []
    if not conditions["count_punc"]:
        tmp = punctuationOmitter(text)
    if conditions["custom_tokenize"]:
        normalizer = hazm.Normalizer()
        tokens = hazm.word_tokenize(
            normalizer.normalize(myNormalizer(text))
        )
    else:
        tokens = tmp.split(" ")

    if conditions["use_lemma"]:
        lemmatizer = hazm.Lemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens


class nGram:
    def __init__(
        self,
        n,
        input_text,
        use_lemma=False,
        count_punc=True,
        custom_tokenize=True,
    ):
        self.counts = [defaultdict(int) for i in range(n)]
        self.conditions = {
            "use_lemma": use_lemma,
            "count_punc": count_punc,
            "custom_tokenize": custom_tokenize,
        }
        tokens = tokenize(input_text, self.conditions)
        self.vocab_size = len(set(tokens))
        # For unknown words
        self.vocab_size += 1
        for j in range(n):
            for i in range(len(tokens) - j):
                to_add = tokens[i : i + j + 1]
                self.counts[j][tuple(to_add)] += 1
        self.models = [{} for i in range(n)]
        self.models[0] = {
            k: v / self.vocab_size for k, v in self.counts[0].items()
        }
        for j in range(1, n):
            for key in self.counts[j].keys():
                self.models[j][key] = (
                    self.counts[j][key]
                    / self.counts[j - 1][tuple(key[:-1])]
                )

    def doc_probability(self, document, model=1):
        prob = 0
        tokens = tokenize(document, self.conditions)
        for i in range(model, len(tokens)):
            to_test = []
            for j in range(model):
                to_test.append(tokens[i - model + j])

            if tuple(to_test) not in self.models[model - 1].keys():
                prob += log2(1 / len(self.models[model - 1].keys()))
            else:
                prob += log2(self.models[model - 1][tuple(to_test)])

        return len(tokens), prob

    def perplexity(self, document, model=1):
        size, doc_prob = self.doc_probability(document, model=model)
        return 2 ** ((-1 / size) * doc_prob)


ngram = nGram(
    5, sentences, use_lemma=True, custom_tokenize=True, count_punc=False
)
print(ngram.perplexity(test, model=3))
