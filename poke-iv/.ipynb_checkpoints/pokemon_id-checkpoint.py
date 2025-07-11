import requests

def get_pokemon_id_name_dict():
    pokemon_dict = {}
    url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción para errores HTTP

            data = response.json()
            results = data["results"]

            if not results:
                break  # No hay más Pokémon para obtener

            for pokemon_data in results:
                # El ID del Pokémon se puede extraer de la URL
                # La URL tiene el formato: "https://pokeapi.co/api/v2/pokemon/ID/"
                parts = pokemon_data["url"].split('/')
                pokemon_id = int(parts[-2]) # El ID es el penúltimo elemento

                pokemon_name = pokemon_data["name"]
                pokemon_dict[pokemon_name] = pokemon_id

        except requests.exceptions.RequestException as e:
            print(f"Error al conectar con la API: {e}")
            break
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            break
    return pokemon_dict

if __name__ == "__main__":
    pokemon_id_name_map = get_pokemon_id_name_dict()
    if pokemon_id_name_map:
        # Imprime los primeros 10 elementos para verificar
        print("Diccionario de Pokémon (primeros 10):")
        count = 0
        for p_id, p_name in pokemon_id_name_map.items():
            print(f"{p_name}: \"{p_id}\"")
            count += 1
            if count >= 10:
                break
        print(f"\nTotal de Pokémon encontrados: {len(pokemon_id_name_map)}")

        # Ejemplo de acceso a un elemento
        print(f"\nEl Pokémon con ID 1 es: {pokemon_id_name_map.get(1)}")
        print(f"El Pokémon con ID 25 es: {pokemon_id_name_map.get(25)}")