import numpy as np
from time import perf_counter

N = 3

A = np.random.rand(N,N)
B = np.random.rand(N,N)

t1 = perf_counter()
C = A@B        # Multiplicacion de matrices
			   
t2 = perf_counter()

dt = t2 - t1

print(f"Tiempo transcurrido = {dt} s")
