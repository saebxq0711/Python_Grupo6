#solicitar nombre y edad 

Nombre =input("Ingresa tu nombre: ")
Edad = int(input("Ingresa tu edad: "))

if Edad >=18 :
    print (F"Buenos dias,{Nombre} usted es mayor de edad y puede participar en la votacion")

else:
    print  (F"Buenos dias,{Nombre} usted es menor de edad y no podra participar en la votacion")