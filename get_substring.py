# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:20:04 2022

@author: erkol
"""

#given a string, and a substring returns a list of indices for the substrings
#for overlapping subseqs, set stepsize to 1
def get_substring(seq,subseq):
    index=0
    stepsize=1
    windowsize=len(subseq)
    s=[]
    t=list()
    if seq>subseq:
        while index<=len(seq)-windowsize:
            seqpiece=seq[index:index+windowsize]
            if seqpiece==subseq:
                result=index+1
                t.append(result)
                s.append(seqpiece)
                index=index+stepsize
            else:
                s.append(seqpiece)
                index=index+stepsize
            
    rejoined="".join(str(t)).strip('[]').replace('[]','\t').replace(',','\t').replace('[]','\t')
    print(rejoined)

    