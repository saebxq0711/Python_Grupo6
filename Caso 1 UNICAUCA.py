# Definir variables 
primerparcial = 0.35
segundoparcial = 0.35
parcialfinal = 0.30

# Solicitar datos, Nombre y código estudiante 
nombreestu = input("Ingrese el nombre del estudiante: ")
codigoestu = input("Ingrese el código del estudiante: ")

# Solicitar Notas
Nota1parcial = float(input("Ingrese la nota del primer parcial: "))
Nota2parcial = float(input("Ingrese la nota del segundo parcial: "))
Notaparcialfinal = float(input("Ingrese la nota del tercer parcial: "))

# Validar la condiciones de las notas 
if Nota1parcial < 0.0 or Nota1parcial > 5.0:
    print("La nota ingresada está fuera de las notas que se usan en la institución, recuerda que las notas van desde 1 a 5")
    exit()

if Nota2parcial < 0.0 or Nota2parcial > 5.0:
    print("La nota ingresada está fuera de las notas que se usan en la institución, recuerda que las notas van desde 1 a 5")
    exit()

if Notaparcialfinal < 0.0 or Notaparcialfinal > 5.0:
    print("La nota ingresada está fuera de las notas que se usan en la institución, recuerda que las notas van desde 1 a 5")
    exit()

# Calcular nota
Notafinal = (Nota1parcial * primerparcial + Nota2parcial * segundoparcial + Notaparcialfinal * parcialfinal)

# Aprueba o no 
if Notafinal >= 3.5:
    print(f"{nombreestu}, con código {codigoestu}, ha aprobado la materia con una nota definitiva de {Notafinal:.2f}.")
else:
    print(f"{nombreestu}, con código {codigoestu}, ha reprobado la materia con una nota definitiva de {Notafinal:.2f}.")
