from character.player import *
from character.enemy import *
from mechanics import *
from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from random import choice, random
from levels.quests import *

def level1(player):
    print(f"\nVocê entrou na floresta...\n")
    sleep(2)
    enemy = Enemy(choice(ENEMY_FLORESTA), *perform_enemy_creation(choice(ENEMY_LEVELS)))
    if(fight(player, enemy)):
        print(f"\nDepois de ter derrotado {enemy.name}, você continua sua caminhada pela floresta.")
        player.hp += 30
        print(f"Você recupera 35 de HP. {player.hp}")
        if(random() <= 0.85):
            quest_carlos(player)
            print("\nVocê continua a caminhada...\n")
        if(random() <= 0.45):
            sleep(1.5)
            enemy = Enemy(choice(ENEMY_FLORESTA), *perform_enemy_creation("normal")) 
            surprise_atk = randint(5,10)
            print(f"""Mas de repente um {enemy.name} e lhe ataca de surpresa!
                  Causando {surprise_atk} de dano crítico""")
            player.hp -= surprise_atk
            if(fight(player, enemy)):
                print("\nPassou do nível 1\n")
            else:
                op = False
                return False    
        else:
            sleep(3)
            print("\nDepois de uma longa caminhada, você chega numa estrada abandonada...\n")
    else:
        op = False
        return False
