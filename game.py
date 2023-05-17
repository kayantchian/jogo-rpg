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
        sleep(0.7)
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
            op_loja = True
            while(op_loja):
                sleep(0.7)
                print("", end="\n")
                categoria = inquirer.select(
                    message="Selecione uma opção da Loja:",
                    choices=["Itens","Armadura", "Armas",Choice(value=False, name="Sair"), ]).execute()
                if(categoria == "Itens"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_item(selected)
                elif(categoria == "Armadura"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_item(selected)
                elif(categoria == "Armas"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_item(selected)
                elif(categoria == "Armas Mágicas"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_item(selected)
                else:
                    op_loja = False
                    
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