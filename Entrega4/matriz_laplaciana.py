from numpy import float32,zeros

def matriz_laplaciana(N, dtype=float32):
    A=zeros((N,N), dtype=dtype)
    
    for i in range(N):
        for j in range(N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A