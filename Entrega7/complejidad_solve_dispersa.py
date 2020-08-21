import scipy.sparse.linalg as spLinalg 
import numpy as np
import matplotlib.pyplot as plt
from numpy import double
from time import perf_counter
from matrices_laplacianas import matriz_laplaciana_dispersa 

#NUMERO DE CORRIDAS  
Ncorridas=5

#TAMAÑO DE MATRICES A PROBAR PARA CADA CORRIDA
Ns=np.array([2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,
    200,250,350,500,600,800,1000,2000,5000,10000])

#CREANDO ARCHIVOS DE TEXTO PARA CADA CORRIDA
for i in range(Ncorridas):
    print(f"Corrida i = {i}\n")
    dts1=[] 
    dts2=[]
    name=(f"solve{i}_dispersa.txt")
    file=open(name,"w")
    
    for N in Ns:
        print(f"N = {N}")

        t1=perf_counter()
        
        A=matriz_laplaciana_dispersa(N,double)
        B=np.ones(N)

        t2=perf_counter()
        C=spLinalg.spsolve(A,B)
        t3=perf_counter() 

        dt1=t2-t1
        dt2=t3-t2

        dts1.append(dt1)
        dts2.append(dt2)

        file.write(f"{N} {dt1} {dt2}\n")

        print(f"Tiempo de ensamblado = {dt1} s")
        print(f"Tiempo de solución = {dt2} s")

        file.flush()
        
file.close()


#CURVAS PARA CADA ARCHIVO DE TEXTO
plt.figure()
for i in range(Ncorridas):
    tamano=[]
    tiempo_ens=[]
    tiempo_sol=[]
    
    name=(f"solve{i}_dispersa.txt")
    f = open(name, "r")
    
    for i in f:
        lista_fila=i.split()
        tamano.append(double(lista_fila[0]))
        tiempo_ens.append(double(lista_fila[1]))
        tiempo_sol.append(double(lista_fila[2]))
    f.close()
    
    plt.subplot(2,1,1)
    
    plt.loglog(tamano,tiempo_ens,marker="o",ms=3,color="k",alpha=0.5)
    
    plt.subplot(2,1,2)
    
    plt.loglog(tamano,tiempo_sol,marker="o",ms=3,color="k",alpha=0.5)

tamano=np.array(tamano)
tiempo_ens=np.array(tiempo_ens)
tiempo_sol=np.array(tiempo_sol)

plt.subplot(2,1,1)    
    
for i in range(5):
    a=tiempo_ens[25]/tamano[25]**i
    if i==0:
        plt.loglog(tamano,(tamano**i)*a,'--',label='Cte')
    elif i==1:
        plt.loglog(tamano,(tamano**i)*a,'--',label='O(N)')
    else:
        plt.loglog(tamano,(tamano**i)*a,'--',label=f'$O(N^{i})$')

xTicks = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xTicks_Text = ["","","","","","","","","","",""]

yTicks = [10**-4,10**-3,10**-2,10**-1,1,10,60,600]
yTicks_Text = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10min"]

plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text,rotation=45)

plt.title("Complejidad Solve Matriz Dispersa", fontsize=10)
plt.ylabel("Tiempo de ensamblado")
plt.grid()
plt.ylim(10**-5,600)
    
    
plt.subplot(2,1,2) 

for i in range(5):
    a=tiempo_sol[25]/tamano[25]**i
    if i==0:
        plt.loglog(tamano,(tamano**i)*a,'--',label='Cte')
    elif i==1:
        plt.loglog(tamano,(tamano**i)*a,'--',label='O(N)')
    else:
        plt.loglog(tamano,(tamano**i)*a,'--',label=f'$O(N^{i})$')

xTicks = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xTicks_Text = ["10","20","50","100","200","500","1000",
        "2000","5000","10000","20000"]

yTicks = [10**-4,10**-3,10**-2,10**-1,1,10,60,600]
yTicks_Text = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10min"]

plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text,rotation=45)

plt.legend(loc=2,prop={'size': 8})
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo de solución")
plt.grid() 
plt.ylim(10**-5,600)

plt.tight_layout()
plt.show()