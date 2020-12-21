#!/usr/bin/env python3

import sys
sys.path.append("../")
import sim_net

import numpy
import pylab
import pickle
import sys
import PIL.Image

#adjacency matrix
W=numpy.loadtxt(sys.argv[1], delimiter=",")
P=W.shape[0]

#image size
figsize=numpy.array(PIL.Image.open(sys.argv[2])).shape[:2]

#normalization mode
normalize=sys.argv[3]

#network simulation
N=30000
prob=0.1
eta=0.01
simlen=3000
gamma=0.6
a_arr=numpy.arange(-1.5,3.1,0.1)

start_node=int(int(figsize[0]/2)*figsize[1]+int(figsize[1]/2))

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

    #numpy.savetxt("overlap_time.csv", m_log[:,start_node], delimiter=",")

    obj_hist[a_ind,:]=obj_log
    numpy.savetxt("objfunc.csv", obj_hist, delimiter=",")
