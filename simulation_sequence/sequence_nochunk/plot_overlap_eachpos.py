#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import networkx
import pickle

fname=sys.argv[1]
m_time=numpy.loadtxt(fname, delimiter=",")
m_time[m_time<0]=0.0

pos=numpy.loadtxt(sys.argv[2], delimiter=",").astype(int)
Npos=m_time.shape[1]
m_pos=numpy.zeros([Npos,Npos])
for i in range(Npos):
    m_pos[i,:]=numpy.mean(m_time[pos==i,:], axis=0)

#border1=30
#border2=60

pylab.figure(figsize=(3,3))
pylab.imshow(m_pos.T, interpolation="none", cmap="jet")
#pylab.plot([0,Npos-1],[border1,border1], "--", color="white")
#pylab.plot([0,Npos-1],[border2,border2], "--", color="white")
#pylab.plot([border1,border1], [0,Npos-1],"--", color="white")
#pylab.plot([border2,border2], [0,Npos-1],"--", color="white")
pylab.xticks([])
pylab.yticks([])
pylab.xlabel("Actual location")
pylab.ylabel("Represented location")
pylab.colorbar()
pylab.tight_layout()
pylab.savefig(fname.rstrip(".csv")+"_eachpos.pdf")
pylab.close()

cor_m=numpy.corrcoef(m_pos)
pylab.figure(figsize=(3,3))
pylab.imshow(cor_m, interpolation="none", cmap="jet")
#pylab.plot([0,Npos-1],[border1,border1], "--", color="white", lw=1)
#pylab.plot([0,Npos-1],[border2,border2], "--", color="white", lw=1)
#pylab.plot([border1,border1], [0,Npos-1],"--", color="white", lw=1)
#pylab.plot([border2,border2], [0,Npos-1],"--", color="white", lw=1)
pylab.xticks([])
pylab.yticks([])
pylab.xlabel("Location")
pylab.ylabel("Location")
pylab.colorbar()
pylab.tight_layout()
pylab.savefig(fname.rstrip(".csv")+"_eachpos_cor.pdf")
pylab.close()
