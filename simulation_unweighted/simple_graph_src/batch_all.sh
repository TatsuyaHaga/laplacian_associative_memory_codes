#!/bin/bash

cd ../

for NETWORK in pentagon karate room 
do
    for NORM in sym asym
    do
        DIR=${NETWORK}_${NORM}
        cp -r simple_graph_src ${DIR}
        cd ${DIR}
        bash batch_${NETWORK}.sh ${NORM}
        #sbatch -p compute -c 40 -t 24:00:00 batch_${NETWORK}.sh ${NORM}
        cd ../
        sleep 10s
    done
done
