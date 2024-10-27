import random
import matplotlib.pyplot as plt

# Función para simular el recorrido de las canicas
def simular_canicas(n_canicas, n_niveles):
    contenedores = [0] * (n_niveles + 1)  # Creamos una lista de contenedores
    
    for i in range(n_canicas):
        posicion = 0
        for _ in range(n_niveles):
            # Decidimos si cae a la derecha (1) o a la izquierda (0)
            posicion += random.choice([0, 1])
        
        # Incrementamos el contenedor correspondiente
        contenedores[posicion] += 1
        
        # Imprimimos en qué contenedor cayó la canica
        print(f"Canica {i + 1} cayó en el contenedor {posicion}")
    
    return contenedores

# Función para graficar el histograma con los totales encima de cada barra
def graficar_histograma(contenedores):
    niveles = range(len(contenedores))
    
    plt.bar(niveles, contenedores)

    # Añadir el total de cada barra encima
    for i in range(len(contenedores)):
        plt.text(i, contenedores[i] + 10, str(contenedores[i]), ha='center')

    # Añadir títulos y etiquetas
    plt.title("Simulación de la Máquina de Galton")
    plt.xlabel("Distribución de canicas")
    plt.ylabel("Cantidad de canicas")
    
    plt.show()

# Parámetros de la simulación
n_canicas = 3000
n_niveles = 12

# Simulación y graficación
contenedores = simular_canicas(n_canicas, n_niveles)
graficar_histograma(contenedores)
