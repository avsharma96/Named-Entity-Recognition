"""
    This file creates word and POS embeddings for words/POS in the clinical corpus 
    by using the pretrained word/POS embeddings from PubMed. 
    Words whose embdeddings are unknown are assigned a word embedding of 'UNK' given by PubMed
    Input Files:
        wikipedia-pubmed-and-PMC-w2v.bin
        Corpus_Sentences.csv
    Output Files:
        word_pos_vect_PubMed.csv
"""

import gensim
import csv
import nltk
import numpy as np
model = gensim.models.KeyedVectors.load_word2vec_format('C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\wikipedia-pubmed-and-PMC-w2v.bin', binary=True)  
model.vector_size
tokens_sentences = list()
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\Corpus_Sentences.csv", "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar= '"')
    for row in csv_reader:
        ts = [word for word in row]
        tokens_sentences.append(ts)
model.word_vec('UNK')
default = np.zeros(200).astype('float32')
wordvect = dict()
posvect = dict()
type(wordvect)
for i in range(len(tokens_sentences)):
    for j in range(len(tokens_sentences[i])):
        try:
            wordvect[tokens_sentences[i][j]] = model.word_vec(tokens_sentences[i][j])
        except:
             wordvect[tokens_sentences[i][j]] = model.word_vec('UNK')
len(wordvect)
postag = [nltk.pos_tag(t) for t in tokens_sentences]
final_pos_tag = list()
for j, pos in enumerate(postag):
    poslist = list()
    for k, pair in enumerate(pos):
        poslist.append(pair[1])
    final_pos_tag.append(poslist)
for i in range(len(final_pos_tag)):
    for j in range(len(final_pos_tag[i])):
        try:
            posvect[final_pos_tag[i][j]] = model.word_vec(final_pos_tag[i][j])
        except:
            posvect[final_pos_tag[i][j]] =  model.word_vec('UNK')
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\word_pos_vect_PubMed.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for j, sent in enumerate(postag):
            writer.writerow("S")
            for k, pair in enumerate(sent):
                writer.writerow([pair[0]] + list(wordvect[pair[0]]) + list(posvect[pair[1]]))
            writer.writerow("E")