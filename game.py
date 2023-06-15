from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from random import choice
from character.player import *
from shop import Loja
from levels.level1 import *
import emoji

def game() -> bool:
    player = Player(*perform_player_creation())
    loja = Loja()
    op = True
    while(op):
        sleep(0.7)
        print("", end="\n")
        moviment = inquirer.select(
            message="Onde quer ir?\n",
            choices=[
                "Começar jornada",
                "Loja",
                "Status",
                "Inventário",
                "Equipamento",
                Choice(value=False, name="Voltar"),
            ]
        ).execute()
    
    
        if(moviment=="Começar jornada"):
            level1(player)
        elif(moviment=="Loja"):
            print(f"\nSaldo atual: {player.money}\n")
            op_loja = True
            while(op_loja):
                sleep(0.7)
                print("", end="\n")
                categoria = inquirer.select(
                    message="Selecione uma opção da Loja:",
                    choices=["Itens","Armadura", "Armas", "Escudos", "Armas Mágicas",Choice(value=False, name="Sair"), ]).execute()
                if(categoria == "Itens"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_item(selected)
                elif(categoria == "Armadura"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_equip(selected)
                elif(categoria == "Armas"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_weapon(selected)
                elif(categoria == "Escudos"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_shield(selected)
                elif(categoria == "Armas Mágicas"):
                    selected = loja.menu(categoria)
                    if(selected!=False):
                        player.buy_magic_weapon(selected)
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