"""
    The code below Tags the annotations in the corpus of the MADE 1.0 Challenge
    Train Data with Begin (B), Inside (I) and Outside (O) tags. It maps the given
    human annotations in the CSV_Annotations.csv file to the clinical notes given
    by the clinical.csv file. The Annotations are given by indices and offsets from
    the beginning of every clinical note. Hence, care has to be taken when counting
    offsets as extra spaces, newlines and tab spaces need to be accounted for. 
    The code also uses token replace to remove certain words which
    hinder sentence disambiguation. The code also writes the Sentences with tokenized
    words, corresponding sentence tags (BIO) and the corresponding POS tags to 
    three separate CSV files.
    Input Files:
        CSV_Annotations.csv
        clinical.csv
    Ouput Files:
        Corpus_Sentences.csv
        Corpus_POS_Tags.csv
        Corpus_Sentences_Tags.csv
"""

import csv
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from collections import defaultdict

clinical = open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\clinical.csv",'r', encoding = 'utf8', newline='')    
values= open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\CSV_Annotations.csv",'r', encoding = 'utf8', newline='')    

readerc = csv.reader(clinical)
readerv = csv.reader(values)

datac = list(readerc)
datav = list(readerv)

tag = list()
final = list()
c = 0

map_annot = defaultdict(list)

for i, row in enumerate(datav):
    if i == 0:
        continue
    if row[1] == '':
        map_annot[row[0]].append(row[1:])
    else:
        map_annot[row[0]].append([row[1], row[2], int(row[3]), int(row[4]), row[5]])

for row in datav:
    map_annot[row[0]].sort(key = lambda x : x[3], reverse = True)
ac=0
ac1=0
ac2=0
num_cont = 0
final_tags = list()
final_words = list()
error=list()

for i,cn in enumerate(datac): #traverse all rows
    if i == 0:
        continue
    text=word_tokenize(cn[1]) #separate words in each row
    tag = list()
    tag = ['O'] * len(text)
    for annot in map_annot[cn[0]]:
        if annot[0] == '':
            break
        annot[4] = annot[4].replace("x4", " 4")
        annot[4] = annot[4].replace("x6", " 6")
        annot[4] = annot[4].replace("x2", " 2")
        annot[4] = annot[4].replace("x1", " 1")
        annot[4] = annot[4].replace("x7", " 7")
        annot[4] = annot[4].replace("x3", " 3")
        annot[4] = annot[4].replace("x8", " 8")
        annot[4] = annot[4].replace("x9", " 9")

        annot[4] = annot[4].replace("p.m.", "p.m ")
        annot[4] = annot[4].replace("E.C.", "E.C ")
        annot[4] = annot[4].replace("a.m.", "a.m ")
        annot[4] = annot[4].replace("h.s.", "h.s ")
        annot[4] = annot[4].replace("a.c.", "a.c ")
        annot[4] = annot[4].replace("p.o.", "p.o ")
        annot[4] = annot[4].replace("No.", "No ")
        
        annot[4] = annot[4].replace("t.i.d.", "t.i.d ")
        annot[4] = annot[4].replace("q.i.d.", "q.i.d ")
        annot[4] = annot[4].replace("b.i.d.", "b.i.d ")
        annot[4] = annot[4].replace("p.r.n.", "p.r.n ")
        annot[4] = annot[4].replace("q.h.s.", "q.h.s ")
        
        annot[4] = annot[4].replace("C. diff", "C  diff")
        annot[4] = annot[4].replace("C. \ndiff", "C  \ndiff")
        annot[4] = annot[4].replace("C. \\ndiff", "C  \\ndiff")
        
        annot[4] = annot[4].replace("q.3 h.", "q.3 h ")
        annot[4] = annot[4].replace("q.6 h.", "q.6 h ")
        annot[4] = annot[4].replace("q.4 h.", "q.4 h ")
        annot[4] = annot[4].replace("q.8 h.", "q.8 h ")
        annot[4] = annot[4].replace("q.24 h.", "q.24 h ")
        annot[4] = annot[4].replace("q.24 \nh.", "q.24 \nh ")
        annot[4] = annot[4].replace("q.24 \\nh.", "q.24 \\nh ")
        
        annot[4] = annot[4].replace("q.1h.", "q.1h ")
        annot[4] = annot[4].replace("q.3h.", "q.3h ")
        annot[4] = annot[4].replace("q.4h.", "q.4h ")
        annot[4] = annot[4].replace("q.6h.", "q.6h ")
        annot[4] = annot[4].replace("q.8h.", "q.8h ")
        annot[4] = annot[4].replace("q.12h.", "q.12h ")
        annot[4] = annot[4].replace("q.48h.", "q.48h ")
        annot[4] = annot[4].replace("q.72h.", "q.72h ")
        
        annot[4] = annot[4].replace("q. 6h.", "q  6h ")
        annot[4] = annot[4].replace("q.6 \nh.", "q.6 \nh ")
        annot[4] = annot[4].replace("q.6 \\nh.", "q.6 \\nh ")
        annot[4] = annot[4].replace("q. \n12h.", "q  \n12h ")
        annot[4] = annot[4].replace("q. \\n12h.", "q  \\n12h ")
        
        annot[4] = annot[4].replace("q. 4 hours", "q  4 hours")
        annot[4] = annot[4].replace("q. 6 hours", "q  6 hours")
        annot[4] = annot[4].replace("q. 8 hours", "q  8 hours")
        annot[4] = annot[4].replace("q. 12 hours", "q  12 hours")
        annot[4] = annot[4].replace("q. 24 hours", "q  24 hours")
        annot[4] = annot[4].replace("q. 3 days", "q  3 days")
        annot[4] = annot[4].replace("q. Wednesday", "q  Wednesday")
        annot[4] = annot[4].replace("q. day", "q  day")
        annot[4] = annot[4].replace("q. 6-month", "q  6-month")
        annot[4] = annot[4].replace("q. 2 months", "q  2 months")
        annot[4] = annot[4].replace("every q.", "every q ")
        
        
        annot[4] = annot[4].replace("q.4-6h.", "q.4-6h ")
        annot[4] = annot[4].replace("q. 6-8", "q  6-8")
        annot[4] = annot[4].replace("q.3-4h.", "q.3-4h ")
        annot[4] = annot[4].replace("q. 3-4h.", "q  3-4h ")
        annot[4] = annot[4].replace("q.3 4h.", "q.3 4h ")
        annot[4] = annot[4].replace("q. 3 4h.", "q  3 4h ")
        
        annot[4] = annot[4].replace("NEC.", "NEC ")
        annot[4] = annot[4].replace("Sat.", "Sat ")
        annot[4] = annot[4].replace("GLUC.", "GLUC ")
        annot[4] = annot[4].replace("VIT.", "VIT ")
        
        annot[4] = annot[4].replace("A. fibrillation", "A  fibrillation")
        
        annot[4] = annot[4].replace("/", " ")
        annot[4] = annot[4].replace("-", " ")
        #annot[4] = annot[4].replace(",", " ")
        annot[4] = annot[4].replace("(", " ")
        annot[4] = annot[4].replace(")", " ")
        annot[4] = annot[4].replace("#", " ")
        annot[4] = annot[4].replace("..", " .")
        annot[4] = annot[4].replace("...", "  .")
        annot[4] = annot[4].replace(":", " ")
        annot[4] = annot[4].replace("[", " ")
        annot[4] = annot[4].replace("]", " ")
        annot[4] = annot[4].replace("*", " ")
        annot[4] = annot[4].replace("\"", " ")
        annot[4] = annot[4].replace("\\n", " ")
        annot[4] = annot[4].replace("\\t", " ")
        annot[4] = annot[4].replace("\n", " ")
        annot[4] = annot[4].replace("\t", " ")
        
        target = word_tokenize(annot[4]) #text from the values file
        l = int(annot[2])
        o = int(annot[3])
        count = 0
        for j, word in enumerate(text): #traverse all words in a single row
            if num_cont > 0:
                num_cont -= 1
                continue
            while(count < len(cn[1]) and (cn[1][count] == " " or cn[1][count] == "\t" or cn[1][count] == "\n")):
                    count += 1
            if count == o:
                for k, word_annot in enumerate(target):
                    """
                    flag_word_annot = 0
                    if target[-1] == '.':
                        print(target)
                        flag_word_annot = 1
                    """
                    if k == 0:
                        tag[j] = "B-" + annot[1]
                        j += 1
                        count += len(word_annot)
                        while(count < len(cn[1]) and (cn[1][count] == " " or cn[1][count] == "\t" or cn[1][count] == "\n")):
                            count += 1
                    else:
                        tag[j] = "I-" + annot[1]
                        j += 1
                        count += len(word_annot)
                        while(count < len(cn[1]) and (cn[1][count] == " " or cn[1][count] == "\t" or cn[1][count] == "\n")):
                            count += 1
                    #if(word_annot=='2'):
                    #    print(k,j-1,word,tag[j-1],count)
                num_cont = len(target) - 1
            else:
                count += len(word)
                while(count < len(cn[1]) and (cn[1][count] == " " or cn[1][count] == "\t" or cn[1][count] == "\n")):
                    count += 1
    final_tags.append(tag)
    final_words.append(text)
    count = 0
    
    annot_comp = [word_tokenize(ann[4])[0] for ann in map_annot[cn[0]] if ann[0] != '']
    
    for word, tag_find in zip(text, tag):
        if tag_find != 'O' and "I-" not in tag_find:
            count += 1
            if(word in annot_comp):
                annot_comp.remove(word)
    annot_comp
    dist_count = [[ann[1], int(ann[3]) , int(ann[3]) + int(ann[2])] for ann in map_annot[cn[0]] if ann[0] != '']
    dist_count.sort(key = lambda x:x[1])
    dist_count_final = list()
    for item in dist_count:
        flag = 0
        for itrow in dist_count_final:
            if (item[1] >= itrow[1] and item[2] <= itrow[2]) or item[1] == itrow[1]:
                flag = 1
                print(cn[0],item[0],itrow[0], item[1], item[2], itrow[1], itrow[2])
                break
        if flag == 0:
            dist_count_final.append(item)
    c += 1
    if count != len(dist_count_final):
        print("Error while annotating ", cn[0])
        error.append(cn[0])
        break
'''
with open("C:\\Users\\1796a\\Documents\\Sem 1\\NLP\\Dataset\\BIO_Tagged_Text.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for row in final_tags:
            writer.writerow(row)
'''
datac = datac[1:]

list_of_sentence = list()
list_of_sentence_tag = list()

len(final_words)
len(final_tags)

for cn, list_of_words, list_of_tags in zip(datac, final_words, final_tags):
    flag = 0
    sentences = sent_tokenize(" ".join(list_of_words))
    k = 0
    for sent in sentences:
        length = len(word_tokenize(sent))
        one_sentence = list()
        tag_sent = list()
        for word, tag_s in zip(list_of_words[k : k + length], list_of_tags[k : k + length]):
            one_sentence.append(word)
            tag_sent.append(tag_s)
            #print(k, k + length, word, " ", tag_s)
        k += length
        list_of_sentence.append(" ".join(one_sentence))
        list_of_sentence_tag.append(tag_sent)
        
#for tag_list, word_list in zip(list_of_sentence_tag, list_of_sentence):
#    print(word_list)
#    print(tag_list)

#for word, tag in zip(word_tokenize(list_of_sentence[0]), list_of_sentence_tag[0]):
#    print(word, tag)
for i, sent in enumerate(list_of_sentence):
    list_of_sentence[i] = word_tokenize(sent)
    

with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\Corpus_Sentences.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for row in list_of_sentence:
            case = [x.casefold() for x in row]
            writer.writerow(case)
            
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\Corpus_Sentences_Tags.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for row in list_of_sentence_tag:
            writer.writerow(row)
            
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\Corpus_POS_Tags.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for row in list_of_sentence_pos_tag:
            writer.writerow(row)