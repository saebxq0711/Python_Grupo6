def determinar_paridad (numero):
    if numero %2 ==0:
        return F"El numero {numero} es par. "
    else:
        return f"El numero {numero} es impar. "
numero = int (input("ingrese un numero"))
resultado = determinar_paridad(numero)
print (resultado)