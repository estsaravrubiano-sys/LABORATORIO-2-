import random
import time
from metodo_ordenamiento import ordenamiento
from metodo_operaciones_matrices import *
def main():
    
    a = 0
    
    while a == 0:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Metodo de Ordenamiento")
        print("2. Operaciones con Matrices")
        print("3. Salir")
        opcion = input("Digite el menu deseado: ")

        match opcion : 
            case "1":
                q = 0
                while q == 0:
                    print("---Ordenamiento de números aleatorios---")
                    print("1. Método burbuja")
                    print("2. Método de inserción")
                    print("3. Método de selección")
                    print("4. Método merge sort")
                    print("5. Salir")
                    
                    opcion = input("Digite el menú deseado: ")
                    
                    
                    
                    
                    match opcion:
                        case "1":
                            cantidad = int(input("Ingrese la cantidad de números para la lista: "))
                            lista = []
                            
                            # CICLO PARA LLENAr LA LISTA
                            for i in range(cantidad):
                                numero = random.randint(1, 100)
                                lista.append(numero)
                            lista_original = lista.copy() # Una copia para mostrarla después
                            objeto = ordenamiento(lista)
                            
                            print("Lista original:", lista_original)
                            inicio = time.time()          # Tiempo antes de ordenar
                            lista_ordenada = objeto.burbuja()
                            fin = time.time()             # Tiempo después de ordenar
                            
                            # la diferencia
                            tiempo_total = fin - inicio
                            
                            print("Lista ordenada: ", lista_ordenada)
                            print(f" Tiempo de ejecución: {tiempo_total:.6f} segundos")    
                        case "2":
                            cantidad = int(input("Ingrese la cantidad de números para la lista: "))
                            lista = []
                            
                            # CICLO PARA LLENAr LA LISTA
                            for i in range(cantidad):
                                numero = random.randint(1, 100)
                                lista.append(numero)
                            lista_original = lista.copy() 
                            objeto = ordenamiento(lista)
                            
                            print("Lista original:", lista_original)
                            inicio = time.time()         
                            lista_ordenada = objeto.insercion()
                            fin = time.time()            
                        
                            tiempo_total = fin - inicio
                            
                            print("Lista ordenada: ", lista_ordenada)
                            print(f" Tiempo de ejecución: {tiempo_total:.6f} segundos")
                        case "3":
                            cantidad = int(input("Ingrese la cantidad de números para la lista: "))
                            lista = []
                            
                            # CICLO PARA LLENAr LA LISTA
                            for i in range(cantidad):
                                numero = random.randint(1, 100)
                                lista.append(numero)
                            lista_original = lista.copy() 
                            objeto = ordenamiento(lista)
                            
                            print("Lista original:", lista_original)
                            inicio = time.time()         
                            lista_ordenada = objeto.seleccion()
                            fin = time.time()            
                        
                            tiempo_total = fin - inicio
                            
                            print("Lista ordenada: ", lista_ordenada)
                            print(f" Tiempo de ejecución: {tiempo_total:.6f} segundos")
                        case "4":
                            cantidad = int(input("Ingrese la cantidad de números para la lista: "))
                            lista = []
                            
                            # CICLO PARA LLENAr LA LISTA
                            for i in range(cantidad):
                                numero = random.randint(1, 100)
                                lista.append(numero)
                            lista_original = lista.copy() 
                            objeto = ordenamiento(lista)
                            
                            print("Lista original:", lista_original)
                            inicio = time.time()         
                            lista_ordenada = objeto.mergesort(0, len(lista)-1)
                            fin = time.time()            
                        
                            tiempo_total = fin - inicio
                            
                            print("Lista ordenada: ", lista_ordenada)
                            print(f" Tiempo de ejecución: {tiempo_total:.6f} segundos")
                        case "5":
                            break
            case "2":
                b = 0
                while b == 0:
                    print("---Operaciones con Matrices ---")
                    print("1. Suma de Matrices")
                    print("2. Producto de Matrices ")
                    print("3. Inversa de la Matriz")
                    print("4. Producto de una Matriz por Vector")
                    print("5. Salir")

                    Submenu = input("Digite el menu deseado: ")
                    if Submenu == "5":
                        break
                    filas = int(input("Digite la cantidad de filas: "))
                    columnas = int(input("Digite la cantidad de columnas: "))
                    matriz1 = Operaciones_con_Matrices(filas, columnas)
                    matriz1 = matriz1.generar_matriz()
                    fi = filas
                    co = columnas

                    print("Generando Matriz...")
                    time.sleep(1)
                    match Submenu:
                        case "1":
                            
                            print("---Suma de Matrices---")
                            matriz2 = Operaciones_con_Matrices(filas, columnas)
                            matriz2 = matriz2.generar_matriz()
                            print("")

                            print("Matriz 1:")
                            for fi in matriz1:
                                print (fi)
                            print("")

                            print ("Matriz 2: ")
                            for fi in matriz2:
                                print (fi)
                            print("")

                            matriz_r = Operaciones_con_Matrices(filas, columnas)
                            matriz_r = matriz_r.suma_matriz(matriz1,matriz2)


                            print ("Matriz resultante: ")

                            for fi in matriz_r:
                                print (fi)

                        case "2":
                            print("---Producto de Matrices---")
                            
                            matriz2 = Operaciones_con_Matrices(filas, columnas)
                            matriz2 = matriz2.generar_matriz()
                            print("")

                            print("Matriz 1:")
                            for fi in matriz1:
                                print (fi)
                            print("")

                            print ("Matriz 2: ")
                            for fi in matriz2:
                                print (fi)
                            print("")

                            matriz_r = Operaciones_con_Matrices(filas, columnas)
                            matriz_r = matriz_r.producto_matriz(matriz1,matriz2)


                            print ("Matriz resultante: ")

                            for fi in matriz_r:
                                print (fi)
                        case "3":
                            print("---Inversa de la matriz---")

                            print("")
                            
                            print("Matriz 1:")
                            for fi in matriz1:
                                print (fi)
                            print("")

                            matriz_r = Operaciones_con_Matrices(filas, columnas)
                            matriz_r = matriz_r.inversa(matriz1)

                            print("Matriz Resultante:")
                            for fi in matriz_r:
                                print (fi)
                            print("")
                            
                        case "4":
                            print("---Producto de una matriz por un vector---")

                            print("")
                            print("Matriz 1:")
                            for fi in matriz1:
                                print (fi)
                            print("")

                            vector = Operaciones_con_Matrices(1, columnas)
                            vector = vector.generar_vector()
                            print ("Vector: ", vector)
                            matriz_r = Operaciones_con_Matrices(filas, columnas)
                            matriz_r = matriz_r.producto_matriz_vector(matriz1,vector)
                            print("")
                            print("Matriz Resultante:")
                            for fi in matriz_r:
                                print (fi)
                            print("")
                            
                        case "5":
                            print("---Saliendo---")
                            break
            case "3":
                break      
main()