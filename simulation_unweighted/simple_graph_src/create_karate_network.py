#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import networkx
import pickle

#karate network
G=networkx.karate_club_graph()
pos=plotlib.get_pos_spring(G)
plotlib.plot_network("network_structure.svg",G,pos)
plotlib.plot_network_label("network_label.svg",G,pos)
graph_dump=(G,pos)
pickle.dump(graph_dump, open("graph.pickle","wb"))

#group
group_id=numpy.zeros(G.number_of_nodes(),dtype=int)
for i in range(G.number_of_nodes()):
    if G.nodes[i]["club"]=="Mr. Hi":
        group_id[i]=0
    elif G.nodes[i]["club"]=="Officer":
        group_id[i]=1
    else:
        print("Warning: Unknown groupID.")
        group_id[i]=-1
numpy.savetxt("group_id.csv", group_id, delimiter=",")

#adjacency matrix
P=int(max(map(max,G.edges)))+1
W=numpy.zeros([P,P])
for x in G.edges:
    W[x[0],x[1]]=1.0
    W[x[1],x[0]]=1.0
numpy.savetxt("adjacency.csv", W, delimiter=",")

