#!/bin/bash

date
python create_karate_network.py
python graph_laplacian.py adjacency.csv
python sim.py adjacency.csv $1
python plot_results.py 31
python plot_stat.py
python plot_explainedvar.py
date
