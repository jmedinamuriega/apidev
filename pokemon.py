import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

def print_pokemon_info(pokemon_data):
    name = pokemon_data['name']
    abilities = []
    for ability in pokemon_data['abilities']:
        abilities.append(ability['ability']['name'])
    print(f"Name: {name}")
    print("Abilities:", ", ".join(abilities))

pokemon_name = "pikachu"
pokemon_data = fetch_pokemon_data(pokemon_name)
print_pokemon_info(pokemon_data)

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_list = []

for name in pokemon_names:
    pokemon_data = fetch_pokemon_data(name)
    pokemon_list.append(pokemon_data)

for pokemon in pokemon_list:
    print_pokemon_info(pokemon)

average_weight = calculate_average_weight(pokemon_list)
print(f"Average Weight: {average_weight} hectograms")
