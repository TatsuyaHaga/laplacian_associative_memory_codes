#!/usr/bin/env python3

import numpy
import pylab
import pickle

a_arr, m_hist=pickle.load(open("results.pickle","rb"))
e=numpy.loadtxt("eigenval.csv", delimiter=",")
v=numpy.loadtxt("eigenvec.csv", delimiter=",")

a_ind_pick=[7,10,15,20,25,35]
a_arr=[a_arr[i] for i in a_ind_pick]
m_hist=[m_hist[i] for i in a_ind_pick]

p=100#v.shape[1]
Rsquare=numpy.zeros([len(a_arr),p])
#explained variance between gl and attractor
for a_ind in range(len(a_arr)):
    var=numpy.var(m_hist[a_ind])
    for i in range(p):
        coef,res,rank,sing=numpy.linalg.lstsq(v[:,:i+1],m_hist[a_ind],rcond=None)
        Rsquare[a_ind,i]=1-numpy.mean(res)/v.shape[0]/var

#plot similarity between overlap and bases
cm=pylab.get_cmap("cool")
pylab.figure(figsize=(3,3))
for i in range(len(a_arr)):
    pylab.plot(Rsquare[i,:],".-",label=str(a_arr[i]),color=cm(i/len(a_arr)))
pylab.ylim([0,1])
pylab.xlim([0,p])
pylab.xlabel("The number of GL eigenvectors")
pylab.ylabel("Explained variance ratio")
pylab.legend()
pylab.tight_layout()
pylab.savefig("explained_variance.pdf")
pylab.close() 
