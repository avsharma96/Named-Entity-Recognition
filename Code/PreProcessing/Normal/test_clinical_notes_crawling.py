"""
    The code below crawls the corpus of the MADE 1.0 Test Data and stores them
    as corpus id, corpus content in the clinical_test.csv file.
    Input Files:
        All files in the folder corpus inside made_test_data
    Output Files:
        clinical_test.csv
"""

import csv
import os
path ="C:\\Project_NLP_Final\\Project Dataset\\made_test_data\\corpus\\"
dirListing = os.listdir(path)
files=list()
content=list()
content.append(["Content ID", "Content"])
for item in dirListing:
        data = open("C:\\Project_NLP_Final\\Project Dataset\\made_test_data\\corpus\\{}".format(item)).read()
        data = data.replace("x4", " 4")
        data = data.replace("x6", " 6")
        data = data.replace("x2", " 2")
        data = data.replace("x1", " 1")
        data = data.replace("x7", " 7")
        data = data.replace("x3", " 3")
        data = data.replace("x8", " 8")
        data = data.replace("x9", " 9")

        data = data.replace("p.m.", "p.m ")
        data = data.replace("E.C.", "E.C ")
        data = data.replace("a.m.", "a.m ")
        data = data.replace("h.s.", "h.s ")
        data = data.replace("a.c.", "a.c ")
        data = data.replace("p.o.", "p.o ")
        data = data.replace("No.", "No ")
        
        data = data.replace("t.i.d.", "t.i.d ")
        data = data.replace("q.i.d.", "q.i.d ")
        data = data.replace("b.i.d.", "b.i.d ")
        data = data.replace("p.r.n.", "p.r.n ")
        data = data.replace("q.h.s.", "q.h.s ")
        
        data = data.replace("C. diff", "C  diff")
        data = data.replace("C. \ndiff", "C  \ndiff")
        data = data.replace("C. \\ndiff", "C  \\ndiff")
        
        data = data.replace("q.3 h.", "q.3 h ")
        data = data.replace("q.6 h.", "q.6 h ")
        data = data.replace("q.4 h.", "q.4 h ")
        data = data.replace("q.8 h.", "q.8 h ")
        data = data.replace("q.24 h.", "q.24 h ")
        data = data.replace("q.24 \nh.", "q.24 \nh ")
        data = data.replace("q.24 \\nh.", "q.24 \\nh ")
        
        data = data.replace("q.1h.", "q.1h ")
        data = data.replace("q.3h.", "q.3h ")
        data = data.replace("q.4h.", "q.4h ")
        data = data.replace("q.6h.", "q.6h ")
        data = data.replace("q.8h.", "q.8h ")
        data = data.replace("q.12h.", "q.12h ")
        data = data.replace("q.48h.", "q.48h ")
        data = data.replace("q.72h.", "q.72h ")
        
        data = data.replace("q. 6h.", "q  6h ")
        data = data.replace("q.6 \nh.", "q.6 \nh ")
        data = data.replace("q.6 \\nh.", "q.6 \\nh ")
        data = data.replace("q. \n12h.", "q  \n12h ")
        data = data.replace("q. \\n12h.", "q  \\n12h ")
        
        data = data.replace("q. 4 hours", "q  4 hours")
        data = data.replace("q. 6 hours", "q  6 hours")
        data = data.replace("q. 8 hours", "q  8 hours")
        data = data.replace("q. 12 hours", "q  12 hours")
        data = data.replace("q. 24 hours", "q  24 hours")
        data = data.replace("q. 3 days", "q  3 days")
        data = data.replace("q. Wednesday", "q  Wednesday")
        data = data.replace("q. day", "q  day")
        data = data.replace("q. 6-month", "q  6-month")
        data = data.replace("q. 2 months", "q  2 months")
        data = data.replace("every q.", "every q ")
        
        
        data = data.replace("q. 3 4h.", "q  3 4h ")
        data = data.replace("q.4-6h.", "q.4-6h ")
        data = data.replace("q. 6-8", "q  6-8")
        data = data.replace("q.3-4h.", "q.3-4h ")
        data = data.replace("q.3 4h.", "q.3 4h ")
        
        
        data = data.replace("NEC.", "NEC ")
        data = data.replace("Sat.", "Sat ")
        data = data.replace("GLUC.", "GLUC ")
        data = data.replace("VIT.", "VIT ")
        
        data = data.replace("A. fibrillation", "A  fibrillation")
        
        data = data.replace("/", " ")
        data = data.replace("-", " ")
        #data = data.replace(",", " ")
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
        
        content.append([item]+[data])
        
with open("C:\\Project_NLP_Final\\Project Dataset\\PreProcessing\\Normal\\clinical_test.csv",'w', encoding = 'utf8', newline='') as outcsv:   
    writer=csv.writer(outcsv, delimiter=',', quotechar = '"')
    for row in content:
        writer.writerow(row)