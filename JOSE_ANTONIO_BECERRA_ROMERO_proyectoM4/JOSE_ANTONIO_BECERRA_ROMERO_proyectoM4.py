import requests
import json
import os
import webbrowser

# Función para obtener datos de un Pokémon desde la API
def obtener_datos_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("El Pokémon no existe. Por favor verifica el nombre.")
        return None
    else:
        print(f"Error al conectar con la API. Código: {response.status_code}")
        return None

# Función para mostrar la información del Pokémon
def mostrar_informacion(pokemon):
    print("\n=== Información del Pokémon ===")
    print(f"Nombre: {pokemon['name'].capitalize()}")
    print(f"Peso: {pokemon['weight']} hectogramos")
    print(f"Altura: {pokemon['height']} decímetros")
    print("Habilidades:")
    for habilidad in pokemon['abilities']:
        print(f" - {habilidad['ability']['name'].capitalize()}")
    print("Tipos:")
    for tipo in pokemon['types']:
        print(f" - {tipo['type']['name'].capitalize()}")

# Función para mostrar la imagen frontal del Pokémon
def mostrar_imagen(pokemon):
    imagen_url = pokemon['sprites']['front_default']
    if imagen_url:
        print("\nAbriendo la imagen del Pokémon en el navegador...")
        webbrowser.open(imagen_url)
    else:
        print("No se encontró una imagen para este Pokémon.")

# Función para guardar los datos del Pokémon en un archivo JSON
def guardar_en_json(pokemon):
    cwd = os.getcwd() 
    cwd = cwd + "/JOSE_ANTONIO_BECERRA_ROMERO_proyectoM4"
    pokedex_path = os.path.join(cwd, "pokedex")
    if not os.path.exists(pokedex_path):
        os.makedirs(pokedex_path)

    archivo = os.path.join(pokedex_path, f"{pokemon['name']}.json")
    with open(archivo, "w") as file:
        json.dump(pokemon, file, indent=4)
    print(f"\nInformación de {pokemon['name']} guardada en {archivo}.   {cwd}")

# Función principal que integra todas las funcionalidades
def main():
    print("=== Bienvenido a la Pokédex ===")
    nombre = input("Introduce el nombre del Pokémon: ")
    datos_pokemon = obtener_datos_pokemon(nombre)

    if datos_pokemon:
        mostrar_informacion(datos_pokemon)
        mostrar_imagen(datos_pokemon)
        guardar_en_json(datos_pokemon)
    else:
        print("No se pudo obtener información del Pokémon.")

if __name__ == "__main__":
    main()
