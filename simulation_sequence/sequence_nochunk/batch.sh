#!/bin/bash

python create_network_ring.py
python sim.py adjacency.csv
for FILE in overlap*.csv
do
    python plot_overlap.py $FILE
    python plot_overlap_eachpos.py $FILE stim_pos.csv
done
python plot_overlap_eachpos_mean.py
