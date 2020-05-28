from hazm import *
from functions import myNormalizer, punctuationOmitter
from random import randint

text_in = open("train_data_out.txt", "r", encoding="utf8")
text_file = text_in.read()
text_in.close()
text_file_puncless = punctuationOmitter(text_file)

normalizer = Normalizer()
tokens_hooshmand = word_tokenize(normalizer.normalize(myNormalizer(text_file)))
tokens_space_splitter = text_file.split(" ")

tokens_hooshmand_puncless = word_tokenize(
    normalizer.normalize(myNormalizer(text_file_puncless)))
tokens_space_splitter_puncless = text_file_puncless.split(" ")

# q2
with open("q2/token_hooshmand.txt", "w+", encoding="utf8") as out:
    for data in tokens_hooshmand:
        out.write("%s\n" % data)

with open("q2/token_space_splitter.txt", "w+", encoding="utf8") as out:
    for data in tokens_space_splitter:
        out.write("%s\n" % data)

with open("q2/token_hooshmand_puncless.txt", "w+", encoding="utf8") as out:
    for data in tokens_hooshmand_puncless:
        out.write("%s\n" % data)

with open("q2/token_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    for data in tokens_space_splitter_puncless:
        out.write("%s\n" % data)


# q3
# q3 - token_hooshmand
txt = ''
for i in range(100):
    for j in range(randint(5, 8)):
        index = randint(0, len(tokens_hooshmand))
        txt += tokens_hooshmand[index] + ' '
    txt += '\n'

with open("q3/token_hooshmand/1-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_hooshmand)-1)
        txt += tokens_hooshmand[index] + ' ' + \
            tokens_hooshmand[index + 1] + ' '

    txt += '\n'

with open("q3/token_hooshmand/2-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_hooshmand)-2)
        txt += tokens_hooshmand[index] + ' ' + \
            tokens_hooshmand[index + 1] + ' ' + \
            tokens_hooshmand[index + 2] + ' '

    txt += '\n'

with open("q3/token_hooshmand/3-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(2, 4)):
        index = randint(0, len(tokens_hooshmand)-3)
        txt += tokens_hooshmand[index] + ' ' + \
            tokens_hooshmand[index + 1] + ' ' + \
            tokens_hooshmand[index + 2] + ' ' + \
            tokens_hooshmand[index + 3] + ' '

    txt += '\n'

with open("q3/token_hooshmand/4-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(1, 2)):
        index = randint(0, len(tokens_hooshmand)-4)
        txt += tokens_hooshmand[index] + ' ' + \
            tokens_hooshmand[index + 1] + ' ' + \
            tokens_hooshmand[index + 2] + ' ' + \
            tokens_hooshmand[index + 3] + ' ' + \
            tokens_hooshmand[index + 4] + ' '

    txt += '\n'

with open("q3/token_hooshmand/5-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

# q3 - token_hooshmand_puncless
txt = ''
for i in range(100):
    for j in range(randint(5, 8)):
        index = randint(0, len(tokens_hooshmand_puncless))
        txt += tokens_hooshmand_puncless[index] + ' '
    txt += '\n'

with open("q3/token_hooshmand_puncless/1-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_hooshmand_puncless)-1)
        txt += tokens_hooshmand_puncless[index] + ' ' + \
            tokens_hooshmand_puncless[index + 1] + ' '

    txt += '\n'

with open("q3/token_hooshmand_puncless/2-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_hooshmand_puncless)-2)
        txt += tokens_hooshmand_puncless[index] + ' ' + \
            tokens_hooshmand_puncless[index + 1] + ' ' + \
            tokens_hooshmand_puncless[index + 2] + ' '

    txt += '\n'

with open("q3/token_hooshmand_puncless/3-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(2, 4)):
        index = randint(0, len(tokens_hooshmand_puncless)-3)
        txt += tokens_hooshmand_puncless[index] + ' ' + \
            tokens_hooshmand_puncless[index + 1] + ' ' + \
            tokens_hooshmand_puncless[index + 2] + ' ' + \
            tokens_hooshmand_puncless[index + 3] + ' '

    txt += '\n'

with open("q3/token_hooshmand_puncless/4-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(1, 2)):
        index = randint(0, len(tokens_hooshmand_puncless)-4)
        txt += tokens_hooshmand_puncless[index] + ' ' + \
            tokens_hooshmand_puncless[index + 1] + ' ' + \
            tokens_hooshmand_puncless[index + 2] + ' ' + \
            tokens_hooshmand_puncless[index + 3] + ' ' + \
            tokens_hooshmand_puncless[index + 4] + ' '

    txt += '\n'

with open("q3/token_hooshmand_puncless/5-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

# q3 - token_space_splitter
txt = ''
for i in range(100):
    for j in range(randint(5, 8)):
        index = randint(0, len(tokens_space_splitter))
        txt += tokens_space_splitter[index] + ' '
    txt += '\n'

with open("q3/token_space_splitter/1-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_space_splitter)-1)
        txt += tokens_space_splitter[index] + ' ' + \
            tokens_space_splitter[index + 1] + ' '

    txt += '\n'

with open("q3/token_space_splitter/2-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_space_splitter)-2)
        txt += tokens_space_splitter[index] + ' ' + \
            tokens_space_splitter[index + 1] + ' ' + \
            tokens_space_splitter[index + 2] + ' '

    txt += '\n'

with open("q3/token_space_splitter/3-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(2, 4)):
        index = randint(0, len(tokens_space_splitter)-3)
        txt += tokens_space_splitter[index] + ' ' + \
            tokens_space_splitter[index + 1] + ' ' + \
            tokens_space_splitter[index + 2] + ' ' + \
            tokens_space_splitter[index + 3] + ' '

    txt += '\n'

with open("q3/token_space_splitter/4-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(1, 2)):
        index = randint(0, len(tokens_space_splitter)-4)
        txt += tokens_space_splitter[index] + ' ' + \
            tokens_space_splitter[index + 1] + ' ' + \
            tokens_space_splitter[index + 2] + ' ' + \
            tokens_space_splitter[index + 3] + ' ' + \
            tokens_space_splitter[index + 4] + ' '

    txt += '\n'

with open("q3/token_space_splitter/5-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)


# q3 - token_space_splitter
txt = ''
for i in range(100):
    for j in range(randint(5, 8)):
        index = randint(0, len(tokens_space_splitter_puncless))
        txt += tokens_space_splitter_puncless[index] + ' '
    txt += '\n'

with open("q3/token_space_splitter_puncless/1-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_space_splitter_puncless)-1)
        txt += tokens_space_splitter_puncless[index] + ' ' + \
            tokens_space_splitter_puncless[index + 1] + ' '

    txt += '\n'

with open("q3/token_space_splitter_puncless/2-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(3, 5)):
        index = randint(0, len(tokens_space_splitter_puncless)-2)
        txt += tokens_space_splitter_puncless[index] + ' ' + \
            tokens_space_splitter_puncless[index + 1] + ' ' + \
            tokens_space_splitter_puncless[index + 2] + ' '

    txt += '\n'

with open("q3/token_space_splitter_puncless/3-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(2, 4)):
        index = randint(0, len(tokens_space_splitter_puncless)-3)
        txt += tokens_space_splitter_puncless[index] + ' ' + \
            tokens_space_splitter_puncless[index + 1] + ' ' + \
            tokens_space_splitter_puncless[index + 2] + ' ' + \
            tokens_space_splitter_puncless[index + 3] + ' '

    txt += '\n'

with open("q3/token_space_splitter_puncless/4-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)

txt = ''
for i in range(100):
    for j in range(randint(1, 2)):
        index = randint(0, len(tokens_space_splitter_puncless)-4)
        txt += tokens_space_splitter_puncless[index] + ' ' + \
            tokens_space_splitter_puncless[index + 1] + ' ' + \
            tokens_space_splitter_puncless[index + 2] + ' ' + \
            tokens_space_splitter_puncless[index + 3] + ' ' + \
            tokens_space_splitter_puncless[index + 4] + ' '

    txt += '\n'

with open("q3/token_space_splitter_puncless/5-gram_space_splitter_puncless.txt", "w+", encoding="utf8") as out:
    out.write("%s" % txt)
