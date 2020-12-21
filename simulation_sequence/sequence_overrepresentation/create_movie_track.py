#!/usr/bin/env python3

import sys
import numpy
import pylab
import networkx
import pickle

#overlap
m_log=numpy.loadtxt(sys.argv[1], delimiter=",")
datalen=m_log.shape[0]

m_max=numpy.max(m_log)
m_min=numpy.min(m_log)

plot_pitch=10

#plot
count=0
for t in range(datalen):
    if t%plot_pitch==0:
        m=m_log[t,:]
        pylab.figure(figsize=(6,3))
        x=range(1,len(m)+1)
        pylab.plot(x,m)
        pylab.plot(x,[0]*len(m),color="black")
        pylab.xlim([1,len(m)])
        pylab.ylim([m_min,m_max])
        pylab.ylabel("Overlap")
        pylab.xlabel("Patterns")
        pylab.title("t="+str(t), fontsize=20)
        pylab.tight_layout()
        pylab.savefig("img"+str(count).zfill(4)+".png")
        pylab.close()
        count=count+1

#movie
import os 
os.system("ffmpeg -r 20 -i img%04d.png -vsync cfr movie.avi")
os.system("rm img*.png")
