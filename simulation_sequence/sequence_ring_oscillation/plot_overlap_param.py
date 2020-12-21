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
a_arr=numpy.loadtxt(sys.argv[2], delimiter=",")

P=m_time.shape[1]
Lgap=1
peak=numpy.argmax(m_time, axis=1)
vel=(peak-numpy.roll(peak,Lgap))
vel[vel<-1]=vel[vel<-1]+P
vel=vel/Lgap
vel[:Lgap]=0.0

Nactive=numpy.sum(m_time>0.01, axis=1)

plot_len=3000
m_time=m_time[:plot_len,:]
m_time[m_time<0]=0.0

#plotlib.plot_overlap_withparam(fname.rstrip(".csv")+".pdf",m_time,a_arr)
filename=fname.rstrip(".csv")+".pdf"
pylab.figure(figsize=(3,3))
pylab.subplot2grid((3,1),(0,0),rowspan=1)
pylab.plot(a_arr[:plot_len])
pylab.xlim([0,plot_len-1])
pylab.xticks([])
pylab.ylabel(r"$\alpha$")
pylab.subplot2grid((3,1),(1,0),rowspan=2)
pylab.imshow(m_time.T, interpolation="none", aspect="auto", cmap="jet")
pylab.xlabel("Time")
pylab.ylabel("Pattern")
#pylab.colorbar()
pylab.tight_layout()
pylab.savefig(filename)
pylab.colorbar()
pylab.tight_layout()
pylab.savefig("colorbar_"+filename)
pylab.close() 
