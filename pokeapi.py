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
        choice = input(' Que deseas hacer?  PALABRAS MAYUSCULAS PARA RESPONDER \n'
                       '  A 󰛂 Elegir Pokemones Aleatorios\n'
                       '  B 󰛂 ELegir los Pokemones manualmente\n'
                       'Tu respuesta : ')
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
                print('󰋇 SELECCIONA TU POKEMON 󰩔 \n')
                for i , pokemon in enumerate(list_pokemons, 1):
                    print(f"{i}. {pokemon}")        
                    print('󰟾' * 15)
                print('')
                print(' Selecciona tu Pokemon , elige un Pokemon por su numero (1-150)\n'
                      '             󰐝 SOLO PUEDES ELEGIR 3 POKEMONES 󰐝                   ')
                try:
                    choice_your_first_pokemon = int(input('Tu respuesta : '))
                    choice_first_pokemon = list_pokemons[int(choice_your_first_pokemon) - 1]
                    new_pokemons.append(choice_first_pokemon)
                except ValueError:
                    os.system('clear')
                    input('󰬅 TU ARGUMENTO NO ES VALIDO , INTENTEMOS DE NUEVO 󰬅\n'
                          '              [ENTER PARA CONTINUAR]                 ')
                except IndexError:
                    os.system('clear')
                    input('󰬅 TU ARGUMENTO NO ES VALIDO , INTENTEMOS DE NUEVO 󰬅\n'
                          '              [ENTER PARA CONTINUAR]                 ')
                if len(new_pokemons) == 3:
                    os.system('clear')
                    return new_pokemons
        elif not choice:
            os.system('clear')
            input(' NO SELECCIONASTE NADA, ELIGE UNA RESPUESTA \n'
                  '            [ENTER PARA CONTINUAR]            \n')
            
def pokemon_start(new_pokemons):
    os.system('clear')
    print('󰟾' * 51)
    print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
    print('󰟾' * 51)
    print('-PREPARANDO LA PELEA , POR FAVOR ESPERE UN MOMENTO-')
    print('󰟾' * 51)
    sleep(10)
    input('              [ENTER PARA CONTINUAR]               ')
    os.system('clear')
    start = False
    while start == False:
        print('󰟾' * 51)
        print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
        print('󰟾' * 51)
        print('')
        print('󰨉 Estos son tus pokemones > ', new_pokemons)
        ready_or_not_ready = input(' Estas listo para la pelea?\n'
                                   '  A 󰛂 Si estoy listo\n'
                                   '  B 󰛂 No estoy listo\n'
                                   'Tu respuesta : ')
        if ready_or_not_ready == 'A':
            os.system('clear')
            print('󰟾' * 51)
            print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
            print('󰟾' * 51)
            print('')
            input('󱡂 ENTONCES A LUCHAR , PREPARATE PARA LA BATALLA 󱡂\n'
                  '            [ENTER PARA CONTINUAR]               \n')
            os.system('clear')
            break
        elif ready_or_not_ready == 'B':
            os.system('clear')
            print('󰟾' * 51)
            print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
            print('󰟾' * 51)
            print('')
            input('[ENTONCES VETE COBARDE!]-[ENTER PARA SALIR DEL JUEGO]\n')
            break
        elif not ready_or_not_ready:
            os.system('clear')
            print('󰟾' * 51)
            print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
            print('󰟾' * 51)
            print('')
            input('[TU ARGUMENTO NO ES VALIDO , INTENTEMOS DE NUEVO]\n'
                  '------------[ENTER PARA CONTINUAR]---------------')
            os.system('clear')
            
def pokemon_battle(new_pokemons , list_pokemons):
    start_battle = False
    while not start_battle:
        print('󰟾' * 51)
        print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
        print('󰟾' * 51)
        print('')
        print('󰨉 Tus Pokemones > ', new_pokemons)
        your_choice = int(input(' Que Pokemon deseas utilizar?\n'
                            '      1 󰛂 El primer Pokemon\n'
                            '      2 󰛂 El segundo Pokemon\n'
                            '      3 󰛂 El tercer Pokemon\n'
                            'Tu respuesta : '))
        if your_choice == 1:
            print(' Elegiste a > ', new_pokemons[0])
            pokemon_user = new_pokemons[0]
        elif your_choice == 2:
            print(' Elegiste a > ', new_pokemons[1])
            pokemon_user = new_pokemons[1]
        elif your_choice == 3:
            print(' Elegiste a > ', new_pokemons[2])
            pokemon_user = new_pokemons[2]
        
        cpu_pokemons = []
        cpu_1 = random.randint(1, 146)
        cpu_2 = random.randint(1 ,146)
        cpu_3 = random.randint(1, 146)
        choice_cpu_1 = list_pokemons[int(cpu_1)  - 1]
        choice_cpu_2 = list_pokemons[int(cpu_2)  - 1]
        choice_cpu_3 = list_pokemons[int(cpu_3)  - 1]
        cpu_pokemons.append(choice_cpu_1)
        cpu_pokemons.append(choice_cpu_2)
        cpu_pokemons.append(choice_cpu_3)

        battle = input('󱚝 Tu rivales son : {} , {} , {} '.format(choice_cpu_1, choice_cpu_2, choice_cpu_3))
        start_of_the_game = False
        while start_of_the_game == False:
            elegy_pokemon = {
                'name' : pokemon_user,
                pokemon_user : 300
            }
            enemy_pokemons = {
                'pokemon_1' : choice_cpu_1,
                choice_cpu_1 : 100,
                'pokemon_2' : choice_cpu_2,
                choice_cpu_2 : 100,
                'pokemon_3' : choice_cpu_3,
                choice_cpu_3 : 100
            }
            name_enemy_1 = enemy_pokemons['pokemon_1']
            life_enemy_1 = enemy_pokemons[choice_cpu_1]
            attack_1 = random.randint(1, 3)
            print('Turno de > ', name_enemy_1 + ' 󰚩 [CPU]')
            if attack_1 == 1:
                print(name_enemy_1 + ' ataca con Ataque Fuerte y te resta 20 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            elif attack_1 == 2:
                print(name_enemy_1 + ' ataca con Ataque Debil y te resta 10 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            elif attack_1 == 3:
                print(name_enemy_1 + ' se regenera con Curacion y se cura 15 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            name_enemy_2 = enemy_pokemons['pokemon_2']
            life_enemy_2 = enemy_pokemons[choice_cpu_2]
            attack_2 = random.randint(1, 3)
            print('Turno de > ', name_enemy_2 + ' 󰚩 [CPU]')
            if attack_2 == 1:
                print(name_enemy_2 + ' ataca con Ataque Debil y te resta 5 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            elif attack_2 == 2:
                print(name_enemy_2 + ' ataca con Ataque Fuerte y te resta 15 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            elif attack_2 == 3:
                print(name_enemy_2 + ' se regenera con Curacion y se cura 10 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            name_enemy_3 = enemy_pokemons['pokemon_3']
            life_enemy_3 = enemy_pokemons[choice_cpu_3]
            attack_3 = random.randint(1, 3)
            print('Turno de > ', name_enemy_3 + ' 󰚩 [CPU]')
            if attack_3 == 1:
                print(name_enemy_3 + ' ataca con Ataque Debil y te resta 25 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            elif attack_3 == 2:
                print(name_enemy_3 + ' ataca con Ataque Fuerte y te resta 35 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            elif attack_3 == 3:
                print(name_enemy_3 + ' se regenera con Curacion y se cura 20 puntos de vida')
                input('----------------------[ENTER PARA CONTINUAR]-------------------------')
            print('Turno de > ' + elegy_pokemon['name'] + "  [TU]")
            input('Que deseas hacer?\n'
                  '1 󰛂 Ataque Fuerte 󱡂\n'
                  '2 󰛂 Ataque Debil 󰓥\n'
                  '3 󰛂 Curacion Instantanea 󱐱\n'
                  '4 󰛂 Bloquear Golpe \n'
                  'Tu respuesta : ')
            
            
            
           
            
           
            
           
            
            # input('Hola')
            
            # input('Turno de ' + enemy_pokemons[choice] + ' [CPU]')
            # cpu_choice = random.randint(1, 3)
            
            
           
        
            
            
def main():
    pokemons = api_pokemon()
    list_pokemons = pokemon_menu(pokemons)
    pokemon_start(list_pokemons)
    pokemon_battle(list_pokemons , pokemons)
    
        
if __name__ == '__main__':
    main()