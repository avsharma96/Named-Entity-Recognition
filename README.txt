Concept Extraction of Adverse Drug Events for the MADE 1.0 Challenge
====================================================================
Contributors:
Ashwin Karthik Ambalavanan
Aditya Vikram Sharma

Students of Arizona State University, Tempe

This is a project done as part of the coursework of NLP for BioMedical Text Mining (BMI 598) under the able guidance of Professor Dr Murthy Devarakonda

Download the Project_NLP_Final folder to the C:/ Drive so that all file paths are supported.
The data set is made available to teams working on them under a data-use agreement and is strictly confidential. Hence, you would need to get the dataset on your own and then run the code given on the dataset.

The codebase is used for Named entity recognition (NER) to develop a system to automatically detect mentions of medication name and its attributes (dosage, frequency, route, duration), as well as mentions of ADEs, indications, other signs & symptoms in the MADE 1.0 Challenge.

Refer Challenge website for more information.

The Project folder contains the following folders:
1. Code- Contains the PreProcessing and Neural Network Modelling codes for different approaches used.
2. Project Dataset- Contains the required raw data (Corpus + Annotations) and the processed data written by different code.
3. Project Documents- Proposal + Mid term PPT + Final PPT
4. Project Papers Referred- Papers referred for designing our model and exploring related work.

PACKAGE DEPENDENCIES
	Python - 3.6
	Tensorflow - 1.12.0
	Keras - 2.2.2
	keras_contrib - 0.0.2
	sklearn - 0.18.1
	matplotlib - 3.0.1
	tensorflow_hub - 0.1.1
	nltk - 3.3
	gensim - 3.6.0

PROJECT DATASET FOLDER
The Project Dataset given by the MADE Challenge contains 876 Clinical Notes for Training and 213 Clinical Notes for Testing. The Annotations of each corpus is given as separate annotation xml files. These files can be found inside the Project Dataset folder inside made_train_data and made_test_data respectively.

The file "Changes as of 29-11" are the changes to be made to the dataset. These changes are made in files “clinical.csv” and in "CSV Annotations" as of 29-11-2018
The changes need to be done after running the clinical_notes_crawling and the annotation_crawling code and before the annot_mapping code. All the changes apply when you are using the Normal String replace code but only very few changes would be required when using Regex.

The Project Dataset Folder also contains the Saved Models folder which contains the model weights (.h5 files) and training logs of each of the neural network models used.

The PreProcessing Folder contains files written by the PreProcessing Python Codes which is used in later stages during Neural Network Modelling. The Regex and Normal folder shows the different types of files written from the same source data but using Regex and normal string replace for specific strings respectively.
Short File Descriptions:
	clinical.csv - Contains the Corpus ID and the Corpus Content for each of the Clinical Notes of the MADE Training Data.
	clinical_test.csv - Contains the Corpus ID and the Corpus Content for each of the Clinical Notes of the MADE Testing Data.
	CSV_Annotations.csv - Contains the Annotations crawled from the xml files of the MADE Training data combined together.
	Test_CSV_Annotations.csv - Contains the Annotations crawled from the xml files of the MADE Testing data combined together.
	Corpus_POS_Tags.csv - Contains the POS Tagged Sentences of the MADE Training Data.
	Corpus_POS_Tags_Test.csv - Contains the POS Tagged Sentences of the MADE Testing Data.
	Corpus_Sentences.csv - Contains the Sentences written from the MADE Training Clinical data.
	Corpus_Sentences_Test.csv - Contains the Sentences written from the MADE Testing Clinical data.
	Corpus_Sentences_Tags.csv - Contains the BIO Tagged Sentences of the MADE Training Data.
	Corpus_Sentences_Tags_Test.csv - Contains the BIO Tagged Sentences of the MADE Testing Data.
	word_pos_vect_PubMed.csv - Contains the word embedding of the words corresponding to the Corpus_Sentences.csv as given by PubMed Word2Vec
	word_pos_vect.csv - Contains the word embedding of the words corresponding to the Corpus_Sentences.csv using the Gensim Word2Vec package.
	wikipedia-pubmed-and-PMC-w2v.bin - Used to give words their respective embeddings as trained on PubMed Articles. DOWNLOAD THIS FILE FROM: http://evexdb.org/pmresources/vec-space-models/ and then run the pubmed.py file for proper execution.


CODE FOLDER
The PreProcessing Folder contains all the python code used to preprocess data
The Neural Network Modelling folder contains all the ipython files for Neural Network Modelling.

THE CODE SHOULD BE RUN IN THE ORDER SPECIFIED BELOW FOR CORRECT PROCESSING.

PREPROCESSING FOLDER

The preprocessing folder is for both normal and regex. Though the file names differ, the content in both is the same and the sample below is given for Regex which is the same for normal as well.

clinical_notes_crawling_regex.py - The code below crawls the corpus of the MADE 1.0 Train Data and stores them as corpus id, corpus content in the clinical.csv file.
									Input Files:
										All files in the folder corpus inside made_train_data
									Output Files:
										clinical.csv
										
test_clinical_notes_crawling_regex.py - The code below crawls the corpus of the MADE 1.0 Test Data and stores them as corpus id, corpus content in the clinical_test.csv file.
										Input Files:
											All files in the folder corpus inside made_test_data
										Output Files:
											clinical_test.csv
									
annotation_crawling.py - The code below crawls the annotations of the MADE 1.0 Train Data and stores them as Corpus ID, Annotation ID, Type, Length, Offset, Text in the 
							CSV_Annotations.csv file.
							Input Files:
								All xml files in the annotations folder in the made_train_data folder
							Output Files:
								CSV_Annotations.csv
							Note: Make sure to delete the CSV_Annotations.csv file if already existing in 
							the folder as this code appends to the existing file.
						
test_annotation_crawling.py - The code below crawls the annotations of the MADE 1.0 Test Data and stores them
								as Corpus ID, Annotation ID, Type, Length, Offset, Text in the 
								Test_CSV_Annotations.csv file.
								Input Files:
									All xml files in the annotations folder in the made_test_data folder
								Output Files:
									Test_CSV_Annotations.csv
								Note: Make sure to delete the Test_CSV_Annotations.csv file if already existing in 
								the folder as this code appends to the existing file.

annot_mapping_regex.py -     The code below Tags the annotations in the corpus of the MADE 1.0 Challenge
								Train Data with Begin (B), Inside (I) and Outside (O) tags. It maps the given
								human annotations in the CSV_Annotations.csv file to the clinical notes given
								by the clinical.csv file. The Annotations are given by indices and offsets from
								the beginning of every clinical note. Hence, care has to be taken when counting
								offsets as extra spaces, newlines and tab spaces need to be accounted for. 
								The code also uses regular expressions to remove certain words which
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
									
test_annot_mapping_regex.py -     The code below Tags the annotations in the corpus of the MADE 1.0 Challenge
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
										
pubmed.py - This file creates word and POS embeddings for words/POS in the clinical corpus  by using the pretrained word/POS embeddings from PubMed. Words whose embdeddings are 
			unknown are assigned a word embedding of 'UNK' given by PubMed
			Input Files:
				wikipedia-pubmed-and-PMC-w2v.bin
				Corpus_Sentences.csv
			Output Files:
				word_pos_vect_PubMed.csv
				
gensim.py - This file creates word and POS embeddings for words/POS in the clinical corpus  by using the Gensim Package. 
			Input Files:
				Corpus_Sentences.csv
			Output Files:
				word_pos_vect.csv			
				
NEURAL NETWORK MODELLING FOLDER
If using Pubmed and IF Corpus_Sentences, Corpus_Sentences_Tags, Corpus_Sentences_POS_Tags and the correponding test files exist, MAKE SURE TO RUN THE pubmed.py FILE BEFORE RUNNING THE FOLLOWING .ipynb FILES otherwise run all the PREPROCESSING CODE in the order mentioned above with the specified directions for correct processing.

If using Gensim and IF Corpus_Sentences, Corpus_Sentences_Tags, Corpus_Sentences_POS_Tags and the correponding test files exist, MAKE SURE TO RUN THE gensim.py FILE BEFORE RUNNING THE FOLLOWING .ipynb FILES otherwise run all the PREPROCESSING CODE in the order mentioned above with the specified directions for correct processing.

BMI_NLP_ELMo - Neural Network Modelling for NER using Embedding from Language Models (ELMo)
				Note 1: You need an active internet connection to download ELMo and cache it when running for the first time.
				Note 2: ELMo training and testing takes way too long to execute and needs a computer with atleast 32 GB RAM
				Input Files:
					Corpus_Sentences, Corpus_Sentences_Tags Corpus_POS_Tags
				Output Files:
					Corpus_Sentences_Test, Corpus_Sentences_Tags_Test, Corpus_POS_Tags_Test
					
NN_Model_Train_Test_Split - Neural Network Modelling for NER using Self-Trained Word Embeddings with train-test split
							Input Files:
								Corpus_Sentences, Corpus_Sentences_Tags Corpus_POS_Tags, word_pos_vect_PubMed.csv
							Output Files:
								Corpus_Sentences_Test, Corpus_Sentences_Tags_Test, Corpus_POS_Tags_Test
								
NN_Model_Test_Word_Embed_Regex - Neural Network Modelling for NER by letting the model learn the embeddings on its own
									Input Files:
										Corpus_Sentences, Corpus_Sentences_Tags Corpus_POS_Tags
									Output Files:
										Corpus_Sentences_Test, Corpus_Sentences_Tags_Test, Corpus_POS_Tags_Test

NN_Model_Test_PubMed - Neural Network Modelling for NER using PubMed Pre-Trained Word Embeddings
						Input Files:
							Corpus_Sentences, Corpus_Sentences_Tags Corpus_POS_Tags, word_pos_vect_PubMed.csv
						Output Files:
							Corpus_Sentences_Test, Corpus_Sentences_Tags_Test, Corpus_POS_Tags_Test
							
NN_Model_PubMed - Neural Network Modelling for NER using PubMed Pre-Trained Word Embeddings
						Input Files:
							Corpus_Sentences, Corpus_Sentences_Tags Corpus_POS_Tags, word_pos_vect_PubMed.csv
						Output Files:
							Corpus_Sentences_Test, Corpus_Sentences_Tags_Test, Corpus_POS_Tags_Test

NN_Model_Gensim - Neural Network Modelling for NER using PubMed Pre-Trained Word Embeddings
						Input Files:
							Corpus_Sentences, Corpus_Sentences_Tags Corpus_POS_Tags, word_pos_vect.csv
						Output Files:
							Corpus_Sentences_Test, Corpus_Sentences_Tags_Test, Corpus_POS_Tags_Test