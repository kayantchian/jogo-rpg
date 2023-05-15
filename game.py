from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from random import choice
from player import *
from loja import Loja
from levels.level1 import *

def game() -> bool:
    player = perform_player_creation()
    loja = Loja()
    op = True
    while(op):
        print("", end="\n")
        moviment = inquirer.select(
            message="Onde quer ir?\n",
            choices=[
                "Floresta",
                "Loja",
                "Status",
                "Inventário",
                "Equipamento",
                Choice(value=False, name="Voltar"),
            ]
        ).execute()
    
    
        if(moviment=="Floresta"):
            level1(player)
        elif(moviment=="Loja"):
            print(f"\nSaldo atual: {player.money}\n")
            categoria = inquirer.select(
                message="Selecione uma opção da Loja:",
                choices=["Itens Mágicos","Equipamentos",Choice(value=False, name="Sair"), ]).execute()
            if(categoria == "Itens Mágicos"):
                player.buy_item(loja.menu(categoria))
            elif(categoria == "Equipamentos"):
                player.buy_equip(loja.menu(categoria))
        elif(moviment=="Inventário"):
            player.invent()
        elif(moviment=="Equipamento"):
            player.equipament()
        elif(moviment == "Status"):
            player.status()
        else:
            break
        
        
if(__name__ == "__main__"):
    game()