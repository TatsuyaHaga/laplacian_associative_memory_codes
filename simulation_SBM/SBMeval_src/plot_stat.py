#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import networkx
import pickle
import sys

a_arr, m_hist, cor_hist=pickle.load(open("results.pickle","rb"))
Na=len(a_arr)

max_overlap=numpy.zeros(Na)
Nactive=numpy.zeros(Na)
for a_ind in range(Na):
    m=m_hist[a_ind]
    max_m=numpy.max(m,axis=0,keepdims=True)
    max_overlap[a_ind]=numpy.mean(max_m)
    Nactive[a_ind]=numpy.mean(numpy.sum((m>0.5*max_m)*(m>0.05),axis=0))
    #Nactive[a_ind]=numpy.mean(numpy.sum((m>0.05),axis=0))

xlim=[numpy.min(a_arr),numpy.max(a_arr)]
xticks=[-1,0,1,2]
pylab.figure(figsize=(4,2))
pylab.subplot(1,2,1)
pylab.plot(a_arr, max_overlap)
pylab.xlim(xlim)
pylab.xticks(xticks)
pylab.xlabel(r"$\alpha$")
pylab.ylabel("Maximum overlap")

pylab.subplot(1,2,2)
pylab.plot(a_arr, Nactive)
pylab.xlim(xlim)
pylab.xticks(xticks)
pylab.xlabel(r"$\alpha$")
pylab.ylabel("Number of\nactive patterns")
pylab.tight_layout()
pylab.savefig("overlap_stat.svg")
