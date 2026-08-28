import random

class Operaciones_con_Matrices:
    def __init__(self, f, c):
        
        self.f = f
        self.c = c
    def generar_vector(self):
        vector = []
        for x in range (self.c):
            vector.append (random.randint(0, 100))
        return vector

    def generar_matriz (self):
        matriz = [] 
        for i in range (self.f):
            fila = []
            for x in range (self.c):
                fila.append (random.randint(0, 100))
            matriz.append(fila)
        return matriz   
    def suma_matriz (self, matriz1, matriz2):
        matriz_r = []
        for i in range (self.f):
            fila = []
            for x in range (self.c):
                fila.append(matriz1 [i][x] + matriz2 [i] [x]) 
            matriz_r.append(fila)
        return matriz_r
    def producto_matriz(self, matriz1, matriz2):
        fila1 = len(matriz1)
        columna1 = len(matriz1[0])
        columna2 = len(matriz2[0])
        
        matriz_r = []
        for i in range(fila1):
            fila = []
            for j in range(columna2):
                suma = 0
                for k in range(columna1):
                    suma += matriz1[i][k] * matriz2[k][j]
                fila.append(suma)
            matriz_r.append(fila)
        return matriz_r           
    def producto_matriz_vector(self, matriz, vector):
        filas = len(matriz)
        columnas = len(matriz[0])
        
        if columnas != len(vector):
            print("Error: el número de columnas de la matriz debe ser igual al tamaño del vector")
            return None
        
        resultado = []
        for i in range(filas):
            suma = 0
            for j in range(columnas):
                suma += matriz[i][j] * vector[j]
            resultado.append(suma)
        return resultado   
    def inversa(self, matriz1):
        n = len(matriz1)
        
        # Verificar que sea cuadrada
        if len(matriz1[0]) != n:
            print("Error: la matriz debe ser cuadrada para tener inversa")
            return None

        # Crear matriz aumentada [A | I]
        aumentada = []
        for i in range(n):
            fila = matriz1[i][:]  # copia de la fila original
            for j in range(n):
                fila.append(1 if i == j else 0)
            aumentada.append(fila)

        # Eliminación Gauss-Jordan
        for i in range(n):
            # Si el pivote es 0, buscar una fila para intercambiar
            if aumentada[i][i] == 0:
                for k in range(i+1, n):
                    if aumentada[k][i] != 0:
                        aumentada[i], aumentada[k] = aumentada[k], aumentada[i]
                        break
                else:
                    print("Error: la matriz no tiene inversa (determinante = 0)")
                    return None

            # Normalizar la fila del pivote (dividir toda la fila entre el pivote)
            pivote = aumentada[i][i]
            for j in range(2*n):
                aumentada[i][j] = aumentada[i][j] / pivote

            # Hacer ceros en las demás filas de esa columna
            for k in range(n):
                if k != i:
                    factor = aumentada[k][i]
                    for j in range(2*n):
                        aumentada[k][j] -= factor * aumentada[i][j]

        # Extraer la mitad derecha (la inversa)
        inversa = []
        for i in range(n):
            inversa.append(aumentada[i][n:])
        
        return inversa     