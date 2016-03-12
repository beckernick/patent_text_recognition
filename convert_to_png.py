# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:48:56 2016

@author: nickbecker
"""


import time
import os
import subprocess


"""
NOTES:

Should manually define a test set.
Then run a parameter grid-search to tune the algorithm to optimal convert pixel density
"""


### Loop through directory of patents and convert patent pdf to a png
### Output .png version of patents to new directory called 'patent_pngs'

patents_list_path = '/Users/nickbecker/Python_Projects/patent_project/D/references'
os.chdir(patents_list_path)

patent_list = os.listdir(os.getcwd())
already_converted_list = os.listdir('/Users/nickbecker/Python_Projects/patent_project/D/references/patent_pngs/')

starting_point = patent_list.index(already_converted_list[-1][:-4] + '.pdf')
remaining_patents = patent_list[starting_point:]

count = 0
limit = 5*10**5 # limit on any one run is 50,000

for i in remaining_patents:
    time.sleep(0.1)
    if i.endswith("references.pdf"):
        #if i.split('_')[0] not in already_converted_list:
        convert_statement = 'convert -density 600 ' + i + ' /Users/nickbecker/Python_Projects/patent_project/D/references/patent_pngs/' + i[:-4] + '.png'
        subprocess.call(convert_statement, shell = True)
        
        print i.split('_')[0]
        count += 1
    if count >= limit:
        break
    else:
        continue


