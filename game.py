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
    moviment = inquirer.select(
        message="Onde quer ir?",
        choices=[
            "Floresta",
            "Loja",
            Choice(value=False, name="Voltar"),
        ]
    ).execute()
    if(moviment=="Floresta"):
        print(f"Você entrou na floresta...")
        sleep(2)
        enemy = random.choice(Enemy.ENEMY_LIST)
        jogador.fight(enemy)
    if(moviment=="Loja"):
        jogador.comprar_item(loja.menu())
    
if(__name__ == "__main__"):
    game()