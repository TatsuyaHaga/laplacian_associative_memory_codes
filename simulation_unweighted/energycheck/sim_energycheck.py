#!/usr/bin/env python3

import sys
sys.path.append("../")
import sim_net

import numpy
import pylab
import pickle
import sys

#adjacency matrix
W=numpy.loadtxt(sys.argv[1], delimiter=",")
P=W.shape[0]
start_node=int(sys.argv[2])
normalize="sym"

#network simulation
N=10000
prob=0.1
eta=0.01
simlen=3000
gamma=0.3
a_arr=[-0.8, -0.5, 0.0, 0.5, 1.0, 2.0]#numpy.arange(-1.5,3.1,0.1)

a_hist=[]
m_hist=[]
obj_hist=numpy.zeros([len(a_arr),simlen])

network=sim_net.sim_net(N,P,prob,W,gamma,normalize)

for a_ind in range(len(a_arr)):
    a=numpy.around(a_arr[a_ind],decimals=1)
    print(a)
    m_log,obj_log=network.simulate_single(a,eta,simlen,start_node)
    m=m_log[-1,:]

    a_hist.append(a)
    m_hist.append(m)
    save=(a_hist,m_hist)
    pickle.dump(save, open("results.pickle","wb"))
    obj_hist[a_ind,:]=obj_log
    numpy.savetxt("objfunc.csv", obj_hist, delimiter=",")
