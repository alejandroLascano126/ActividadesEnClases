

sucursales = [
    "Pepito",
    "Juanito",
    "Albertito",
    "Juanita",
    "Sofiita",
    "Alejnadrito",
    "Luisillo",
    "Andreita",
    "Jonanthansito",
    "Luigito",
    "Andrisino",
    "Lascanito",
    "Chavesito",
    "Josueito",
    "Ericksito",
    "La Ganga", 
    "Comandato",
    "Juana",
    "Andrew",
    "James",
    "Alex",
    "Pycca",
    "Mi comisariato",
    "Mi Jugueteria",
    "Ferreteria"
]

ventas = [
    5000,
    4000,
    7000,
    9000,
    10000,
    500,
    7000,
    8000,
    19000,
    9000,
    4000,
    3000,
    2000,
    1000,
    90000,
    58700, 
    50000,
    8000,
    46000,
    25000,
    76000,
    90000,
    435000,
    156000,
    1000
]

def obtenerPromediosDeVentas(ventas):
    suma = sum(ventas)  
    return suma // len(ventas) 

def SucursalesConVentasMayorAlPromedio(promedio, sucursales, ventas):
    sucursalesConVentasMayorAlPromedio = []
    
   
    for sucursal, venta in zip(sucursales, ventas):
        if venta > promedio:
            sucursalesConVentasMayorAlPromedio.append(sucursal)
    
    return sucursalesConVentasMayorAlPromedio


promedioDeVentas = obtenerPromediosDeVentas(ventas)


sucursalesVentasMayorAlPromedio = SucursalesConVentasMayorAlPromedio(promedioDeVentas, sucursales, ventas)


print("El promedio de ventas fue: " + str(promedioDeVentas))
print("Las sucursales con ventas mayor al promedio fueron: ")
for sucursal in sucursalesVentasMayorAlPromedio:
    print(sucursal)
