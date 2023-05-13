from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from random import choice
from player import *
from loja import Loja
from enemy import Enemy

def game():
    jogador = perform_player_creation()
    loja = Loja()
    op = True
    while(op):
        print("", end="\n")
        moviment = inquirer.select(
            message="Onde quer ir?\n",
            choices=[
                "Floresta",
                "Loja",
                "Inventário",
                Choice(value=False, name="Voltar"),
            ]
        ).execute()
    
    
        if(moviment=="Floresta"):
            print(f"\nVocê entrou na floresta...\n")
            sleep(2)
            enemy = random.choice(Enemy.ENEMY_LIST)
            jogador.fight(enemy)
        elif(moviment=="Loja"):
            jogador.comprar_item(loja.menu())
        elif(moviment=="Inventário"):
            jogador.invent()
        else:
            break
        
        
if(__name__ == "__main__"):
    game()