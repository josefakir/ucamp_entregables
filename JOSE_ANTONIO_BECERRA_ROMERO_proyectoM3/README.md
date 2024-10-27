# Simulación de la Máquina de Galton

Este proyecto simula una Máquina de Galton con 3000 canicas que caen a través de 12 niveles de obstáculos. La máquina sigue el principio de probabilidad, donde las canicas pueden caer hacia la izquierda o la derecha en cada nivel. Al final, los resultados se muestran en un histograma que representa cuántas canicas caen en cada contenedor.

## Descripción del proyecto

### Funciones principales:

1. **Simulación del recorrido de las canicas:**
   La función `simular_canicas` simula el recorrido de cada canica desde el nivel superior hasta el inferior, donde tiene 12 posibilidades de moverse a la izquierda o a la derecha. Una vez que la canica llega al final, se incrementa el contador del contenedor correspondiente.
   
2. **Graficación del histograma:**
   La función `graficar_histograma` genera un histograma utilizando la librería `matplotlib`. Este histograma muestra la cantidad de canicas que han caído en cada uno de los 13 contenedores posibles.

3. **Impresión en consola:**
   El programa también imprime en la consola en qué contenedor cayó cada canica, permitiendo un seguimiento detallado de la simulación.

### Instrucciones de uso:

1. Ejecuta el código para simular la caída de 3000 canicas.
2. Se generará una gráfica de barras (histograma) mostrando la distribución de las canicas en los 13 contenedores.
3. Además, en la consola verás un registro de en qué contenedor cae cada canica.

### Librerías utilizadas:

- **`random`**: Para simular la dirección en la que cae cada canica (izquierda o derecha).
- **`matplotlib`**: Para la visualización de los resultados a través de un histograma.

## Reflexiones sobre el Bootcamp

Hasta ahora, el Bootcamp ha sido una experiencia de aprendizaje intensa pero gratificante. A través de este proyecto en particular, hemos aprendido la importancia de descomponer problemas grandes en funciones y módulos más manejables, lo cual facilita tanto el desarrollo como el mantenimiento del código.

Algunas reflexiones importantes que hemos recogido:

1. **La importancia de la planificación**: Antes de comenzar a escribir código, entender el problema y cómo dividirlo en pasos claros ha sido clave para proyectos como este. Nos ha enseñado que planificar ahorra tiempo a largo plazo.
   
2. **El valor de la colaboración**: El Bootcamp ha fomentado el trabajo en equipo y la colaboración, algo que se refleja en la resolución de problemas de manera más eficiente y creativa.
   
3. **La paciencia y la práctica**: A medida que avanzamos en la complejidad de los proyectos, hemos aprendido que la programación requiere paciencia. Resolver errores y mejorar el código es un proceso iterativo, pero la práctica constante nos ha permitido desarrollar mejores soluciones.

4. **Reflexión sobre el uso de librerías**: Librerías como `matplotlib` y `random` nos han permitido crear visualizaciones potentes y realizar simulaciones que de otra manera habrían sido complejas de manejar manualmente. Aprender a usar estas herramientas nos ha abierto la puerta a nuevas posibilidades en proyectos futuros.

En conclusión, el Bootcamp hasta ahora ha sido una experiencia increíblemente enriquecedora. No solo hemos ganado habilidades técnicas, sino también la confianza para enfrentar desafíos más grandes y resolver problemas del mundo real utilizando código.

---

¡Esperamos que disfrutes este proyecto tanto como nosotros disfrutamos creándolo!
