# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 12:15:19 2021

@author: erkol
"""
import re

def base_composition(seq,query_base):
    base_counter=0
    seq_len=len(seq)
    
    for index in range(0,seq_len):
        seq_base=seq[index]
        if seq_base==query_base:
            base_counter= base_counter+1
    
    return base_counter

##Given a DNA(A,C,T,G) sequence string, returns the GC content as a float
def GC_content(seq):
    g_cont=base_composition(seq,"G")
    c_cont=base_composition(seq,"C")
    seq_len=len(seq)
    gc=(g_cont+c_cont)/float(seq_len)
    
    return gc

sequences = dict()
f=open("rosalind.txt")
for line in f:
                # get ID from header and create new entry
    if line.startswith('>'):
        ini_id = line.replace('>', '').strip()
        sequences[ini_id] = ''
    else:
        # repl. all white-space chars and join seqs spanning multiple lines
        sequences[ini_id] += ''.join(line.split()).upper()
#print(sequences)
IDs=sequences.keys()
seqs=sequences.values()
ids=list(IDs)
sequence=list(seqs)
#print(ids)
#print(sequence)
s=[]

for i in range(0,len(sequence)):
    seqgc=GC_content(sequence[i])
    s.append(seqgc)
print(s)
gc=dict(zip(ids,s))
max_key=max(gc,key=gc.get)
all_values=gc.values()
max_value = max(all_values)
print(str(max_key)+"\n"+ str(max_value*100))
