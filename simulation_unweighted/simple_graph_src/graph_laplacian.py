#!/usr/bin/env python3

import numpy
import scipy.linalg
import sys

W=numpy.loadtxt(sys.argv[1], delimiter=",")
P=W.shape[0]

#normalize
Dnorm=numpy.diag(numpy.sum(W,axis=1)**-1)
#laplacian
L=numpy.eye(P)-Dnorm@W
e,v=scipy.linalg.eig(L)
e=numpy.real(e)
v=numpy.real(v)
order=numpy.argsort(e)
e=e[order]
v=v[:,order]

numpy.savetxt("eigenval.csv", e, delimiter=",")
numpy.savetxt("eigenvec.csv", v, delimiter=",")
