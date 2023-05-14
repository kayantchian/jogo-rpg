from time import sleep
import random
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from player import Player
from enemy import Enemy

def fight(player, enemy) -> bool:
        print(f"""\n Um(a) {enemy.name} se aproxima!\n
              | HP: {enemy.hp}
              | ATK: {enemy.atk}
              | DEF: {enemy.den}
              | CRITICAL ATK: {enemy.critical_atk}%\n""")
        sleep(1)
        turn = random.choice([True, False])
        while enemy.hp > 0:
            turn = not turn
            print(f"\n{enemy.name}: {enemy.hp} HP", end="\n")
            print(f"Você: {player.hp} HP", end="\n")
            print("", end="\n")
            sleep(1.5)
            #Player's turn
            if(turn == True):
                sleep(1)
                player_choice = inquirer.select(
        message="Selecione uma opção:",
        choices=["Atacar","Item","Passar a vez", "Fugir"],
    ).execute()
                
                if(player_choice == "Atacar"):
                    if(player.atk > enemy.den):
                        print(f"\nVocê causou {player.atk} de dano!", end="\n")
                        enemy.hp = enemy.hp - player.atk
                        print(f"{enemy.name}: {enemy.hp} HP", end="\n")
                    else:
                        print(f"\nSeu ataque não causou dano em {enemy.name}", end="\n")
                        enemy.den -= player.atk
                        print(f"Mas a defesa de {enemy.name} foi reduzida para {enemy.den}")
                
                elif(player_choice == "Fugir"):
                    if random.random() <= 0.25:
                        print('\nVocê conseguiu fugir!', end="\n")
                        sleep(2)
                        break
                        return True
                    else:
                        print(f'\n{enemy.name} bloqueou a sua fuga.', end="\n")
                elif(player_choice == "Passar a vez"):
                    pass
                
            #Enemy's turn        
            elif(turn == False):
                sleep(1)
                if(enemy.atk > player.den):
                    print(f"\n{enemy.name} te atacou! {enemy.atk} de dano\n", end="\n")
                    player.hp -= enemy.atk
                else:
                    player.den -= enemy.atk
                    print(f"\nO ataque de {enemy.name} não teve efeito.", end="\n")
                    sleep(0.5)
                    print(f"Mas sua defesa foi reduzida para {player.den}")
            #Verifies if player is dead
            if player.hp <= 0:
                for x in range(1, 10):
                    print("==", end="", flush=True)
                    sleep(0.1)
                for char in "\n\n     GAME OVER      \n\n":
                    print(char, end="", flush=True)
                    sleep(0.1)
                for x in range(1, 10):
                    print("==", end="", flush=True)
                    print("\n", end="\n")
                    sleep(1)
                break
                return False
              
        #Verifies if enemy is dead:
        if enemy.hp <= 0:
            print(f"\n{enemy.name} morreu!")
            player.xp += enemy.xp
            print(f'{enemy.xp} pontos de xp adquiridos! Atual: {player.xp}' , end="\n")
            print(f'{enemy.money} moedas adquiridas! Atual: {player.money}' , end="\n")
            return True