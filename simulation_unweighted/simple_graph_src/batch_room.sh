#!/bin/bash

date
python create_network_room.py
python graph_laplacian.py adjacency.csv
python sim.py adjacency.csv $1
python plot_results.py 2
python plot_stat.py
python plot_explainedvar.py
python plot_subgoal.py
date
