#!/usr/bin/env python3

import numpy
import pylab
import pickle
import itertools

a_arr, m_hist, cor_hist=pickle.load(open("results.pickle","rb"))
e=numpy.loadtxt("eigenval.csv", delimiter=",")
v=numpy.loadtxt("eigenvec.csv", delimiter=",")
v = v @ numpy.diag(e)

group_ans = numpy.loadtxt("group_hier.csv", delimiter=",", dtype=int)
if group_ans.ndim==1:
    group_ans = group_ans.reshape([len(group_ans),1])
N, Nhier = group_ans.shape
Nsep = numpy.max(group_ans)+1

#representational similarity within communities
def calc_matching(cor, hierarchy):
    sumplus = 0.0
    Nplus = 0
    for j,k in itertools.combinations(list(range(N)),2):
        if hierarchy==0 or numpy.all(group_ans[j,:hierarchy]==group_ans[k,:hierarchy]):
            if (hierarchy==Nhier) or (hierarchy<Nhier and group_ans[j,hierarchy]!=group_ans[k,hierarchy]):
                sumplus += cor[j,k]
                Nplus += 1
    return sumplus/Nplus

def calc_matching_all(cor):
    sumplus = 0.0
    Nplus = 0
    for j,k in itertools.combinations(list(range(N)),2):
        sumplus += cor[j,k]
        Nplus += 1
    return sumplus/Nplus

#LAM
matching_LAM=numpy.zeros([len(a_arr),Nhier+1])
for a_ind in range(len(a_arr)):
    matching_LAM[a_ind,0] = calc_matching_all(cor_hist[a_ind])
    for h in range(1,Nhier+1):
        matching_LAM[a_ind,h] = calc_matching(cor_hist[a_ind], h)
#GL
p=numpy.min([50, v.shape[1]-1])
matching_GL=numpy.zeros([p,Nhier+1])
for i in range(p):
    matching_GL[a_ind,0] = calc_matching_all(numpy.corrcoef(v[:,:i+2]))
    for h in range(1,Nhier+1):
        matching_GL[i,h] = calc_matching(numpy.corrcoef(v[:,:i+2]), h)

#plot
colors = ["gray", "red", "blue", "green"]
pylab.figure(figsize=(2.5,2.5))
pylab.plot(a_arr, matching_LAM[:,0],".-",label="All pairs",color=colors[0])
for h in range(1,Nhier+1):
    pylab.plot(a_arr, matching_LAM[:,h],".-",label="Level "+str(h),color=colors[h])
pylab.xlim([-1,3])
pylab.xticks([-1,0,1,2])
pylab.xlabel(r"$\alpha$")
pylab.ylabel("Average pattern correlation")
pylab.tight_layout()
pylab.savefig("cor_cluster_LAM_nolegend.pdf")
pylab.legend()
pylab.savefig("cor_cluster_LAM.pdf")
pylab.close() 

pylab.figure(figsize=(2.5,2.5))
pylab.plot(range(2,p+2), matching_GL[:,0],".-",label="All pairs",color=colors[0])
for h in range(1,Nhier+1):
    pylab.plot(range(2,p+2), matching_GL[:,h],".-",label="Level "+str(h),color=colors[h])
pylab.xlim([0,p+2])
pylab.xlabel("Dimension of representations")
pylab.ylabel("Average pattern correlation")
pylab.tight_layout()
pylab.savefig("cor_cluster_GL_nolegend.pdf")
pylab.legend()
pylab.savefig("cor_cluster_GL.pdf")
pylab.close() 
