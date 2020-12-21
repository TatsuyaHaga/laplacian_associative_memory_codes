#!/bin/bash

date
python create_network_pentagon.py
python graph_laplacian.py adjacency.csv
python sim.py adjacency.csv $1
python plot_results.py 1
python plot_stat.py
python plot_explainedvar.py
date
