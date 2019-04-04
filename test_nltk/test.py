import pickle
import nltk
nltk.data.path.append("./nltk_data")

with open('nltk_german_classifier_data.pickle', 'rb') as f:
    tagger = pickle.load(f)

string = ""
with open("../texte/nena.txt") as fp:
    line = fp.readline()
    cnt = 1
    while line:
        string += line.strip() + " "
        line = fp.readline()
        cnt += 1

tockens = nltk.word_tokenize(string)

print(tagger.tag(tockens))
