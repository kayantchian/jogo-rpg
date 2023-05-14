from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from random import choice
from player import *
from enemy import *
from loja import Loja
from mechanics import fight

def game():
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
                "Inventário",
                Choice(value=False, name="Voltar"),
            ]
        ).execute()
    
    
        if(moviment=="Floresta"):
            print(f"\nVocê entrou na floresta...\n")
            sleep(2)
            enemy = Enemy("Gárgula", *perform_enemy_creation("easy"))
            if(fight(player, enemy)):
                print("Você passou!")
            else:
                op = False
                return False
        elif(moviment=="Loja"):
            print(f"\nSaldo atual: {player.money}\n")
            categoria = inquirer.select(
                message="Selecione uma opção da Loja:",
                choices=["Itens mágicos","Equipamentos",Choice(value=False, name="Sair"), ]).execute()
            if(categoria == "Itens mágicos"):
                player.buy_item(loja.menu(categoria))
            elif(categoria == "Equipamentos"):
                player.buy_equip(loja.menu(categoria))
        elif(moviment=="Inventário"):
            player.invent()
        else:
            break
        
        
if(__name__ == "__main__"):
    game()