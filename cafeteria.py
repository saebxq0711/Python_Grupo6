precio = float (input("Por favor ingrese el valor de el producto comprado: " ))
descuento = 0


if precio >0:
    if precio  >=100000:
        descuento = (precio*5)/100
else:
    if precio >=300000:
        descuento = (precio*10)/100

rebaja= precio-descuento
resta= descuento
print (f"El total a pagar es: ${rebaja}")
print (f"El descuento aplicado es: ${descuento}")