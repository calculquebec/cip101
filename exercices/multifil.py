import os
import time
from multiprocessing import Process

# Nombre de processus basé sur Slurm
NUM_PROCS = int(os.environ.get("SLURM_CPUS_PER_TASK", 1))

# Mémoire (> 1 Go)
MEMORY_GB = float(os.environ.get("MEMORY_GB", 1.2))
TOTAL_BYTES = int(MEMORY_GB * 1024**3)

# Travail CPU total (fixe)
TOTAL_ITERATIONS = 600_000_000

def worker(proc_id, iterations):
    # Allocation mémoire locale au processus
    data = bytearray(TOTAL_BYTES // NUM_PROCS)

    # Toucher la mémoire
    for i in range(0, len(data), 4096):
        data[i] = (data[i] + proc_id) % 256

    # Charge CPU
    x = 0
    for _ in range(iterations):
        x = (x * 1664525 + 1013904223) & 0xFFFFFFFF

if __name__ == "__main__":
    iterations_per_proc = TOTAL_ITERATIONS // NUM_PROCS

    t0 = time.time()

    procs = []
    for p in range(NUM_PROCS):
        proc = Process(
            target=worker,
            args=(p, iterations_per_proc)
        )
        proc.start()
        procs.append(proc)

    for proc in procs:
        proc.join()

    elapsed = time.time() - t0
    print(f"Temps total écoulé : {elapsed:.1f} s")
