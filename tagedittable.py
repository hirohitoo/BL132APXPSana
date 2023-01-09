#! /usr/bin/env python3
# Python needs to be >3.5
# This script make a table, which is referenced to convert KE to BE

globpath = './*_SUM.csv'

import os
import glob
import pandas as pd

file_list=[]
fname_list=[]
fkey_list=[]

file_list=(glob.glob(globpath, recursive=True))

for f in file_list:
    fname_list.append(os.path.splitext(os.path.basename(f))[0])
    fkey_list.append(os.path.splitext(os.path.basename(f))[0])
    
df2=pd.DataFrame({'OrgName':fkey_list,'NewName':fname_list})
dest_filepath='nametable.csv'
#Write Dataframe df into CSV file
df2.to_csv(dest_filepath, sep=',',header='true',index=False)


#filename,target_tag,value
