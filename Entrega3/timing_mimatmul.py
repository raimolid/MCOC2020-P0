import numpy as np
from mimatmul import mimatmul
from time import perf_counter
import matplotlib.pyplot as plt

#NUMERO DE CORRIDAS 
Ncorridas=10

#TAMAÑO DE MATRICES A PROBAR PARA CADA CORRIDA
Ns=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,
    200,250,350,500]#,600,800,1000,2000,5000,10000]

#CREANDO ARCHIVOS DE TEXTO PARA CADA CORRIDA
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
        C=mimatmul(A,B)
        t2=perf_counter() 

        dt=t2-t1

        size=3*(N**2)*8

        dts.append(dt)
        mem.append(size)

        fid.write(f"{N} {dt} {size}\n")

        print(f"Tiempo transcurrido = {dt} s")
        print(f"Memoria usada = {size} bytes")

        fid.flush()
        
fid.close()


#CURVAS PARA CADA ARCHIVO DE TEXTO
plt.figure()

for i in range(Ncorridas):
    tamano=[]
    tiempo=[]
    memoria=[]
    
    name=(f"matmul{i}.txt")
    f = open(name, "r")
    
    for i in f:
        lista_fila=i.split()
        tamano.append(int(lista_fila[0]))
        tiempo.append(float(lista_fila[1]))
        memoria.append(int(lista_fila[2]))
    f.close()
    
    plt.subplot(2,1,1)
    
    plt.plot(tamano,tiempo,marker="o",color="blue")
    plt.loglog(tamano,tiempo,marker="o")
    
    
    xTicks = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    xTicks_Text = ["","","","","","","","","","",""]
    
    yTicks = [10**-4,10**-3,10**-2,10**-1,1,10,60,600]
    yTicks_Text = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10min"]
    
    plt.yticks(yTicks, yTicks_Text)
    plt.xticks(xTicks, xTicks_Text,rotation=45)
    
    plt.title("Rendimiento A@B", fontsize=10)
    plt.ylabel("Tiempo transcurrido")
    
    plt.grid(True)
    
    plt.subplot(2,1,2)
    
    plt.plot(tamano, memoria,marker="o",color="blue")
    plt.loglog(tamano,memoria,marker="o")
    
    xTicks = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    xTicks_Text = ["10","20","50","100","200","500","1000",
                    "2000","5000","10000","20000"]
    
    yTicks = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
    yTicks_Text = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
    
    plt.yticks(yTicks, yTicks_Text)
    plt.xticks(xTicks, xTicks_Text,rotation=45)
    
    plt.xlabel("Tamaño matriz N")
    plt.ylabel("Uso memoria")
    
    plt.axhline(y=3*(10**10),color='k',ls="--")
    
    plt.grid(True)
    
    plt.tight_layout()
    
plt.show() 
