# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:45:43 2022

@author: erkol
"""
# given two strings(s,t) of equal length, returns the hamming distance between the two strings#
def Hamming_distance(s,t):
    s=list(s)
    t=list(t)
    count=0
    if len(s)==len(t):
        for i in range(0,len(s)):
            if s[i]!=t[i]:
                count=count+1
        return count
                
            
    