#! /usr/bin/env python3
# Python needs to be >3.5
# This script converts .csv files with header to .tsf files without header for CasaXPS

replacements = [(b'2022', b'1000')]
globpath = './*_SUM.csv'

import os
import glob
import pandas as pd

for filepath in glob.iglob(globpath, recursive=True):
    # Read CSV file into DataFrame df
    df = pd.read_csv('sample.csv', index_col=0)  
    for f, r in replacements:
        #s = s.replace(f, r)
        print(list(df.columns)[0])
        if f in list(df.columns)[0]:
            df.columns[0]=df.columns[0]-r
            
        #    convert x.val to vbedge-x.val
    dest_filepath=os.path.splitext(filepath)[0]+'_BE.csv'
   # Write Dataframe df into CSV file
    df.to_csv(dest_filepath, sep=',',header='true')
    #with open(dest_filepath, "wb") as file:  
    #    #s = s.split(b'\n', 1)[1]
    #    file.write(s)
