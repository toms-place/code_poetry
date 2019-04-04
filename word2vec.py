from gensim.models import Word2Vec
from poeti.src import getLines
sentences = getLines.fromTXT("./texte/nena.txt")
model = Word2Vec(sentences, min_count=1)
vector = model.wv['General']  # numpy vector of a word
test = model.wv.most_similar("luft")  # numpy vector of a word
print(test)