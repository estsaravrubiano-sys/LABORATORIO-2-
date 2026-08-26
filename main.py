import random
import time
from metodo_ordenamiento import ordenamiento

def main():
    print("Ordenamiento de números aleatorios")
    a = 0
    
    while a == 0:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Método burbuja")
        print("2. Método de inserción")
        print("3. Método de selección")
        print("4. Método merge sort")
        print("5. Salir")
        
        opcion = input("Digite el menú deseado: ")
        
        if opcion == "5":
            print("¡Saliendo del programa. Adiós!")
            break
            
        if opcion in ["1", "2", "3", "4"]:
            try:
                cantidad = int(input("Ingrese la cantidad de números para la lista: "))
                lista = []
                
                # CICLO PARA LLENAr LA LISTA
                for i in range(cantidad):
                    numero = random.randint(1, 100)
                    lista.append(numero)
                
                match opcion:
                    case "1":
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
                        lista_original = lista.copy() 
                        objeto = ordenamiento(lista)
                        
                        print("Lista original:", lista_original)
                        inicio = time.time()         
                        lista_ordenada = objeto.mergesort(0, len(lista)-1)
                        fin = time.time()            
                    
                        tiempo_total = fin - inicio
                        
                        print("Lista ordenada: ", lista_ordenada)
                        print(f" Tiempo de ejecución: {tiempo_total:.6f} segundos")
                        
            except ValueError:
                print(" ingresa un número entero válido.")
        else:
            print("Opción no válida.")
main()