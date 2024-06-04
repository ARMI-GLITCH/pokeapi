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
    play_again = True
    while play_again == True:
        start_battle = True
        prepare_for_battle = True
        while start_battle == True:
            print('󰟾' * 51)
            print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
            print('󰟾' * 51)
            print('')
            print('󰨉 Tus Pokemones > ', new_pokemons)
            try:
                your_choice = int(input(' Que Pokemon deseas utilizar?\n'
                                    '      1 󰛂 El primer Pokemon\n'
                                    '      2 󰛂 El segundo Pokemon\n'
                                    '      3 󰛂 El tercer Pokemon\n'
                                    'Tu respuesta : '))
                if your_choice == 1:
                    pokemon_elegy = 0
                    print(' Elegiste a > ', new_pokemons[0])
                    pokemon_user = new_pokemons[0]
                    break
                elif your_choice == 2:
                    pokemon_elegy = 1
                    print(' Elegiste a > ', new_pokemons[1])
                    pokemon_user = new_pokemons[1]
                    break
                elif your_choice == 3:
                    pokemon_elegy = 3
                    print(' Elegiste a > ', new_pokemons[2])
                    pokemon_user = new_pokemons[2]
                    break
            except ValueError:
                print('--NO ELEGISTE NADA--')
                input('ENTER PARA CONTINUAR')
        while prepare_for_battle == True:
            cpu_pokemons = []
            cpu_1 = random.randint(1, 146)
            choice_cpu_1 = list_pokemons[int(cpu_1)  - 1]
            cpu_pokemons.append(choice_cpu_1)
            
            battle = input('󱚝 Tu rival es : {}'.format(choice_cpu_1))
            life_your_pokemon = 350
            life_user = life_your_pokemon
            cpu_life = 350
            choice_cpu_life_1 = cpu_life
            disadvantage_or_advantage = random.randint(1, 5)
            if disadvantage_or_advantage == 1:
                wheel_of_fortune = random.randint(100, 200)
                life_your_pokemon += wheel_of_fortune
                os.system('clear')
                print(' Ventaja para: ' + pokemon_user)
                print('Haz recibido una ventaja, tienes una suma de {} puntos de vida\n'.format(wheel_of_fortune))
                input('                         ENTER PARA CONTINUAR                                     ')
                os.system('clear')
            elif disadvantage_or_advantage == 2:
                consumes_life = random.randint(50, 100)
                life_your_pokemon -= consumes_life
                os.system('clear')
                print(' Desventaja para: ' + pokemon_user)
                print('Haz recibido una desventaja, tienes una resta de {} puntos de vida\n'.format(consumes_life))
                input('                         ENTER PARA CONTINUAR                                     ')
                os.system('clear')
            elif disadvantage_or_advantage == 3:
                wheel_of_fortune = random.randint(100, 200)
                cpu_life += wheel_of_fortune
                os.system('clear')
                print('󱚝 Ventaja para: ' + choice_cpu_1)
                print('Ha recibido una ventaja, tiene una suma de {} puntos de vida\n'.format(wheel_of_fortune))
                input('                         ENTER PARA CONTINUAR                                     ')
                os.system('clear')
            elif disadvantage_or_advantage == 4:
                consumes_life = random.randint(50, 100)
                cpu_life -= consumes_life
                os.system('clear')
                print('󱚝  Desventaja para: ' + choice_cpu_1)
                print('Ha recibido una desventaja, tiene una resta de {} puntos de vida\n'.format(consumes_life))
                input('                         ENTER PARA CONTINUAR                                     ')
                os.system('clear')
            else:
                os.system('clear')
                input('Ninguno recibio ventajas..'
                    '   ENTER PARA CONTINUAR   ')
                os.system('clear')
            if start_battle:
                time_to_play = True
                while time_to_play == True:
                    your_attack = None
                    attack_1 = random.randint(1, 3)
                    print('󰟾' * 51)
                    print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
                    print('󰟾' * 51)
                    if attack_1 == 1:
                        random_attack_1 = random.randint(15, 30)
                        life_user -= random_attack_1
                        print('Turno de > ' + choice_cpu_1 + ' 󰚩 [CPU]')
                        print(choice_cpu_1 + ' ataca con Ataque Fuerte y te resta {} puntos de vida'.format(random_attack_1))
                        life_bar_of_your_pokemon = int(life_user * 10 / life_your_pokemon)
                        print(pokemon_user + '   : [{}{}] ({}/{})'.format('' * life_bar_of_your_pokemon, ' ' * (10 - life_bar_of_your_pokemon),
                                                                        life_user, life_your_pokemon))
                        life_bar_cpu_pokemon = int(choice_cpu_life_1 * 10 / cpu_life)
                        print(choice_cpu_1 + '   : [{}{}] ({}/{})'.format('' * life_bar_cpu_pokemon, ' ' * (10 - life_bar_cpu_pokemon),
                                                                        choice_cpu_life_1, cpu_life))
                        print(' ')
                        input('[----------------------[ENTER PARA CONTINUAR]-------------------------]')
                    elif attack_1 == 2:
                        random_attack_1 = random.randint(10, 20)
                        life_user -= random_attack_1
                        print('Turno de > ' + choice_cpu_1 + ' 󰚩 [CPU]')
                        print(choice_cpu_1 + ' ataca con Ataque Debil y te resta {} puntos de vida'.format(random_attack_1))
                        life_bar_of_your_pokemon = int(life_user * 10 / life_your_pokemon)
                        print(pokemon_user + '   : [{}{}] ({}/{})'.format('' * life_bar_of_your_pokemon, ' ' * (10 - life_bar_of_your_pokemon),
                                                                        life_user, life_your_pokemon))
                        life_bar_cpu_pokemon = int(choice_cpu_life_1 * 10 / cpu_life)
                        print(choice_cpu_1 + '   : [{}{}] ({}/{})'.format('' * life_bar_cpu_pokemon, ' ' * (10 - life_bar_cpu_pokemon),
                                                                        choice_cpu_life_1, cpu_life))
                        print(' ')
                        input('[----------------------[ENTER PARA CONTINUAR]-------------------------]')
                    elif attack_1 == 3:
                        random_life_1 = random.randint(10, 30)
                        choice_cpu_life_1 += random_life_1
                        print('Turno de > ' + choice_cpu_1 + ' 󰚩 [CPU]')
                        print(choice_cpu_1 + ' se regenera con Curacion y se cura {} puntos de vida'.format(random_life_1))
                        life_bar_of_your_pokemon = int(life_user * 10 / life_your_pokemon)
                        print(pokemon_user + '   : [{}{}] ({}/{})'.format('' * life_bar_of_your_pokemon, ' ' * (10 - life_bar_of_your_pokemon),
                                                                        life_user, life_your_pokemon))
                        life_bar_cpu_pokemon = int(choice_cpu_life_1 * 10 / cpu_life)
                        print(choice_cpu_1 + '   : [{}{}] ({}/{})'.format('' * life_bar_cpu_pokemon, ' ' * (10 - life_bar_cpu_pokemon),
                                                                        choice_cpu_life_1, cpu_life))
                        print(' ')
                        input('[----------------------[ENTER PARA CONTINUAR]-------------------------]')
                    try:
                        your_attack =  int(input(' Que deseas hacer?\n'
                                            '1 󰛂 Ataque Fuerte 󱡂\n'
                                            '2 󰛂 Ataque Debil 󰓥\n'
                                            '3 󰛂 Curacion Instantanea 󱐱\n'
                                            'Tu respuesta : '))
                    except ValueError:
                        print('[No hiciste nada en contra del rival]')
                        input('[-------[ENTER PARA CONTINUAR]------]')
                    except UnboundLocalError:
                        print('[No hiciste nada en contra del rival]')
                        input('[-------[ENTER PARA CONTINUAR]------]')
                    if your_attack == 1:
                        your_random = random.randint(10 , 30)
                        choice_cpu_life_1 -= your_random
                        print('Turno de > ' + pokemon_user + '  [TU]')
                        print(pokemon_user + ' usa Ataque Fuerte y a le restas {} puntos de vida'.format(your_random))
                        life_bar_of_your_pokemon = int(life_user * 10 / life_your_pokemon)
                        print(pokemon_user + '   : [{}{}] ({}/{})'.format('' * life_bar_of_your_pokemon, ' ' * (10 - life_bar_of_your_pokemon),
                                                                        life_user, life_your_pokemon))
                        life_bar_cpu_pokemon = int(choice_cpu_life_1 * 10 / cpu_life)
                        print(choice_cpu_1 + '   : [{}{}] ({}/{})'.format('' * life_bar_cpu_pokemon, ' ' * (10 - life_bar_cpu_pokemon),
                                                                        choice_cpu_life_1, cpu_life))
                        print(' ')
                        input('[----------------------------[ENTER PARA CONTINUAR]----------------------------------]')
                        os.system('clear')
                    if your_attack == 2:
                        your_random = random.randint(15, 20)
                        choice_cpu_life_1 -= your_random
                        print('Turno de > ' + pokemon_user + '  [TU]')
                        print(pokemon_user + ' usa Ataque Debil y le restas {} puntos de vida'.format(your_random))
                        life_bar_of_your_pokemon = int(life_user * 10 / life_your_pokemon)
                        print(pokemon_user + '   : [{}{}] ({}/{})'.format('' * life_bar_of_your_pokemon, ' ' * (10 - life_bar_of_your_pokemon),
                                                                        life_user, life_your_pokemon))
                        life_bar_cpu_pokemon = int(choice_cpu_life_1 * 10 / cpu_life)
                        print(choice_cpu_1 + '   : [{}{}] ({}/{})'.format('' * life_bar_cpu_pokemon, ' ' * (10 - life_bar_cpu_pokemon),
                                                                        choice_cpu_life_1, cpu_life))
                        print(' ')
                        input('[----------------------------[ENTER PARA CONTINUAR]----------------------------------]')
                        os.system('clear')
                    if your_attack == 3:
                        random_life = random.randint(10, 25)
                        life_user += random_life
                        print('Turno de > ' + pokemon_user + '  [TU]')
                        print(pokemon_user + ' usa Curacion Instantanea y te curas {} puntos de vida'.format(random_life))
                        life_bar_of_your_pokemon = int(life_user * 10 / life_your_pokemon)
                        print(pokemon_user + '   : [{}{}] ({}/{})'.format('' * life_bar_of_your_pokemon, ' ' * (10 - life_bar_of_your_pokemon),
                                                                        life_user, life_your_pokemon))
                        life_bar_cpu_pokemon = int(choice_cpu_life_1 * 10 / cpu_life)
                        print(choice_cpu_1 + '   : [{}{}] ({}/{})'.format('' * life_bar_cpu_pokemon, ' ' * (10 - life_bar_cpu_pokemon),
                                                                        choice_cpu_life_1, cpu_life))
                        print(' ')
                        input('[----------------------------[ENTER PARA CONTINUAR]----------------------------------]')
                        os.system('clear')
                    if choice_cpu_life_1 <= 0:
                        time_to_play = False
                        cpu_pokemons = []
                        print(cpu_pokemons)
                        print('Hola')
                        break
                    elif life_user <= 0:
                        time_to_play = False
                        new_pokemons.remove(pokemon_user)
                        print(new_pokemons)
                        os.system('clear')
                        try:
                            again = input(' Deseas continuar luchando?\n'
                                        'S 󰛂 Seguir Luchando!!\n'
                                        'N 󰛂 Me rindo..\n')
                            if again == 'S':
                                choice_pokemon = True
                                while choice_pokemon == True:
                                    os.system('clear')
                                    print('󰟾' * 51)
                                    print('󱎂-----󰐝------󰠰󰠰--POKEMON-BATTLE--󰠰󰠰------󰐝--------󱎂')
                                    print('󰟾' * 51)
                                    print('')
                                    print('󰨉 Tus Pokemones > ', new_pokemons)
                                    try:
                                        your_choice = int(input(' Que Pokemon deseas utilizar?\n'
                                                                '  1 󰛂 El primer Pokemon\n'
                                                                '  2 󰛂 El segundo Pokemon\n'
                                                                '  3 󰛂 El tercer Pokemon\n'
                                                                'Tu respuesta : '))
                                        if your_choice == 1:
                                                print(' Elegiste a > ', new_pokemons[0])
                                                pokemon_user = new_pokemons[0]
                                                play_again = True
                                                break 
                                        elif your_choice == 2:
                                                print(' Elegiste a > ', new_pokemons[1])
                                                pokemon_user = new_pokemons[1]
                                                play_again = True
                                                break
                                        elif your_choice == 3:
                                                print(' Elegiste a > ', new_pokemons[2])
                                                pokemon_user = new_pokemons[2]
                                                play_again = True
                                                break
                                    except ValueError:
                                        print('Hola WEY')
                            elif again == 'N':
                                    play_again = False
                        except ValueError:
                            input('No mames cabron')
                            
                    
            
        
        
            
def main():
    pokemons = api_pokemon()
    list_pokemons = pokemon_menu(pokemons)
    pokemon_start(list_pokemons)
    pokemon_battle(list_pokemons , pokemons)
    
        
if __name__ == '__main__':
    main()