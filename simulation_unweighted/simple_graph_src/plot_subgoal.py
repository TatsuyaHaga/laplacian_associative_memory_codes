#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import networkx
import pickle
import sys

G,pos=pickle.load(open("graph.pickle","rb"))
a_arr, m_hist, cor_hist=pickle.load(open("results.pickle","rb"))
e=numpy.loadtxt("eigenval.csv", delimiter=",")
v=numpy.loadtxt("eigenvec.csv", delimiter=",")
group_id=numpy.loadtxt("group_id.csv", delimiter=",")

sort_ind=numpy.argsort(group_id)

A=numpy.loadtxt("adjacency.csv",delimiter=",")
Dnorm=numpy.diag(numpy.sum(A,axis=1)**-1)
prob=Dnorm@A

P=v.shape[0]
for dim in range(1,5):
    x=v[:,1:dim+1]
    x=x/numpy.linalg.norm(x,axis=1,keepdims=True)
    r=numpy.zeros(P)
    for i in range(P):
        r[i]=numpy.sum(prob[i,:]*0.5*(1-numpy.sum(x*x[i:i+1,:],axis=1)))
    plotlib.plot_color_network_positive("subgoal_laplacian"+str(dim)+".svg",G,pos,r)

for a_ind in range(len(a_arr)):
    a=numpy.around(a_arr[a_ind],decimals=1)
    cor=cor_hist[a_ind]
    r=numpy.zeros(P)
    for i in range(P):
        r[i]=numpy.sum(prob[i,:]*0.5*(1-cor[i,:]))
    plotlib.plot_color_network_positive("subgoal_network"+str(a_ind).zfill(2)+".svg",G,pos,r,title=r"$\alpha$="+str(a))
