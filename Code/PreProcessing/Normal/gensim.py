import csv
import nltk
from gensim.models import Word2Vec
from nltk.tokenize.nist import NISTTokenizer
from nltk.tokenize import word_tokenize

tokens_sentences = list()
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\Corpus_SentencesCase.csv", "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar= '"')
    for row in csv_reader:
        ts = [word for word in row]
        tokens_sentences.append(ts)

postag = [nltk.pos_tag(t) for t in tokens_sentences]
#Gensim W2vec model for the Corpus sentenes
model_final = Word2Vec(tokens_sentences, min_count=1, size=50)

final_pos_tag = list()
for j, pos in enumerate(postag):
    poslist = list()
    for k, pair in enumerate(pos):
        poslist.append(pair[1])
    final_pos_tag.append(poslist)
    
len(final_pos_tag)
len(tokens_sentences)

words = list(model_final.wv.vocab)
len(words)

wordvect = dict()
type(wordvect)

for i, word in enumerate(words):
    wordvect[word] = model_final[word]
#Gensim W2vec model for the POS tags of the Corpus sentenes
model_pos = Word2Vec(final_pos_tag, min_count=1, size=50)
poss = list(model_pos.wv.vocab)
posvect = dict()

for i, pos in enumerate(poss):
    posvect[pos]= model_pos[pos]

with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\word_pos_vect.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for j, sent in enumerate(postag):
            writer.writerow("S")
            for k, pair in enumerate(sent):
                writer.writerow([pair[0]] + list(wordvect[pair[0]]) + list(posvect[pair[1]]))
            writer.writerow("E")
