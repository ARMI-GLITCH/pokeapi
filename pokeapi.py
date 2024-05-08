import requests
import os
import json
import random
from time import sleep

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
        print('')
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
                print('[-SELECCIONA TU POKEMON-]\n')
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
            
def pokemon_start(new_pokemons):
    os.system('clear')
    print('󰟾' * 51)
    print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
    print('󰟾' * 51)
    print('-PREPARANDO LA PELEA , POR FAVOR ESPERE UN MOMENTO-')
    print('󰟾' * 51)
    sleep(10)
    input('[-------------[ENTER PARA CONTINUAR]--------------]')
    os.system('clear')
    print('Estos son tus pokemones > ', new_pokemons)
    start = False
    while start == False:
        ready_or_not_ready = input('Estas listo para la pelea?\n'
                                   '-A-Si estoy listo\n'
                                   '-B-No estoy listo\n')
        if ready_or_not_ready == 'A':
            os.system('clear')
            input('[ENTONCES A LUCHAR]-[ENTER PARA CONTINUAR]\n')
            os.system('clear')
            break
        elif ready_or_not_ready == 'B':
            os.system('clear')
            input('[ENTONCES VETE COBARDE!]-[ENTER PARA SALIR DEL JUEGO]\n')
            break
        elif not ready_or_not_ready:
            os.system('clear')
            input('[TU ARGUMENTO NO ES VALIDO , INTENTEMOS DE NUEVO]\n'
                  '------------[ENTER PARA CONTINUAR]---------------')
            os.system('clear')
            
def pokemon_battle(new_pokemons , list_pokemons):
    start_battle = False
    while start_battle == False:
        print('󰟾' * 51)
        print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
        print('󰟾' * 51)
        print('')
        print('Tu Pokemones > ', new_pokemons)
        your_choice = input('Que Pokemon deseas utilizar?\n'
                            '-1-El primer Pokemon\n'
                            '-2-El segundo Pokemon\n'
                            '-3-El tercer Pokemon\n')
        if your_choice == 1:
            print('Elegiste a > ', new_pokemons[0])
        elif your_choice == 2:
            print('Elegiste a > ', new_pokemons[1])
        elif your_choice == 3:
            print('Elegiste a > ', new_pokemons[2])
            
        random_pokemon = random.randint(0 , 146)
        random_list = list_pokemons[random_pokemon]     
        battle = input('Tu contrincante es : '+ random_list)
        input('Turno de ' + random_list + ' [CPU]')
        cpu_choice = random.randint(1, 3)
        if cpu_choice == 1:
           input(random_list + ' ataca con Golpe Fuerte y te resta 20 puntos de vida\n'
                 '[--------------------[ENTER PARA CONTINUAR-----------------------]\n')
        elif cpu_choice == 2:
           input(random_list + ' ataca con Golpe Debil y te resta 10 puntos de vida\n'
                 '[--------------------[ENTER PARA CONTINUAR-----------------------]\n')
        elif cpu_choice == 3:
           input(random_list + ' se regenera con Curacion Fuerte y le sube 30 puntos de vida\n'
                 '[------------------------[ENTER PARA CONTINUAR---------------------------]\n')
        elif cpu_choice == 4:
            input(random_list + ' se regenera con Curacion Debil y le sube 15 puntos de vida\n'
                 '[------------------------[ENTER PARA CONTINUAR----------------------------]\n')
        
        
            
            
def main():
    pokemons = api_pokemon()
    list_pokemons = pokemon_menu(pokemons)
    pokemon_start(list_pokemons)
    pokemon_battle(list_pokemons , pokemons)
    
        
if __name__ == '__main__':
    main()