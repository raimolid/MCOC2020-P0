import numpy as np

def mimatmul(A,B):
    matriz=[]
    for i in range(len(A)):
        lista=[]
        for j in range(len(B[0])):
            suma=0
            for k in range(len(B)):
                suma+= A[i][k]*B[k][j]
            lista.append(suma)
        matriz.append(lista)    
    C= np.array(matriz)
    return C
