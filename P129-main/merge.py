## START IF CODE ##

import csv
import pandas as pd

file1='bright_stars.csv'
file2='dwarf_stars.csv'

d1=[]
d2=[]

with open (file1,'r',encoding='utf-8') as f:
    csvreader=csv.reader(f)

    for i in csvreader:
        d1.append(i)

with open (file2,'r',encoding='utf-8') as f:
    csvreader=csv.reader(f)

    for i in csvreader:
        d2.append(i)    

h1=d1[0]
h2=d2[0]

p_d1=d1[1:]
p_d2=d2[1:]

h=h1+h2

p_d=[]

for i in p_d1:
    p_d.append(i)
for j in p_d2:
    p_d.append(j)
    
with open ("Brightest_stars.csv",'w',encoding='utf-8')as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(p_d)

df=pd.read_csv ("Brightest_stars.csv")
df.tail(8)
## END OF CODE ##

## ERRORS ##

##    File "c:\Users\danie\Desktop\P129\merge.py", line 12, in <module>
##     with open ('file1','r',encoding='utf-8') as f:
## FileNotFoundError: [Errno 2] No such file or directory: 'file1'