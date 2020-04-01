#!/anaconda3/bin/python

# Python 3.6
# >ls *.txt | sed 's/^/\.\/SEStxt2xy.py /' > exportxy.sh
# >source exportxy.sh

import os
import re
import sys
from collections import Counter

#if sys.argv < 2:
#    print('To few arguments, please specify a filename')

#strip .txt
FILE_NAME= os.path.splitext(sys.argv[1])[0]

INPUT_FILE=FILE_NAME+'.txt'
#print(INPUT_FILE)

with open(INPUT_FILE,'r') as g:
    region_counts = Counter(g.read().split())

g.close()

#xmax=0
xmax=(region_counts.get('[Data'))
#print(xmax)


for x in range(1,xmax+1):
    with open(INPUT_FILE, 'r') as f:
        for i in re.split(r'\n\n+', f.read()):
                REGION_NUM="%d" % x
                SECT_NAME='[Data ' + REGION_NUM + ']'
                if i.startswith(SECT_NAME):
                    string=i

        string=string.split("\n", 1)[1]
        f.close()
        OUTPUT_FILE = FILE_NAME+'_'+ REGION_NUM+'.xy'
                #print(INPUT_FILE)
        print(OUTPUT_FILE)
        with open(OUTPUT_FILE, 'w') as text_file:
            print(string, file = text_file)
            text_file.close()

