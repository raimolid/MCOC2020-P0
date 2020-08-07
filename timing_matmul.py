#!/usr/bin/env python
# coding: utf-8

# **Parte 1- Archivos de texto**

# In[ ]:


import numpy as np
from time import perf_counter


# In[ ]:


Ns=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]


# In[ ]:


Ncorridas=10


# In[ ]:


for i in range(Ncorridas):
    dts=[]
    mem=[]
    name=(f"matmul{i}.txt")
    fid=open(name,"w")
    
    for N in Ns:

        print(f"N = {N}")

        A=np.random.rand(N,N)
        B=np.random.rand(N,N)

        t1=perf_counter()
        C=A@B
        t2=perf_counter()

        dt=t2-t1

        size=3*(N**2)*8

        dts.append(dt)
        mem.append(size)

        fid.write(f"{N} {dt} {size}\n")

        #print(f"Tiempo transcurrido = {dt} s")
        #print(f"Memoria usada = {mem} bytes")

        fid.flush()


# In[ ]:


fid.close()

