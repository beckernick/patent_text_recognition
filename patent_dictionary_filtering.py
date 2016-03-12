# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:59:34 2016

@author: nickbecker
"""


"""
Filter patent data using regular expressions to try and keep only prior art
Could also use % of numeric digits in string to identify patents and then fix slashes, etc
"""

#-*- coding: utf-8 -*-


import pickle
import re




with open('/Users/nickbecker/Python_Projects/patent_project/O/patent_art_dict.pickle', 'rb') as handle:
  art_dict = pickle.load(handle)


"""
Loop through the dictionary and keep only patents with 3 consecutive numbers
First it replaces some incorrectly OCR'd characters ('l' and 'I' vs. '/', etc. in prior art)
This is a rudimentary way of doing the filtering.
Should/will probably combine several regex together and filter if any are true
"""

filtered_dict = {}
count = 0
limit = 500
regex2 = re.compile(r"[0-9][0-9][0-9]")
for key, values in art_dict.items():
    #print key, value
    count += 1
    if count > limit:
        break
    
    filtered_list = []
    for each in values:
        #print each
        decoded_patent = each.replace('l', '/')
        decoded_patent = each.replace('.', ',')
        
        if 'I' in each:
            decoded_patent = decoded_patent.replace('I', '/')
            
        decoded_patent = decoded_patent.decode('utf-8').replace('\xe2\x80\x94'.decode('utf-8'), '-')
        #print decoded_patent
        if re.search(regex2, decoded_patent):
            filtered_list.append(decoded_patent)
    
    if key in filtered_dict:
        filtered_dict[key] += filtered_list
        
    if key not in filtered_dict:
        filtered_dict[key] = filtered_list




# save the filtered dictionary
with open('/Users/nickbecker/Python_Projects/patent_project/O/patent_dict_filtered.pickle', 'wb') as handle:
    pickle.dump(filtered_dict, handle)









