#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import networkx
import pickle
import sys
import PIL.Image

figsize=numpy.array(PIL.Image.open("resized.jpg")).shape[:2]
e=numpy.loadtxt("eigenval.csv", delimiter=",")
v=numpy.loadtxt("eigenvec.csv", delimiter=",")

for k in range(6):
    color_max=numpy.max(numpy.abs(v[:,k]))
    pylab.imshow(v[:,k].reshape(figsize), interpolation="none", cmap="bwr", vmax=color_max, vmin=-color_max)
    pylab.axis("off")
    pylab.colorbar()
    pylab.savefig("laplacian"+str(k)+".pdf")
    pylab.close()

a_arr, m_hist=pickle.load(open("results.pickle","rb"))

for a_ind in range(len(a_arr)):
    a=numpy.around(a_arr[a_ind],decimals=1)
    m=m_hist[a_ind]

    color_max=numpy.max(numpy.abs(m))
    pylab.imshow(m.reshape(figsize), interpolation="none", cmap="bwr", vmax=color_max, vmin=-color_max)
    pylab.axis("off")
    pylab.colorbar()
    pylab.title(r"$\alpha$="+str(a),fontsize=20)
    pylab.savefig("result"+str(a_ind).zfill(2)+".pdf")
    pylab.close()
