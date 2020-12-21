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
m_time=m_time[10:,:]
m_time[m_time<0]=0.0

stim_pos=numpy.loadtxt("stim_pos.csv",delimiter=",")

border1=30
border2=60

plot_len=4000

filename=fname.rstrip(".csv")+".pdf"
pylab.figure(figsize=(4,3))
pylab.imshow(m_time[:plot_len,:].T, interpolation="none", aspect="auto", cmap="jet")
pylab.plot(stim_pos[:plot_len], "--", color="red", linewidth=1)
pylab.plot([0,plot_len],[border1,border1], "--", color="white")
pylab.plot([0,plot_len],[border2,border2], "--", color="white")
pylab.yticks([])
pylab.xlabel("Time")
pylab.ylabel("Location")
pylab.colorbar()
pylab.tight_layout()
pylab.savefig(filename)
pylab.close() 
