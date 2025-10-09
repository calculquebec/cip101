#!/bin/bash

#SBATCH --account=def-sponsor00
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=256M
#SBATCH --time=00:01:00

module load python/3.13.2

python --version
