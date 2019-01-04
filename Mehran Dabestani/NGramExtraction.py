from nltk import ngrams
from collections import Counter
import random
import codecs
import numpy as np
import math


def generate_ngrams():
    with codecs.open("Train.txt", encoding='utf-8') as trainFile:
        sentences = trainFile.read().split("\n")

    for sentence in sentences:
        sentence = "<s> " + sentence + " </s>"
        sentence = sentence.replace("*", " ")
        for x in range(1, 6):
            grams = ngrams(sentence.split(), x)
            with codecs.open(`x` + "-grams.txt", "a", encoding='utf-8') as ngramFile:
                for gram in grams:
                    ngramFile.write(",".join(gram))
                    ngramFile.write("\n")


def generate_unigrams_for_test_data():
    with codecs.open("Test.txt", encoding='utf-8') as testFile:
        sentences = testFile.read().split("\n")

    for sentence in sentences:
        sentence = "<s> " + sentence + " </s>"
        sentence = sentence.replace("*", " ")
        grams = ngrams(sentence.split(), 1)
        with codecs.open("unigrams-for-test-data.txt", "a", encoding='utf-8') as ngramFile:
            for gram in grams:
                ngramFile.write(",".join(gram))
                ngramFile.write("\n")


def compute_unigrams_probability():
    with codecs.open("1-grams.txt", "r", encoding='utf-8') as ngramFile:
        ngrams = ngramFile.read().split("\n")
        counter = Counter(ngrams)
        numberOfUniqueWords = len(counter)
        for attribute, value in counter.items():
            probability = value / float(numberOfUniqueWords)
            with codecs.open("1-grams-probabilities.txt", "a", encoding='utf-8') as ngramProbabilityFile:
                ngramProbabilityFile.write(
                    attribute + " " + `probability`)
                ngramProbabilityFile.write("\n")


def compute_unigrams_probability_for_test_data():
    with codecs.open("unigrams-for-test-data.txt", "r", encoding='utf-8') as ngramFile:
        ngrams = ngramFile.read().split("\n")
        counter = Counter(ngrams)
        numberOfUniqueWords = len(counter)
        for attribute, value in counter.items():
            probability = value / float(numberOfUniqueWords)
            with codecs.open("unigram-probabilities-for-test-data.txt", "a", encoding='utf-8') as ngramProbabilityFile:
                ngramProbabilityFile.write(
                    attribute + " " + `probability`)
                ngramProbabilityFile.write("\n")


def compute_other_probabilities():
    for x in range(2, 6):
        with codecs.open(`x` + "-grams.txt", "r", encoding='utf-8') as ngramFile:
            y = x-1
            with codecs.open(`y` + "-grams.txt", "r", encoding='utf-8') as previousNgramFile:
                ngrams = ngramFile.read().split("\n")
                ngramsCounter = Counter(ngrams)
                previousNgrams = previousNgramFile.read().split("\n")
                previousNgramsCounter = Counter(previousNgrams)
                for attribute, value in ngramsCounter.items():
                    previousAttribute = ",".join(attribute.split(",")[:-1])
                    probability = value / \
                        float(previousNgramsCounter[previousAttribute])
                    with codecs.open(`x` + "-grams-probabilities.txt", "a", encoding='utf-8') as ngramProbabilityFile:
                        ngramProbabilityFile.write(
                            attribute + " " + `probability`)
                        ngramProbabilityFile.write("\n")


def generate_sentences():
    for x in range(1, 6):
        with codecs.open(`x` + "-grams-probabilities.txt", "r", encoding='utf-8') as ngramProbabilityFile:
            grams = ngramProbabilityFile.read().split("\n")
            for m in range(100):
                word = ""
                words = []
                probabilities = []
                sentence = ""
                for i in grams:
                    words.append(i.split()[0])
                    probabilities.append(float(i.split()[1]))
                if x == 1:
                    randomIndex = random.randint(0, len(words)-1)
                    word = words[randomIndex]
                    sentence += word + " "
                else:
                    foundFirstWord = False
                    while not foundFirstWord:
                        randomIndex = random.randint(0, len(words)-1)
                        if words[randomIndex].split(",")[0] == "<s>":
                            foundFirstWord = True
                            word = " ".join(words[randomIndex].split(",")[:-1])
                            sentence += word + " "
                while word != "</s>":
                    if x == 1:
                        word = np.random.choice(words, 1, probabilities)[0]
                        sentence += word + " "
                    else:
                        xlastWordsOfSentence = " ".join(
                            sentence.split()[-x+1:])
                        selectedWords = []
                        selectedWordsProbabilities = []
                        for i in range(len(words)):
                            w = words[i]
                            if xlastWordsOfSentence == " ".join(w.split(",")[:-1]):
                                selectedWords.append(w.split(",")[-1])
                                selectedWordsProbabilities.append(
                                    probabilities[i])
                        word = np.random.choice(selectedWords, 1, selectedWordsProbabilities)[
                            0]
                        sentence += word + " "
                with codecs.open(`x` + "-grams-generated-sentences.txt", "a", encoding='utf-8') as generetedSentencesFile:
                    generetedSentencesFile.write(sentence + "\n")


def compute_generated_sentences_perplexities():
    with codecs.open("1-grams-probabilities.txt", "r", encoding='utf-8') as unigramProbabilities:
        grams = unigramProbabilities.read().split("\n")
        words = []
        probabilities = []
        for i in grams:
            words.append(i.split()[0])
            probabilities.append(float(i.split()[1]))
        for x in range(1, 6):
            with codecs.open(`x` + "-grams-generated-sentences.txt", "r", encoding='utf-8') as generatedSentencesFile:
                with codecs.open(`x` + "-grams-generated-sentences-perplexity.txt", "a", encoding='utf-8') as generatedSentencesPerplexityFile:
                    sentences = generatedSentencesFile.read().split("\n")
                    for sentence in sentences:
                        sentenceWords = sentence.split()
                        perplexity = 1
                        for word in sentenceWords:
                            perplexity *= math.fabs(
                                math.log(probabilities[words.index(word)], 10))
                        perplexity = math.pow(
                            perplexity, -1/len(sentenceWords))
                        generatedSentencesPerplexityFile.write(
                            `perplexity` + "\n")


def compute_test_file_perplexity():
    with codecs.open("unigram-probabilities-for-test-data.txt", "r", encoding='utf-8') as unigramProbabilities:
        grams = unigramProbabilities.read().split("\n")
        words = []
        probabilities = []
        for i in grams:
            words.append(i.split()[0])
            probabilities.append(float(i.split()[1]))
        with codecs.open("Test.txt", "r", encoding='utf-8') as TestFile:
            with codecs.open("Test-perplexity.txt", "a", encoding='utf-8') as TestPerplexityFile:
                sentences = TestFile.read().split("\n")
                for sentence in sentences:
                    sentence = "<s> " + sentence + " </s>"
                    sentence = sentence.replace("*", " ")
                    sentenceWords = sentence.split()
                    perplexity = 1
                    for word in sentenceWords:
                        perplexity *= math.fabs(
                            math.log(probabilities[words.index(word)], 10))
                    perplexity = math.pow(
                        perplexity, -1/len(sentenceWords))
                    TestPerplexityFile.write(
                        `perplexity` + "\n")
