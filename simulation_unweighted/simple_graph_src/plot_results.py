#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import networkx
import pickle
import sys

start_node=int(sys.argv[1])

G,pos=pickle.load(open("graph.pickle","rb"))
a_arr, m_hist, cor_hist=pickle.load(open("results.pickle","rb"))
e=numpy.loadtxt("eigenval.csv", delimiter=",")
v=numpy.loadtxt("eigenvec.csv", delimiter=",")
group_id=numpy.loadtxt("group_id.csv", delimiter=",")

sort_ind=numpy.argsort(group_id)

for i in range(5):
    plotlib.plot_color_network("laplacian"+str(i)+".svg",G,pos,v[:,i])

for a_ind in range(len(a_arr)):
    a=numpy.around(a_arr[a_ind],decimals=1)
    m=m_hist[a_ind]
    plotlib.plot_color_network("result"+str(a_ind).zfill(2)+".svg",G,pos,m[:,start_node],title=r"$\alpha$="+str(a))

    cor_activity=cor_hist[a_ind]
    cor_activity=cor_activity[:,sort_ind]
    cor_activity=cor_activity[sort_ind,:]
    plotlib.plot_pattern_cor("pattern_cor_"+str(a_ind).zfill(2)+".pdf", cor_activity,title=r"$\alpha$="+str(a))

