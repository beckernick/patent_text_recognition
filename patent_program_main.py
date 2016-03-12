# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:33:45 2016

@author: nickbecker
"""


import time
import subprocess



"""

This program takes the following steps to recreate this entire process:

1. Convert to PNG format
2. Crop image and run OCR
3. Assign prior art to patents and store in a dictionary
4. Assign priort art's dates to patents and store in a dictionary ***** (doesn't currently do this) ******
5. Filter prior art and prior art dates using regular expressions

It does this by executing programs that individually do the above steps.

"""


if __name__ == "__main__":
    subprocess.call('python /Users/nickbecker/Python_Projects/patent_project/P/convert_to_png.py', shell = True)
    time.sleep(1)

    subprocess.call('python /Users/nickbecker/Python_Projects/patent_project/P/crop_and_ocr_domestic_art_png_images.py', shell = True)
    time.sleep(1)
    
    #subprocess.call('python /Users/nickbecker/Python_Projects/patent_project/P/crop_and_ocr_domestic_dates_png_images.py', shell = True)
    #time.sleep(1)
    
    subprocess.call('python /Users/nickbecker/Python_Projects/patent_project/P/assign_prior_art_to_patents.py', shell = True)
    time.sleep(1)

    #subprocess.call('python /Users/nickbecker/Python_Projects/patent_project/P/assign_prior_art_dates_to_patents.py', shell = True)
    #time.sleep(1)
    
    subprocess.call('python /Users/nickbecker/Python_Projects/patent_project/P/patent_dictionary_filtering.py', shell = True)

    









