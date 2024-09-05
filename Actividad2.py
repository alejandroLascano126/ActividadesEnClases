import random

def valoresParesImpares():
    sumNumerosPares = 0
    for i in range(500):
        numeroGenerado = random.randint(50,100)
        sumNumerosPares += 1 if numeroGenerado % 2 == 0 else 0

    return sumNumerosPares

cantidadPares = valoresParesImpares()
print("Se generan 500 numeros del 50 al 100 de los cuales ->")
print("Son pares: " + str(cantidadPares) + " impares: " + str(500 - cantidadPares))

