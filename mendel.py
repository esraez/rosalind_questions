# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:36:48 2022

@author: erkol
"""
#given:Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
#returns:The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
k=20
m=29
n=21
prob_k=k/(k+m+n)
prob_m=m/(k+m+n)
prob_n=n/(k+m+n)

prob_kk=(k/(k+m+n))*((k-1)/(k+m+n-1))
prob_km=(k/(k+m+n))*(m/(k+m+n-1))
prob_kn=(k/(k+m+n))*(n/(k+m+n-1))
prob_mk=(m/(k+m+n))*(k/(k+m+n-1))
prob_mm=(m/(k+m+n))*((m-1)/(k+m+n-1))
prob_mn=(m/(k+m+n))*(n/(k+m+n-1))
prob_nk=(k/(k+m+n))*(n/(k+m+n-1))
prob_nm=(n/(k+m+n))*(m/(k+m+n-1))
prob_nn=(n/(k+m+n))*((n-1)/(k+m+n-1))

d_kk=1
d_mm=3/4
d_nn=0
d_mk=1
d_nk=1
d_nm=1/2

total_prob=(prob_kk*d_kk)+(prob_km*d_mk)+(prob_mk*d_mk)+(prob_kn*d_nk)+(prob_nk*d_nk)+(prob_mm*d_mm)+(prob_mn*d_nm)+(prob_nm*d_nm)+(prob_nn*d_nn)
print(total_prob)
                                            
