# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 14:02:49 2021

@author: erkol
"""

initial=1
n=31
k=4
s=n+1
mature=[None]*s 
litter=[None]*s
newmature=[None]*s
t=[]
for i in range(1,n+1):
    if i<=2:
       litter[i]=0
       mature[i]=0
       newmature[i]=1
    elif i>2:
        mature[i]=newmature[i-1]+mature[i-1]
        mature.append(mature[i])
        litter[i]=int(mature[i])*k
        litter.append(litter[i])
        newmature[i]=litter[i-1]
        newmature.append(newmature[i])
total=mature[i]+litter[i]+newmature[i]   
print(total)
    