
# Variables

from operator import mul
from pdb import Restart


numero1 = 3
numero2 = 4

print(numero1)
print(numero2)
# Entradas y salidas 

print("Ingrese el numero 1")
numero1 = input()
numero1 = int(numero1)
print("Ingrese el numero 2")
numero2 = input()
numero2 = int(numero2)
print(numero1)
print(numero2)

# Condicionales

if numero1<numero2:
    print("El numero 1 es menor que el numero 2")
else:
    print("El numero 1 es mayor que el numero 2")
    
    # Operaciones
    suma = numero1 + numero2
    print(suma)
    
    Resta = numero1 - numero2
    print(Resta)
    
    multiplicacion = numero1 * numero2
    print(multiplicacion)

    division = numero1 / numero2
    print(division)
    
    # Ciclos
    
    for i in range(5):
        print(i)
        
        #Ciclo while
    """while numero1 < 5:
        print(numero1)
        numero1 = numero1 + 1
    """
