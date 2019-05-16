import pickle
import nltk
nltk.data.path.append("./nltk_data")

'''nltk_german_classifier_data.pickle'''

with open('nltk_german_classifier_data.pickle', 'rb') as f:
    tagger = pickle.load(f)


import random

flag = True
versionen = []
tokens = []


version1 = ""
with open("../texte/nena.txt") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        version1 += line.strip() + " "
        line = fp.readline()
        cnt += 1

version2 = ""
with open("../texte/heine.txt") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        version2 += line.strip() + " "
        line = fp.readline()
        cnt += 1

testTagsVersions = []

versionen.append(version1)
versionen.append(version2)

for versionI, version in enumerate(versionen):
    tokens.append(nltk.word_tokenize(version))
    pretoken = ""
    for tokenI, token in enumerate(tokens):
        if pretoken != "":
            print("*********")
            pretags = tagger.tag(pretoken)
            for pretagsI, pretag in enumerate(pretags):
                tags = tagger.tag(token)
                for tagI, tag in enumerate(tags):
                    if (tag == pretag):
                        testTagsVersions.append((tagI, token[tagI]))


        pretoken = token
print("------------------")
print(testTagsVersions)


for versionI, version in enumerate(versionen):
    versTokens = (nltk.word_tokenize(version))
    for tokenI, token in enumerate(versTokens):
        print(token)
