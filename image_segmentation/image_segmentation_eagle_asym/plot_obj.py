#!/usr/bin/env python3

import sys
sys.path.append("../")
import plotlib

import numpy
import pylab
import pickle
import sys

a_arr, m_hist=pickle.load(open("results.pickle","rb"))
obj_hist=numpy.loadtxt("objfunc.csv", delimiter=",")

a_ind_pick=[7,10,15,20,25,35]
a_arr=[a_arr[i] for i in a_ind_pick]
obj_hist=[obj_hist[i] for i in a_ind_pick]
pylab.close()
for a_ind in range(len(a_arr)):
    a=numpy.around(a_arr[a_ind],decimals=1)
    pylab.plot(obj_hist[a_ind], label=str(a_arr[a_ind]))

pylab.xlabel("Time step")
pylab.ylabel("Energy")
pylab.legend()
#pylab.tight_layout()
pylab.savefig("objfunc.svg")
