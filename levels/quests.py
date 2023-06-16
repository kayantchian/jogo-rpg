from mechanics import *
from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
from random import choice, random
from inutil import *


def quest_carlos(player):
    npc = "Carlos Henrique"
    sleep(2)
    print(f"{npc} -- Preciso de ajuda!! Meu malbec foi roubado")
    sleep(1)
    print(f"\n{npc} -- Eu suspeito de um aluno", end="", flush=True)
    ponto()
    print("\n")
    answer = inquirer.select(
            message=f"{npc} Você pode me ajudar a encontrá-lo?\n",
            choices=[
                "Claro!",
                "Não",
            ]
        ).execute()
    if(answer == "Claro!"):
        print(f"{npc} -- Que bom!")
        sleep(1)
        print(f"\n{npc} -- Eu sei onde ele mora. Vou te passar o endereço.\n Vá lá e traga meu malbec de volta!")
        sleep(4)
        print(f"\n{npc} te passa o endereço da casa do aluno suspeito, e você caminha até lá", end="", flush=True)
        enemy = Enemy("Eduardo, o Papaizão", 600, 25, 20, 45, 15, 100, 150, 15)
        sleep(5)
        print(f"\n\n{enemy.name} -- o que faz aqui na minha casa?")
        sleep(2)
        print(f"\n(Você) -- Vim pegar o malbec do {npc}. Dê-me agora!")
        sleep(2.5)
        print(f"\n{enemy.name} -- Não vou te dar nada! Se quiser terá de lutar comigo, seu miserável!\n")
        sleep(2)
        qst = inquirer.select(
            message=f"Lutar contra {enemy.name}?\n",
            choices=[
                "Sim",
                "Não",
            ]
        ).execute()
        if(qst == "Não"):
            print("\nVocê com medo foge da luta", end="", flush= True)
            pass
        if(qst=="Sim"):
            fight(player, enemy)
            print(f"\n{npc} -- Obrigado por devolver meu malbec!\n")
            print(f"\n{npc} -- Quer saber? Pode ficar com ele! Você merece", end="", flush=True)
            ponto()
            sleep(2)
            perfume = {"name":"Perfume Malbec", "price":0, "atk" : 35, "den" : 0, "magic_atk" : 0, "magic_den": 0,  'limit': 1}
            player.weapons.append(perfume)
    if(answer == "Não"):
        print(f"{npc} -- Poxa")
        ponto()
        pass
if(__name__ == "__main__"):
    pass     