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

#network simulation
N=10000
prob=0.1
eta=0.1
simlen=10000
gamma=0.6

period=500.0
a_arr=0.9*numpy.cos(2*numpy.pi*numpy.arange(simlen)/period)
numpy.savetxt("a_array.csv", a_arr, delimiter=",")
pylab.plot(a_arr)
pylab.xlabel("Time")
pylab.ylabel("a")
pylab.savefig("a_arr.svg")
pylab.close()

network=sim_net.sim_net(N,P,prob,W,gamma,normalize="asym")
m_log=network.simulate_single_changeparam(a_arr,eta,simlen,start_node=0)
numpy.savetxt("overlap.csv", m_log, delimiter=",")
