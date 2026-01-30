#!/bin/bash
#SBATCH --account=def-sponsor00
#SBATCH --cpus-per-task=2
#SBATCH --mem=2G
#SBATCH --time=00:05:00

module load python/3.13.2

export MEMORY_GB=1.2

srun python multifil.py
