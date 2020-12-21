#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import itertools
import networkx
import pickle

N=100
group_id=numpy.zeros(N)
group=[[],[],[],[]]

#node position
pos={}
for i in range(N):
    pos[i]=[int(i%10), int(i//10)]

xcut=6
ycut=4

for x in range(0,xcut):
    for y in range(0,ycut):
        group[0].append(x+10*y)
        group_id[x+10*y]=0

for x in range(0,xcut):
    for y in range(ycut,10):
        group[1].append(x+10*y)
        group_id[x+10*y]=1

for x in range(xcut,10):
    for y in range(ycut,10):
        group[2].append(x+10*y)
        group_id[x+10*y]=2

for x in range(xcut,10):
    for y in range(0,ycut):
        group[3].append(x+10*y)
        group_id[x+10*y]=3

edge_list=[]
for i in range(len(group)):
    for j,k in itertools.combinations(group[i],2):
        xdif=numpy.abs(j%10-k%10)
        ydif=numpy.abs(j//10-k//10)
        if xdif<=1 and ydif<=1:
            edge_list.append([j,k])

for x1,y1,x2,y2 in [[2,ycut-1,2,ycut], [3,ycut-1,3,ycut], [2,ycut-1,3,ycut], [3,ycut-1,2,ycut], [xcut-1,8,xcut,8], [7,ycut-1,7,ycut], [8,ycut-1,8,ycut], [7,ycut-1,8,ycut], [8,ycut-1,7,ycut], [xcut-1,1,xcut,1]]:
    edge_list.append([x1+10*y1,x2+10*y2])

map(tuple, edge_list)

#Adjacency matrix
W=numpy.zeros([N,N])
for x in edge_list:
    W[x[0],x[1]]=1.0
    W[x[1],x[0]]=1.0

numpy.savetxt("edgelist.csv", numpy.array(edge_list), delimiter=",", fmt="%d")
numpy.savetxt("group_id.csv", group_id, delimiter=",", fmt="%d")
numpy.savetxt("adjacency.csv", W, delimiter=",")

G=networkx.Graph()
G.add_edges_from(edge_list)
plotlib.plot_network("network_structure.svg",G,pos)
plotlib.plot_network_label("network_label.svg",G,pos)

graph_dump=(G,pos)
pickle.dump(graph_dump, open("graph.pickle","wb"))
