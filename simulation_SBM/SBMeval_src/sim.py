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
normalize=sys.argv[2]

#network simulation
N=10000
prob=0.1
eta=0.01
simlen=3000
gamma=0.3
a_arr=numpy.arange(-1.5,3.1,0.1)

a_hist=[]
m_hist=[]
cor_hist=[]

network=sim_net.sim_net(N,P,prob,W,gamma,normalize)

for a_ind in range(len(a_arr)):
    a=numpy.around(a_arr[a_ind],decimals=1)
    print(a)
    m_log,cor_activity=network.simulate_allstarts(a,eta,simlen)
    m=m_log[-1,:,:]+0.0

    a_hist.append(a)
    m_hist.append(m)
    cor_hist.append(cor_activity)
    save=(a_hist,m_hist,cor_hist)
    pickle.dump(save, open("results.pickle","wb"))

    #numpy.savetxt("overlap_time.csv", m_log[:,:,1], delimiter=",")
