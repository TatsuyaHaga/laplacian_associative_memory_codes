#!/bin/bash

for HIER in 2 3
do
    for SEP in 2 3
    do
        for NODE in 200 400
        do
            for TRIAL in 1 2
            do
            DIR=SBMeval_hier${HIER}_sep${SEP}_node${NODE}_trial${TRIAL}
            cp -r SBMeval_src ${DIR}
            cd ${DIR}
            bash batch.sh ${NODE} ${HIER} ${SEP}
            #sbatch -p compute -c 20 --mem=20G -t 48:00:00 batch.sh ${NODE} ${HIER} ${SEP}
            cd ../
            sleep 60s
            done
        done
    done
done
