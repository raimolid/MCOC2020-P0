import numpy as np

def matriz_laplaciana_llena(N,t=np.float32):
    m=np.eye(N,N,dtype=t)-np.eye(N,N,1,dtype=t)
    return m+m.T


from scipy.sparse import eye

def matriz_laplaciana_dispersa(N,t=np.float32):
    m=eye(N,N,dtype=t)-eye(N,N,1,dtype=t)
    return m+m.T 

# A=matriz_laplaciana_llena(3)
# B=matriz_laplaciana_dispersa(3)

# print(type(A))
# print(A)
# print(type(B))
# print(B)
# print("multiplicacion:\n")
# print(A@A)
# print((B@B).toarray())


# a=np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.T)

