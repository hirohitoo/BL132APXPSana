#! /usr/bin/env python3
# Python needs to be >3.5
# This script converts .csv files with header to .tsf files without header for CasaXPS

replacements = [('2022','1000')]
globpath = './*_SUM.csv'

import os
import glob
import pandas as pd

#import csv
#with open('vbedge.csv', newline='') as f0:
#    reader = csv.reader(f0)
#    replacements = list(reader)
#print(replacements)

for filepath in glob.iglob(globpath, recursive=True):
    # Read CSV file into DataFrame df
    df = pd.read_csv(filepath, index_col=0)  
    for f, r in replacements:
        #s = s.replace(f, r)
        print(list(df.columns)[0])
        if f in list(df.columns)[0]: df[df.index]=df[df.index]-float(r)
            
    dest_filepath=os.path.splitext(filepath)[0]+'_BE.csv'
   # Write Dataframe df into CSV file
    df.to_csv(dest_filepath, sep=',',header='true')

