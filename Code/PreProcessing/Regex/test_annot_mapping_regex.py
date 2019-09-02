"""
    The code below Tags the annotations in the corpus of the MADE 1.0 Challenge
    Test Data with Begin (B), Inside (I) and Outside (O) tags. It maps the given
    human annotations in the Test_CSV_Annotations.csv file to the clinical notes given
    by the clinical_test.csv file. The Annotations are given by indices and offsets from
    the beginning of every clinical note. Hence, care has to be taken when counting
    offsets as extra spaces, newlines and tab spaces need to be accounted for. 
    The code also uses regular expressions to remove certain words which
    hinder sentence disambiguation. The code also writes the Sentences with tokenized
    words, corresponding sentence tags (BIO) and the corresponding POS tags to 
    three separate CSV files.
    Input Files:
        Test_CSV_Annotations.csv
        clinical_test.csv
    Ouput Files:
        Corpus_Sentences_Test.csv
        Corpus_POS_Tags_Test.csv
        Corpus_Sentences_Tags_Test.csv
"""

# Importing required packages

import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from collections import defaultdict
import re

# Reading the required files

clinical = open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Regex\\clinical_test.csv",'r', encoding = 'utf8', newline='')    
values= open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Regex\\Test_CSV_Annotations.csv",'r', encoding = 'utf8', newline='')    

readerc = csv.reader(clinical)
readerv = csv.reader(values)

datac = list(readerc)
datav = list(readerv)

tag = list()
final = list()
c = 0

map_annot = defaultdict(list)

# Sorting the annotations by offset to eliminate inner concepts when BIO Tagging

for i, row in enumerate(datav):
    if i == 0:
        continue
    if row[1] == '':
        map_annot[row[0]].append(row[1:])
    else:
        map_annot[row[0]].append([row[1], row[2], int(row[3]), int(row[4]), row[5]])

for row in datav:
    map_annot[row[0]].sort(key = lambda x : x[3], reverse = True)

num_cont = 0
final_tags = list()
final_words = list()
error=list()

# Performing BIO Tagging

for i,cn in enumerate(datac): 
    if i == 0:
        continue
    text=word_tokenize(cn[1]) 
    tag = list()
    tag = ['O'] * len(text)
    for annot in map_annot[cn[0]]:
        if annot[0] == '':
            break
        
        annot[4] += " "
        annot[4] = annot[4].replace("\\n",' \n')
        
        p = re.compile('[x]([0-9]+)')
        annot[4] = p.sub(r' \1', annot[4])

        p = re.compile('([A-Za-z]+[.])([A-Za-z]+)[.](\s+)')
        annot[4] = p.sub(r'\1\2 \3', annot[4])
        
        p = re.compile('([C])[.]([\s\n]+diff)')
        annot[4] = p.sub(r'\1 \2', annot[4])
        
        p = re.compile('([A-Za-z][.][0-9]+)([\s\n]+h)[.]')
        annot[4] = p.sub(r'\1\2 ', annot[4])
        
        p = re.compile('([A-Za-z][.][0-9]+h)[.]')
        annot[4] = p.sub(r'\1 ', annot[4])
        
        p = re.compile('([A-Za-z])[.](\s+)([0-9]+)(h)[.]')
        annot[4] = p.sub(r'\1 \2\3\4 ', annot[4])
        
        p = re.compile('([A-Za-z])[.](\s+)([0-9]+[-\s]+)([A-Za-z]+)')
        annot[4] = p.sub(r'\1 \2\3\4', annot[4])
        
        p = re.compile('([q])[.](\s+)([A-Za-z]*day)')
        annot[4] = p.sub(r'\1 \2\3', annot[4])
        
        p = re.compile('([A-Za-z])[.](\s*)([0-9-\s]+h)[.]')
        annot[4] = p.sub(r'\1 \2\3 ', annot[4])
        
        annot[4] = annot[4].replace("every q.", "every q ")
        annot[4] = annot[4].replace("NEC.", "NEC ")
        annot[4] = annot[4].replace("Sat.", "Sat ")
        annot[4] = annot[4].replace("GLUC.", "GLUC ")
        annot[4] = annot[4].replace("VIT.", "VIT ")
        
        annot[4] = annot[4].replace("A. fibrillation", "A  fibrillation")
        
        annot[4] = annot[4].replace("/", " ")
        annot[4] = annot[4].replace("-", " ")
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
        annot[4] = annot[4].replace("&", " ")
        annot[4] = annot[4].replace("{", " ")
        annot[4] = annot[4].replace("}", " ")
        annot[4] = annot[4].replace("@", " ")
        annot[4] = annot[4].replace("^", " ")
        annot[4] = annot[4].replace("`", " ")

        annot[4] = annot[4].replace("No.", "No ")
        annot[4] = annot[4].replace("NO_", "NO ")
        annot[4] = annot[4].replace("No_", "No ")
        
        target = word_tokenize(annot[4]) 
        l = int(annot[2])
        o = int(annot[3])
        count = 0
        for j, word in enumerate(text): 
            if num_cont > 0:
                num_cont -= 1
                continue
            while(count < len(cn[1]) and (cn[1][count] == " " or cn[1][count] == "\t" or cn[1][count] == "\n")):
                    count += 1
            if count == o:
                for k, word_annot in enumerate(target):
                    if k == 0:
                        if annot[1] != 'By Patient' and annot[1] != 'By Physician':
                            tag[j] = "B-" + annot[1]
                        j += 1
                        count += len(word_annot)
                        while(count < len(cn[1]) and (cn[1][count] == " " or cn[1][count] == "\t" or cn[1][count] == "\n")):
                            count += 1
                    else:
                        if annot[1] != 'By Patient' and annot[1] != 'By Physician':
                            tag[j] = "I-" + annot[1]
                        j += 1
                        count += len(word_annot)
                        while(count < len(cn[1]) and (cn[1][count] == " " or cn[1][count] == "\t" or cn[1][count] == "\n")):
                            count += 1
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
    dist_count = [[int(ann[3]) , int(ann[3]) + int(ann[2])] for ann in map_annot[cn[0]] if ann[0] != '']
    dist_count.sort(key = lambda x:x[0])
    dist_count_final = list()
    for item in dist_count:
        flag = 0
        for itrow in dist_count_final:
            if (item[0] >= itrow[0] and item[1] <= itrow[1]) or item[0] == itrow[0]:
                flag = 1
                print(cn[0], item[0], item[1], itrow[0], itrow[1])
                break
        if flag == 0:
            dist_count_final.append(item)
    c += 1
    if count != len(dist_count_final):
        print(cn[0])
        error.append(cn[0])

datac = datac[1:]

list_of_sentence = list()
list_of_sentence_tag = list()

len(final_words)
len(final_tags)

# Combining the tagged words to form sentences

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
        k += length
        list_of_sentence.append(" ".join(one_sentence))
        list_of_sentence_tag.append(tag_sent)
        
# Using NLTK Sentence Tokenizer to tokenize the sentences
        
for i, sent in enumerate(list_of_sentence):
    list_of_sentence[i] = word_tokenize(sent)

# POS Tagging the sentences

list_of_postag = [nltk.pos_tag(t) for t in list_of_sentence]
list_of_sentence_pos_tag = list()

for row in list_of_postag:
    temp = list()
    for i, pair in enumerate(row):
        temp.append(pair[1])
    list_of_sentence_pos_tag.append(temp)


len(list_of_sentence_tag)
len(list_of_sentence[-1])
len(list_of_sentence_pos_tag[-1])

# Writing the required files

with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Regex\\Corpus_Sentences_Test.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for row in list_of_sentence:
            case = [x.casefold() for x in row]
            writer.writerow(case)
           
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Regex\\Corpus_Sentences_Tags_Test.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for row in list_of_sentence_tag:
            writer.writerow(row)
            
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Regex\\Corpus_POS_Tags_Test.csv",'w', encoding = 'utf8', newline='') as outcsv:   
        writer = csv.writer(outcsv, delimiter=',',quotechar = '"')
        for row in list_of_sentence_pos_tag:
            writer.writerow(row)
