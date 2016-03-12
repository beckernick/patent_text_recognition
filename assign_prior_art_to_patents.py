# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:07:28 2016

@author: nickbecker
"""

import pandas as pd
import time
import os
import pickle
import csv



### Loop through directory of extracted prior art text and assign to a key:value pair

patents_list_path = '/Users/nickbecker/Python_Projects/patent_project/D/references/extracted_text/domestic_art/'
os.chdir(patents_list_path)

count = 0
limit = 5*10**5
patent_prior_art_dictionary = {}

for i in os.listdir(os.getcwd()):
    time.sleep(0.1)
    if i.endswith(".txt"): 
        
        tesseract_out_path = '/Users/nickbecker/Python_Projects/patent_project/D/references/extracted_text/domestic_art/' + i[:-4]
        
        ### Read in the text file from the patent
        text_data_input_path = tesseract_out_path + '.txt'
        
        current_patent = pd.read_csv(text_data_input_path, sep="\n", quoting=csv.QUOTE_NONE, header = None)
        current_patent.columns = ['patent_numbers']
        
        print i
        #print(current_patent)
        
        patent_key = i.split('_')[0]
        
        if patent_key in patent_prior_art_dictionary:
            patent_prior_art_dictionary[patent_key] += current_patent.patent_numbers.tolist()
        
        if patent_key not in patent_prior_art_dictionary:
            patent_prior_art_dictionary[patent_key] = current_patent.patent_numbers.tolist()
                
        count += 1
        if count >= limit:
            break
    else:
        continue


# save the raw dictionary
with open('/Users/nickbecker/Python_Projects/patent_project/O/patent_art_dict.pickle', 'wb') as handle:
    pickle.dump(patent_prior_art_dictionary, handle)



