#debe de pedir, NOMBRE, PATERNO, MATERNO, EDAD, PESO Y ESTATURA, desplegarlos en pantalla y también desplegar el IMC (IMC = peso / estatura al cuadrado);
import numbers
nombre = ""
while not nombre:
    nombre = input("¿Cual es tu nombre?\n")
    if not nombre:
        print("El nombre no debe estar vacio")

paterno = ""
while not paterno:
    paterno = input("¿Cual es tu apellido paterno?\n")
    if not paterno:
        print("El apellido paterno no debe estar vacio")

materno = ""
while not materno:
    materno = input("¿Cual es tu apellido materno?\n")
    if not materno:
        print("El apellido materno no debe estar vacio")

edad = ""
while not edad.isdigit():
    edad = input("Ingrese su edad: ")
    if not edad.isdigit():
        print("La edad no puede estar vacía, y debe de ser un número")
edad = int(edad)

peso = ""
while True:
    peso = input("Ingrese su peso en Kg (puede incluir decimales): ")
    try:
        peso = float(peso)
        if isinstance(peso, numbers.Number):
            break
    except ValueError:
        print("El peso no puede estar vacío, y debe de ser un número (puede incluir decimales)")

estatura = ""
while True:
    estatura = input("Ingrese su estatura en metros (puede incluir decimales): ")
    try:
        estatura = float(estatura)
        if isinstance(estatura, numbers.Number):
            break
    except ValueError:
        print("La estatura no puede estar vacía, y debe de ser un número (puede incluir decimales)")

#TENEMOS LISTOS LOS INPUT, AHORA ES MOMENTO DE CALCULAR EL IMC PESO/ESTATURA²

IMC = peso / (estatura  ** 2)

print(f"Tu nombre es: {nombre} {paterno} {materno}")
print(f"La edad ingresada es: {edad}")
print(f"El peso ingresado es: {peso}")
print(f"La estatura ingresada es: {estatura}")
print(f"Tu IMC es: {IMC}")
