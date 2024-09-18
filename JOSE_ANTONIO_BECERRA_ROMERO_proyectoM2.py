def longitud():
    # Pedir palabra al usuario
    palabra = input("Ingrese una palabra\n")
    # Obtener la longitud de la palabra
    longitud = len(palabra)
    #Caso uno, longitud dentro del rango:
    if(longitud >=4 and longitud <=8):
        print("La palabra es correcta")
    #Caso dos, longitud abajo del rango:
    elif(longitud < 4):
        print(f"Hacen falta letras. Solo tiene {longitud} letras")
    #Caso tres, longitud arriba del rango:
    elif(longitud>8):
        print(f"Sobran letras. Tiene {longitud} letras")
#Mandar llamar la longitud:
longitud()



def pedir_coordenada(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor != 0:
                return valor
            else:
                print("Error: El valor no puede ser cero.")
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def coordenadas():
    # Pedir coordenada X
    x = pedir_coordenada("Introduce la coordenada X (entero): ")

    # Pedir coordenada Y
    y = pedir_coordenada("Introduce la coordenada Y (entero): ")

    # Guardar en una tupla ( esto se podría omitir, pero me hace más sencillo la impresión de las coordenadas )
    coordenadas = (x, y)

    #creo la variable cuadrante, para guardar su resultado
    cuadrante = ''

    #determinación del cuadrante:
    if(x>0 and y>0):
        cuadrante = 'I'
    elif(x<0 and y>0):
        cuadrante = "II"
    elif(x<0 and y<0):
        cuadrante = "III"
    elif(x>0 and y<0):
        cuadrante = "IV"
    # Mostrar la tupla con las coordenadas
    print(f"Las coordenadas son: {coordenadas} y se encuentran dentro del cuadrante: {cuadrante}")

coordenadas()