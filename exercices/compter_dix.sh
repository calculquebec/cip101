#!/bin/bash

#SBATCH --time=00:10:00
#SBATCH --account=def-sponsor00

module load python/3.13.2
python compter_dix.py
