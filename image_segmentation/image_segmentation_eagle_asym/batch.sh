#!/bin/bash

IMG=eagle-1753002_640.jpg

date
python resize_image_eagle.py $IMG
python create_network_from_image.py resized.jpg
python graph_laplacian.py adjacency.csv
python sim_image.py adjacency.csv resized.jpg asym
python plot_results_image.py 
python plot_stat_image.py
python plot_explainedvar_image.py
date
