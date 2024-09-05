def pedirSumarNumero():
    suma = 0
    for i in range(10):
        numero = int(input("Ingrese un numero para sumar: \n"))
        suma += numero

    promedio = suma // 10
    sumaPromedio = [suma, promedio]
    return sumaPromedio


valorAMostrar = pedirSumarNumero()
print("La suma de los numeros ingresados: " + str(valorAMostrar[0]))
print("El promedio de los numeros ingresados: " + str(valorAMostrar[1]))


