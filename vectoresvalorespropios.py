import numpy as np

#definir la matriz
D = np.array([[2,5,3], [9,5,8],[2,3,8]])

# Calculamos los valores propios y los vectores propios
valores_propios, vectores_propios = np.linalg.eig(D)

# Mostramos los resultados
print("Valores propios:")
print(valores_propios)
print("Vectores propios:")
print(vectores_propios)



