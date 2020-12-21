#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import networkx
import pickle

m_time=numpy.loadtxt(sys.argv[1], delimiter=",")
a_arr=numpy.loadtxt(sys.argv[2], delimiter=",")

P=m_time.shape[1]
Phalf=int(P//2)

Lgap=5
peak=numpy.argmax(m_time, axis=1)
vel=(peak-numpy.roll(peak,Lgap))
vel[vel<-Phalf]=vel[vel<-Phalf]+P
vel[vel>Phalf]=vel[vel>Phalf]-P
vel=vel/Lgap
vel[:Lgap]=0.0

vel_hi=numpy.mean(vel[a_arr>0.0])
vel_mid=numpy.mean(vel[(a_arr<0.0)*(a_arr>-0.8)])
vel_lo=numpy.mean(vel[(a_arr<-0.8)])

pylab.figure(figsize=(3,1.5))
pylab.barh([2,1,0], [vel_hi, vel_mid, vel_lo], tick_label=[r"$\alpha>0$", r"$-0.8<\alpha<0$", r"$\alpha<-0.8$"], color=["blue","green","red"])
pylab.xlabel("Speed (patterns/time-step)")
pylab.tight_layout()
pylab.savefig("speed.svg")
pylab.close()

for t in range(len(m_time)):
    m_time[t,:]=numpy.roll(m_time[t,:],Phalf-numpy.argmax(m_time[t,:]))

mean_hi=numpy.mean(m_time[a_arr>0,:], axis=0)
mean_mid=numpy.mean(m_time[(a_arr<0.0)*(a_arr>-0.8),:], axis=0)
mean_lo=numpy.mean(m_time[(a_arr<-0.8),:], axis=0)

x=numpy.arange(P)-Phalf
plot_width=20
ind=range(Phalf-plot_width,Phalf+plot_width+1)
pylab.figure(figsize=(2.5,2))
pylab.plot(x[ind],mean_hi[ind], label=r"$\alpha>0$", color="blue")
pylab.plot(x[ind],mean_mid[ind], label=r"$-0.8<\alpha<0$", color="green")
pylab.plot(x[ind],mean_lo[ind], label=r"$\alpha<-0.8$", color="red")
pylab.legend()
pylab.xlabel("Aligned pattern #")
pylab.ylabel("Mean overlap")
pylab.tight_layout()
pylab.savefig("mean_overlap.svg")
pylab.close()

