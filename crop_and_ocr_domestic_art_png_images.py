# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 07:52:00 2016

@author: nickbecker
"""

from PIL import Image
import time
import os
import subprocess

"""
This program crops the patent to identify and OCR the domestic prior art
"""


### Loop through directory of patent PNGs. Crop them and run OCR

patents_list_path = '/Users/nickbecker/Python_Projects/patent_project/D/references/patent_pngs'
os.chdir(patents_list_path)

dimensions = (600, 1025, 1500, 2980) # approximate prior art boundary coordinates for 600 dpi pdf-png conversion
count = 0
limit = 5*10**5

for i in os.listdir(os.getcwd()):
    time.sleep(0.1)
    if i.endswith(".png"): 
        
        image_input_path = '/Users/nickbecker/Python_Projects/patent_project/D/references/patent_pngs/' + i[:-4] + '.png'
        image_out_path = '/Users/nickbecker/Python_Projects/patent_project/D/references/cropped_pngs/domestic_art/' + i[:-4] + '_cropped.png'
        
        im = Image.open(image_input_path)
        image_cropped = im.crop(dimensions)
        image_cropped.save(image_out_path)
        
        time.sleep(0.1)
        
        tesseract_out_path = '/Users/nickbecker/Python_Projects/patent_project/D/references/extracted_text/domestic_art/' + i[:-4] + '_text'
        tesseract_call = 'tesseract ' + image_out_path + ' ' + tesseract_out_path
        subprocess.call(tesseract_call, shell = True)
        
        count += 1
        if count >= limit:
            break
    else:
        continue



