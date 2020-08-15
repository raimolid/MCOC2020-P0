import scipy as sp
import scipy.linalg as spLinalg
import numpy as np
from time import perf_counter
import matplotlib.pyplot as plt


def matriz_laplaciana(N,t=np.float32):
    m=np.eye(N,N)-np.eye(N,N,1)
    return t(m+m.T)

#TAMAÑO MATRICES
Ns=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,
    200,250,350,500,600,800,1000,2000,5000,10000]

#NUMERO DE CORRIDAS
Ncorridas=10

#CREANDO ARCHIVOS DE TEXTO 
names=['A_invB_inv.txt','A_invB_npSolve.txt']

files=[open(name,"w") for name in names]

#FOR CADA TAMAÑO DE MATRIZ:10(Ncorridas) corridas x 2(Numsolvers) solver
for N in Ns:
    
    #10 filas (corridas) * 2 columnas (numero de solvers usados)
    dts=np.zeros((Ncorridas, len(names))) 
    
    print(f"Matriz de N = {N}") 
    
    #FOR CADA CORRIDA ANALIZO DISTINTOS SOLVER
    for i in range(Ncorridas):
        print(f"Corrida i= {i}")
        
        #INVIRTIENDO Y MULTIPLICANDO (Solver 0)
        A=matriz_laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_inv=np.linalg.inv(A)
        A_invB=A_inv@B
        t2=perf_counter() 
        dt=t2-t1
        #Agrego el tiempo a la columna 0(solver0) de la fila i(corrida1)
        dts[i][0]=dt  
        
        #OCUPANDO LINALG SOLVER (Solver 1)
        A=matriz_laplaciana(N)
        B=np.ones(N)
        t1=perf_counter()
        A_invB=np.linalg.solve(A,B)
        t2=perf_counter() 
        dt=t2-t1
        #Agrego el tiempo a la columna 1(solver1) de la fila i(corrida1)
        dts[i][1]=dt
        
        #(Solver 2)
        #(Solver 3)
        #....
    
    #TIEMPO PARA MATRIZ TAMAÑO N PARA SOLVER0, SOLVER1 X 10(CORRIDAS)
    print(f"dts:\n {dts}")
    
    #SACO EL PROM. DE LAS 10 CORRIDAS
    #GUARDO EN LISTA EL PROMEDIO PARA CADA TAMAÑO MATRIZ
    dts_mean=[np.mean(dts[:,j]) for j in range(len(files))] 
    
    print(f"dts mean:\n {dts_mean}")
    
    #ESCRIBIENDO ARCHIVOS DE TEXTO
    #2 ARCHIVO POR CADA TAMAÑO DE MATRIZ
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()
        
[file.close() for file in files]

#CURVAS PARA CADA ARCHIVO DE TEXTO

plt.figure()

for name in names:
    tamano=[]
    tiempo=[]
    f = open(name, "r")
    
    for i in f:
        lista_fila=i.split()
        tamano.append(int(lista_fila[0]))
        tiempo.append(float(lista_fila[1])) 
        
    #plt.plot(tamano,tiempo,marker="o")
    plt.loglog(tamano,tiempo,marker="o",label=name)
    
    xTicks = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
    xTicks_Text = ["10","20","50","100","200","500","1000",
                    "2000","5000","10000","20000"]
    
    yTicks = [10**-4,10**-3,10**-2,10**-1,1,10,60,600]
    yTicks_Text = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10min"]
    
    plt.yticks(yTicks, yTicks_Text)
    plt.xticks(xTicks, xTicks_Text,rotation=45)
    
    plt.title("Desempeño INV", fontsize=10)
    plt.ylabel("Tiempo transcurrido")
    plt.xlabel("Tamaño matriz N")
    f.close()

plt.grid(True)
plt.legend()    
plt.tight_layout()           
plt.show() 
