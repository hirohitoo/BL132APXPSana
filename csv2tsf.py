#! /usr/bin/env python3
# Python needs to be >3.5
# This script converts .csv files with header to .tsf files without header for CasaXPS

replacements = [(b',', b'\t')]
globpath = './*_SUM.csv'

import os
import glob

for filepath in glob.iglob(globpath, recursive=True):
    with open(filepath, 'rb') as file:
        s = file.read()
        #s = file.readlines()[1:]
    #s2 = s.split(b’\n’, 1)[1]   
    for f, r in replacements:
        s = s.replace(f, r)
    dest_filepath=os.path.splitext(filepath)[0]+'.tsf3'
    with open(dest_filepath, "wb") as file:  
        s = s.split(b'\n', 1)[1]
        file.write(s)
