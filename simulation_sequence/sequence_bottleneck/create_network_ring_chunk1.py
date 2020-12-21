#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import itertools
import networkx
import pickle

N=90
wbase=100
bias=10
group1=range(1,30)
group2=range(31,60)
group3=range(61,N)

pos={}
edge_list=[]
edge_list_now=[]

group_id=[]

#ring
for x in range(0,N):
    angle=2*numpy.pi*x/N
    pos[x]=[numpy.cos(angle),numpy.sin(angle)]
    group_id.append(x)
    if x>0:
        edge_list.append((x-1,x,wbase+bias))
        edge_list.append((x,x-1,wbase-bias))
        edge_list_now.append((x,x-1))
    else:
        edge_list.append((N-1,0,wbase+bias))
        edge_list.append((0,N-1,wbase-bias))
        edge_list_now.append((0,N-1))

count=N
x2=-1
x3=-1
rad2=1.1
rad3=0.9
#side (groups)
for x in range(0,N):
    if (x in group1) or (x in group2) or (x in group3):
        x2prev=x2
        x2=count
        count+=1
        group_id.append(x)
        angle=2*numpy.pi*x/N
        pos[x2]=[rad2*numpy.cos(angle),rad2*numpy.sin(angle)]
        edge_list.append((x2,x,wbase))
        edge_list.append((x,x2,wbase))
        edge_list_now.append((x,x2))
        x3prev=x3
        x3=count
        count+=1
        group_id.append(x)
        pos[x3]=[rad3*numpy.cos(angle),rad3*numpy.sin(angle)]
        edge_list.append((x3,x,wbase))
        edge_list.append((x,x3,wbase))
        edge_list_now.append((x,x3))
        if x!=group1[0] and x!=group2[0] and x!=group3[0]:
            edge_list.append((x2prev,x2,wbase+bias))
            edge_list.append((x2,x2prev,wbase-bias))
            edge_list.append((x2prev,x,wbase+bias))
            edge_list.append((x,x2prev,wbase-bias))
            edge_list.append((x-1,x2,wbase+bias))
            edge_list.append((x2,x-1,wbase-bias))
            edge_list_now.append((x2,x2prev))
            edge_list_now.append((x,x2prev))
            edge_list_now.append((x2,x-1))
            edge_list.append((x3prev,x3,wbase+bias))
            edge_list.append((x3,x3prev,wbase-bias))
            edge_list.append((x3prev,x,wbase+bias))
            edge_list.append((x,x3prev,wbase-bias))
            edge_list.append((x-1,x3,wbase+bias))
            edge_list.append((x3,x-1,wbase-bias))
            edge_list_now.append((x3,x3prev))
            edge_list_now.append((x,x3prev))
            edge_list_now.append((x3,x-1))

#Adjacency matrix
W=numpy.zeros([count,count])
for x in edge_list:
    W[x[0],x[1]]=x[2]

numpy.savetxt("adjacency.csv", W, delimiter=",")
numpy.savetxt("group_id.csv", group_id, delimiter=",")

G=networkx.Graph()
G.add_edges_from(edge_list_now)
plotlib.plot_network_sizefix("network_structure.svg",G,pos,(8,8))
plotlib.plot_network_label("network_label.svg",G,pos)

graph_dump=(G,pos)
pickle.dump(graph_dump, open("graph.pickle","wb"))
