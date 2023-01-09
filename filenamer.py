#! /usr/bin/env python3
# Python needs to be >3.5
# This script converts .csv files with header to .tsf files without header for CasaXPS

replacements = [('2022','1000')]
globpath = './*_SUM.csv'

import os
import glob
import shutil

#import csv
#with open('nametable.csv', newline='') as f0:
#    reader = csv.reader(f0)
#    replacements = list(reader)
#print(replacements)

for filepath in glob.iglob(globpath, recursive=True):
    # Read CSV file into DataFrame df
    #df = pd.read_csv(filepath, index_col=0)  
    for f, r in replacements:
        #s = s.replace(f, r)
        #print(list(df.columns)[0])
        #if f in list(df.columns)[0]: df.index=float(r)-df.index
        org_filepath='./'+f+'.csv'        
        new_filepath='./'+r+'.csv'
        shutil.copy2(org_filepath,new_filepath) 
   # Write Dataframe df into CSV file
    #df.to_csv(dest_filepath, sep=',',header='true')
