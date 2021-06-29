#!/bin/bash

#1:Nnode 2:Nhierarchy 3:Nseparation
date
python create_network_SBM.py $1 $2 $3
python graph_laplacian.py adjacency.csv
python sim.py adjacency.csv asym
python plot_results.py 0
python plot_stat.py
python plot_explainedvar.py
python plot_correlation_cluster.py
date
