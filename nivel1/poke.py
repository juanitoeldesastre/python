pokedex = [
    {
        'Numero' : 83,
        'Nombre' : 'Farfetch',
        'Tipo'   : ['Volador', 'Normal']
    },
    {
        'Numero' : 25,
        'Nombre' : 'Pikachu',
        'Tipo'   : ['Eléctrico']
    },
    {
        'Numero' : 1,
        'Nombre' : 'Bulbasaur',
        'Tipo'   : ['Planta', 'Veneno']
    },
    {
        'Numero' : 6,
        'Nombre' : 'Charizard',
        'Tipo'   : ['Fuego', 'Volador']
    },
    {
        'Numero' : 7,
        'Nombre' : 'Squirtle',
        'Tipo'   : ['Agua']
    },
    {
        'Numero' : 150,
        'Nombre' : 'Mewtwo',
        'Tipo'   : ['Psíquico']
    },
    {
        'Numero' : 143,
        'Nombre' : 'Snorlax',
        'Tipo'   : ['Normal']
    },
    {
        'Numero' : 94,
        'Nombre' : 'Gengar',
        'Tipo'   : ['Fantasma', 'Veneno']
    },
    {
        'Numero' : 12,
        'Nombre' : 'Butterfree',
        'Tipo'   : ['Bicho', 'Volador']
    },
    {
        'Numero' : 131,
        'Nombre' : 'Lapras',
        'Tipo'   : ['Agua', 'Hielo']
    },
    {
        'Numero' : 135,
        'Nombre' : 'Jolteon',
        'Tipo'   : ['Eléctrico']
    },
    {
        'Numero' : 149,
        'Nombre' : 'Dragonite',
        'Tipo'   : ['Dragón', 'Volador']
    },
    {
        'Numero' : 248,
        'Nombre' : 'Tyranitar',
        'Tipo'   : ['Roca', 'Siniestro']
    },
    {
        'Numero' : 39,
        'Nombre' : 'Jigglypuff',
        'Tipo'   : ['Normal', 'Hada']
    },
    {
        'Numero' : 151,
        'Nombre' : 'Mew',
        'Tipo'   : ['Psíquico']
    },
    {
        'Numero' : 245,
        'Nombre' : 'Suicune',
        'Tipo'   : ['Agua']
    },
    {
        'Numero' : 145,
        'Nombre' : 'Zapdos',
        'Tipo'   : ['Eléctrico', 'Volador']
    },
    {
        'Numero' : 146,
        'Nombre' : 'Moltres',
        'Tipo'   : ['Fuego', 'Volador']
    },
    {
        'Numero' : 144,
        'Nombre' : 'Articuno',
        'Tipo'   : ['Hielo', 'Volador']
    },
    {
        'Numero' : 94,
        'Nombre' : 'Garchomp',
        'Tipo'   : ['Dragón', 'Tierra']
    }
]

for pokemon in pokedex:
    print(f"El pokemon {pokemon['Nombre']} es tipo {' y '.join(pokemon['Tipo'])}")

import random

equipo_pokemon = random.sample(pokedex, 6)

print("Tu equipo Pokémon es:")
for pokemon in equipo_pokemon:
    print(f"{pokemon['Nombre']} (Tipo: {' y '.join(pokemon['Tipo'])})")
