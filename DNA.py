# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 09:59:01 2021

@author: erkol
"""

s = 'CGCATACTTGAAGACGAGTTGAACTAAAATATCATTATCTTTATGTTAGACAGCTCGCCCACACCTGTGAATAACATACCCTGACTCCGACGCATCAGGCACGATGGTTTCGCGGAGGGTCGATCAGGAACAAAATCGGAATGAACGTGAGCATCGATCTGATAGCTGCGCTCGAACCTGACAGACGATATTTCAGTCAGTCGTCCTCTGAACCCCTGAGACGGAATATAATCTGCTTGTGACTTGTTAGTCTTCTTCGGACCATCTAGCTTTAAAACGCCCGGAGTAGTGCTAGAATTCTCCCTGGTGGTAATTTATTGTAATACTTGAAATGTAGTATAAGAACCACATCGGCGGAGAACTTATCCGCCCCATCTGAATGGTACTAAGTGCGCTCGGCCTCTGGGTATCAAGGTTAAATGTCTCTCGATGGGCGAGAATAAAGTCACATACTAGGATGGGGTGACGATCATTCCCAGATCTTATATATAACAGACACTGCATGCTAATGTACTAGCTATTCCTATTACACTGGGCGAAGTGACTCCGCCGGGATATGTTCCGTCCACTAATTATCAACTAACAGTTAAACTCGGTATCTTCAGCAGGTTAACAATTAGGTTATCTTACCGAAGTATACTATCTTTAGATTATAGAAGTCCGGTAGGACACAGGATTATATCTAGCCGATGACACATTCTGAACGTAGCCGAAACCTTAGATAGTAGAGAAGGGACTTCCTCTTGGTAAGCTCTTTAATCACACGCCACACCCTATAGACACTCCATATGCTAGTGTAGGTCCTAGGAAAGGGGGGCTAGGGAGGCCGCTTCTCCAATGTAGCTCTAGAGGGTGTTTTGAGCATCGATGGGGTAGAACGCGGAGGCGACACAGAACGCTCAGATCTGGCTCATTGGAAACTCATTGTTGAGC'

if len(s) <= 1000:
    numA=s.count('A')
    numC=s.count('C')
    numG=s.count('G')
    numT=s.count('T')
    print (numA, numC, numG, numT)

  