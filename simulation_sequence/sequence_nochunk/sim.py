#!/usr/bin/env python3

import sys
sys.path.append("../")
import sim_net

import numpy
import pylab
import pickle
import sys

#adjacency matrix
W=numpy.loadtxt(sys.argv[1], delimiter=",").T
P=W.shape[0]

group_id=numpy.loadtxt("group_id.csv", delimiter=",")

#network simulation
N=10000
prob=0.1
eta=0.1
simlen=30000
gamma=0.6

Nsim=3

Pring=90

a=-0.9

time=numpy.arange(simlen)
stim_amp=0.3*((time%150)<50)
stim_pos=numpy.zeros(simlen,dtype=numpy.int)
pos=0.0
speed_max=0.04
speed_min=0.02
prob_speed=0.001
speed=(speed_max-speed_min)*numpy.random.rand()+speed_min
for t in time:
    stim_pos[t]=int(pos)
    pos+=speed
    pos=pos%Pring
    if numpy.random.rand()<prob_speed:
        speed=(speed_max-speed_min)*numpy.random.rand()+speed_min

network=sim_net.sim_net(N,P,prob,W,gamma,normalize="asym")

for s in range(Nsim):
    print(s)
    network.initialize(N,P,prob,W,gamma,normalize="asym")
    m_log=network.simulate_single_stim(a,eta,simlen,start_node=0,stim_pos=stim_pos,stim_amp=stim_amp)

    m_out=numpy.zeros([simlen,Pring])
    for i in range(Pring):
        m_out[:,i]=numpy.mean(m_log[:,group_id==i],axis=1)
    numpy.savetxt("overlap_"+str(s)+".csv", m_out, delimiter=",")

numpy.savetxt("stim_pos.csv", stim_pos, delimiter=",")
numpy.savetxt("stim_amp.csv", stim_amp, delimiter=",")
