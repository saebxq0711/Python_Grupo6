n = int (input("Por favor ingrese la cantidad de marcas de zapatos compradas: "))
i = 1
total=0
while i <=n:

    nombre = input("Ingrese el nombre de la marca : ")   
    cantidad = int(input("Ingrese la cantidad de productos comprados: "))
    precio = float(input("Ingrese el valor de la compra: "))
    print(f"El total a pagar por la marca {nombre} es: ${precio * cantidad} ")
    total = total + (precio * cantidad )
    i += 1

print(f"El total de las compras es: ${total }")
porcentaje= (total*25)/100

print (f"El valor de las ganancias es:$", porcentaje)
