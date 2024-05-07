import requests
import os
import json
import random

# API Pokemon
# PROYECTO MASTERMIND
# Solicita respuesta de la API
def api_pokemon():
    os.system('clear')
    print('󰟾' * 51)
    print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
    print('󰟾' * 51)
    print('-PREPARANDO EL JUEGO , POR FAVOR ESPERE UN MOMENTO-')
    print('󰟾' * 51)
    response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=150")
    list_pokemons = []
    
    if response.status_code == 200:
        data = response.json()
        pokemons_names = data["results"]
        
    for pokemon in pokemons_names:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon['name']}")
        pokemon_data = response.json()
        name = pokemon_data['name']
        if name:
           list_pokemons.append(name)
    return list_pokemons
        
           
def pokemon_menu(list_pokemons):
    game = False
    while game == False:
        choice_pokemons = []
        choice = input('-Que deseas hacer?-[PALABRAS MAYUSCULAS PARA RESPONDER]\n'
                       'A 󰛂 Elegir Pokemones Aleatorios\n'
                       'B 󰛂 ELegir los Pokemones manualmente\n')
        print('󰟾' * 15)
        os.system('clear')
        if choice == 'A':
            new_pokemons = []
            pokemon_1 = random.randint(1, 150)
            pokemon_2 = random.randint(1 ,150)
            pokemon_3 = random.randint(1, 150)
            choice_pokemon_1 = list_pokemons[int(pokemon_1)  - 1]
            choice_pokemon_2 = list_pokemons[int(pokemon_2)  - 1]
            choice_pokemon_3 = list_pokemons[int(pokemon_3)  - 1]
            new_pokemons.append(choice_pokemon_1)
            new_pokemons.append(choice_pokemon_2)
            new_pokemons.append(choice_pokemon_3)
            print('󰟾' * 60)
            print('󰛂 Haz elegido a {} , {} y {} para la batalla 󰛁'.format(choice_pokemon_1, choice_pokemon_2, choice_pokemon_3))
            print('󰟾' * 60)
            return new_pokemons    
        elif choice == 'B':
            new_pokemons = []
            choice_pokemon = False
            while choice_pokemon == False:
                for i , pokemon in enumerate(list_pokemons, 1):
                    print(f"{i}. {pokemon}")        
                    print('󰟾' * 15)
            
                print('Selecciona tu Pokemon , elige un Pokemon por su numero (1-150)\n'
                      '-------------[SOLO PUEDES ELEGIR 3 POKEMONES]-----------------')
                try:
                    choice_your_first_pokemon = int(input('Tu numero > '))
                    choice_first_pokemon = list_pokemons[int(choice_your_first_pokemon) - 1]
                    new_pokemons.append(choice_first_pokemon)
                except ValueError:
                    os.system('clear')
                    input('[TU ARGUMENTO NO ES VALIDO , INTENTEMOS DE NUEVO]\n'
                          '------------[ENTER PARA CONTINUAR]---------------')
                except IndexError:
                    os.system('clear')
                    input('[TU ARGUMENTO NO ES VALIDO , INTENTEMOS DE NUEVO]\n'
                          '------------[ENTER PARA CONTINUAR]---------------')
                    
                if len(new_pokemons) == 3:
                    os.system('clear')
                    return new_pokemons
        elif not choice:
            os.system('clear')
            input('[NO SELECCIONASTE NADA]-[ELIGE UNA RESPUESTA]\n'
                  '-----------[ENTER PARA CONTINUAR]------------\n')
            
def pokemon_battle(new_pokemons):
    print('Esta es tu lista de pokemones > ', new_pokemons)
             
            
def main():
    pokemons = api_pokemon()
    list_pokemons = pokemon_menu(pokemons)
    pokemon_battle(list_pokemons)
    
        
if __name__ == '__main__':
    main()