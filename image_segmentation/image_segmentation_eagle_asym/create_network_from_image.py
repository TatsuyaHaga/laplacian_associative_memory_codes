#!/usr/bin/env python3

import sys
import numpy
import itertools
import PIL.Image

#read & resize image
img=PIL.Image.open(sys.argv[1])
#img=0.298912*img[:,:,0]+0.586611*img[:,:,1]+0.114478*img[:,:,2] #mono
img=numpy.array(img, dtype=float)
figsize=img.shape[:2]
img=img/numpy.max(img)

#adjacency matrix
size_row=img.shape[0]
size_col=img.shape[1]
N=size_row*size_col

sigmaI=0.1
sigmaX=4.0
r=5

tmp=itertools.product(range(size_row),range(size_col))
combi_all=itertools.combinations(tmp,2)
combi=[x for x in combi_all if numpy.sqrt((x[0][0]-x[1][0])**2+(x[0][1]-x[1][1])**2)<r]

edgelist_w=[]
for x1,x2 in combi:
    n1=int(x1[0]*size_col+x1[1])
    n2=int(x2[0]*size_col+x2[1])
    simval=numpy.exp(-numpy.sum((img[x1[0],x1[1]]-img[x2[0],x2[1]])**2)/(sigmaI**2))*numpy.exp(-((x1[0]-x2[0])**2+(x1[1]-x2[1])**2)/(sigmaX**2))
    edgelist_w.append((n1,n2,simval))

#Adjacency matrix
W=numpy.zeros([N,N])
for x in edgelist_w:
    W[x[0],x[1]]=x[2]
    W[x[1],x[0]]=x[2]

print("Nnode=", N, "Nedge=", len(edgelist_w))
#numpy.savetxt("edgelist_weight.csv", edgelist_w, delimiter=",")

numpy.savetxt("adjacency.csv", W, delimiter=",")
