import json

"""with open("superheroes.json") as superheroes_file:
    print(superheroes_file.read())
    print(json.load(superheroes_file))"""


with open("pokemons.json") as file:
    # content  = file.read()
    # pokemons = json.loads(content)["results"]
    pokemons = json.load(file)["results"]
    print(pokemons[0])
