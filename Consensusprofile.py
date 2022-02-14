# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:58:54 2022

@author: erkol
"""

import re
import numpy as np
sequences = dict()
f=open("fasta1.txt") 
for line in f:
                # get uniprot ID from header and create new entry
    if line.startswith('>'):
        uniprot_id = line.replace('>', '').strip()
        sequences[uniprot_id] = ''
    else:
        # repl. all white-space chars and join seqs spanning multiple lines
        sequences[uniprot_id] += ''.join(line.split()).upper()
#print(sequences)
IDs=sequences.keys()
seqs=sequences.values()
ids=list(IDs)
sequence=list(seqs)
#print(ids)
#print(sequence)
a=[]
for i in range(0,len(sequence)):
    b=list(sequence[i])
    a.append(b)
#print(a)

mat= np.array(a)
#print(mat)


countA = np.count_nonzero(mat == "A", axis=0)
countC=np.count_nonzero(mat == "C", axis=0)
countG=np.count_nonzero(mat == "G", axis=0)
countT=np.count_nonzero(mat == "T", axis=0)
count=(countA,countC,countG,countT)
counts = np. vstack(count)
maximum=counts.max(axis=0)

cons=[None]*len(countA)

for i in range(0, len(countA)):
    if countA[i]>=countC[i]:
        if countA[i]>=countG[i]:
            if countA[i]>=countT[i]:
                cons[i]='A'
    if countC[i]>=countA[i]:
        if countC[i]>=countG[i]:
            if countC[i]>=countT[i]:
                cons[i]="C"
    if countG[i]>=countA[i]:
        if countG[i]>=countC[i]:
            if countG[i]>=countT[i]:
                cons[i]="G"
    if countT[i]>=countA[i]:
        if countT[i]>=countC[i]:
            if countT[i]>=countG[i]:
                cons[i]="T"
                
  
rejoined="".join(cons).strip('[]').replace('[]','\t').replace(',','\t').replace('[]','\t')
print(rejoined)
    
    

#print(maximum)

print("A:" ,*countA)
print("C:" ,*countC)
print("G:" ,*countG)
print("T:" ,*countT)





