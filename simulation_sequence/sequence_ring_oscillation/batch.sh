#!/bin/bash

python create_network_ring.py
python sim.py adjacency.csv
python plot_overlap_param.py overlap.csv a_array.csv
python plot_stat.py overlap.csv a_array.csv
python create_movie_track.py overlap.csv
