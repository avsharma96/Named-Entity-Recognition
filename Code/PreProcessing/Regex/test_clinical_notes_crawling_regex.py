"""
    The code below crawls the corpus of the MADE 1.0 Test Data and stores them
    as corpus id, corpus content in the clinical_test.csv file.
    Input Files:
        All files in the folder corpus inside made_test_data
    Output Files:
        clinical_test.csv
"""

# Importing required packages

import csv
import os
import re

# Reading required files from the corpus folder
path ="C:\\Project_NLP_Final\\Project Dataset\\made_test_data\\corpus\\"
dirListing = os.listdir(path)
files=list()
content=list()
content.append(["Content ID", "Content"])
for item in dirListing:
        data = open("C:\\Project_NLP_Final\\Project Dataset\\made_test_data\\corpus\\{}".format(item)).read()
        data = data.replace("\\n",' \n')
        
        p = re.compile('[x]([0-9]+)')
        data = p.sub(r' \1', data)

        p = re.compile('([A-Za-z]+[.])([A-Za-z]+)[.](\s+)')
        data = p.sub(r'\1\2 \3', data)
        
        p = re.compile('([C])[.]([\s\n]+diff)')
        data = p.sub(r'\1 \2', data)
        
        p = re.compile('([A-Za-z][.][0-9]+)([\s\n]+h)[.]')
        data = p.sub(r'\1\2 ', data)
        
        p = re.compile('([A-Za-z][.][0-9]+h)[.]')
        data = p.sub(r'\1 ', data)
        
        p = re.compile('([A-Za-z])[.](\s+)([0-9]+)(h)[.]')
        data = p.sub(r'\1 \2\3\4 ', data)
        
        p = re.compile('([A-Za-z])[.](\s+)([0-9]+[-\s]+)([A-Za-z]+)')
        data = p.sub(r'\1 \2\3\4', data)
        
        p = re.compile('([q])[.](\s+)([A-Za-z]*day)')
        data = p.sub(r'\1 \2\3', data)
        
        p = re.compile('([A-Za-z])[.](\s*)([0-9-\s]+h)[.]')
        data = p.sub(r'\1 \2\3 ', data)
        
        data = data.replace("every q.", "every q ")
        data = data.replace("NEC.", "NEC ")
        data = data.replace("Sat.", "Sat ")
        data = data.replace("GLUC.", "GLUC ")
        data = data.replace("VIT.", "VIT ")
        
        data = data.replace("A. fibrillation", "A  fibrillation")
        
        data = data.replace("/", " ")
        data = data.replace("-", " ")
        data = data.replace("(", " ")
        data = data.replace(")", " ")
        data = data.replace("#", " ")
        data = data.replace("..", " .")
        data = data.replace("...", "  .")
        data = data.replace(":", " ")
        data = data.replace("[", " ")
        data = data.replace("]", " ")
        data = data.replace("*", " ")
        data = data.replace("\"", " ")
        data = data.replace("&", " ")
        data = data.replace("{", " ")
        data = data.replace("}", " ")
        data = data.replace("@", " ")
        data = data.replace("^", " ")
        data = data.replace("`", " ")
        data = data.replace("No.", "No ")
        data = data.replace("NO_", "NO ")
        data = data.replace("No_", "No ")
        
        content.append([item]+[data])
        
        
# Writing the content to the clinical.csv file
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Regex\\clinical_test.csv",'w', encoding = 'utf8', newline='') as outcsv:   
    writer=csv.writer(outcsv, delimiter=',', quotechar = '"')
    for row in content:
        writer.writerow(row)