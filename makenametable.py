#! /usr/bin/env python3
# Python needs to be >3.5
# This script make a table, which is referenced to convert KE to BE

globpath = './*_SUM.csv'

import os
import glob
import pandas as pd

file_list=[]
vbedge_list=[]
fkey_list=[]

file_list=(glob.glob(globpath, recursive=True))


for f in file_list:
    vbedge_list.append(0)
    fkey_list.append(os.path.basename(f))
df2=pd.DataFrame({'FILEkey':fkey_list,'VBedge':vbedge_list})
dest_filepath='VBedgetable.csv'
#Write Dataframe df into CSV file
df2.to_csv(dest_filepath, sep=',',header='true',index=False)
