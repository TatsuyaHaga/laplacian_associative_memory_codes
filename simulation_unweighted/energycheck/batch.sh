#!/bin/bash

python create_network_pentagon.py
python sim_energycheck.py adjacency.csv 1
python plot_obj.py
mkdir pentagon
mv *.csv *.pickle *.svg pentagon/

python create_network_karate.py
python sim_energycheck.py adjacency.csv 31
python plot_obj.py
mkdir karate 
mv *.csv *.pickle *.svg karate/

python create_network_room.py
python sim_energycheck.py adjacency.csv 1
python plot_obj.py
mkdir room
mv *.csv *.pickle *.svg room/
