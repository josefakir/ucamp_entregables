# Pokédex - Python Project

Este proyecto es una Pokédex interactiva construida con Python que utiliza la API pública [PokeAPI](https://pokeapi.co/) para obtener información detallada sobre cualquier Pokémon. Al ingresar el nombre de un Pokémon, el programa muestra su información, abre su imagen frontal en el navegador y guarda sus datos en un archivo JSON.

## Características

- **Consumo de la API de PokeAPI**: Obtención de datos como peso, altura, habilidades y tipos.
- **Visualización de imágenes**: Apertura de la imagen frontal del Pokémon en el navegador.
- **Almacenamiento de datos**: Guarda los datos del Pokémon en un archivo JSON dentro de la carpeta `pokedex`.

## Cómo funciona

1. El usuario ingresa el nombre de un Pokémon.
2. El programa verifica si el Pokémon existe en la Pokédex:
   - Si existe:
     - Muestra su información en la terminal.
     - Abre su imagen frontal en el navegador.
     - Guarda sus datos en un archivo JSON dentro de la carpeta `pokedex`.
   - Si no existe, muestra un mensaje de error.
3. Si ocurre algún problema de conexión, se muestra el código de error HTTP correspondiente.

## Requisitos

Antes de ejecutar el programa, asegúrate de tener lo siguiente instalado:

- Python 3.7 o superior
- Biblioteca `requests`

Para instalar `requests`, ejecuta:
```bash
pip install requests
