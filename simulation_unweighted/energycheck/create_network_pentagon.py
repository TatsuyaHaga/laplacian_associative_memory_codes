#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import itertools
import networkx
import pickle

N=15
group_id=numpy.zeros(N,dtype=int)
group_id[:5]=0
group_id[5:10]=1
group_id[10:15]=2

#set position
rotmat=numpy.array([[numpy.cos(2.0*numpy.pi/5.0), numpy.sin(2.0*numpy.pi/5.0)],[-numpy.sin(2.0*numpy.pi/5.0),numpy.cos(2.0*numpy.pi/5.0)]])
vec=numpy.array([0,10])
pos_penta=numpy.vstack([rotmat.T@rotmat.T@vec, rotmat.T@vec, vec, rotmat@vec, rotmat@rotmat@vec]).T
rotmat=rotmat@rotmat
offset1=numpy.array([15,-25]).reshape((2,1))
offset2=numpy.array([-15,-25]).reshape((2,1))
pos=list(numpy.hstack([pos_penta, rotmat@pos_penta+offset1, rotmat.T@pos_penta+offset2]).T)

#set edges
edge_list=list(itertools.combinations(range(5),2))+list(itertools.combinations(range(5,10),2))+list(itertools.combinations(range(10,15),2))
edge_list.remove((0,4))
edge_list.remove((5,9))
edge_list.remove((10,14))
edge_list.append((4,5))
edge_list.append((9,10))
edge_list.append((0,14))

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
