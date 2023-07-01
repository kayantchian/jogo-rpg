from time import sleep
import random
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from character.player import *
from character.enemy import *

    
def use_item(player, item) -> bool:
    if (len(player.inventory) > 0):
        for item in player.inventory:
            item.get('name') == item
            player.inventory.remove(item)
            return True
        return False
    else:
        return False


def find_dict_by_value(items, key, value) -> dict:
    for item in items:
        if item.get(key) == value:
            return item
    return None


def magic_item_choice(player)  -> dict:
    print("\n")
    selected_item = inquirer.select(
        message="Selecione um item mágico\n",
        choices=[f"{item['name']}: MANA -> {item['cost_mana']}, MAGIC ATK -> {item['magic_atk']}" for item in player.magic_weapons] + ["Voltar"]
        ).execute()
    if(selected_item != "Voltar"):
        selected_item = selected_item.split(":", 1)  # get name of item in string
        item = find_dict_by_value(player.magic_weapons, "name", selected_item[0])
        return item
    else:
        return False

def skill_choice(player) -> dict:
    print("\n")
    selected_item = inquirer.select(
        message="Selecione uma habilidade\n",
        choices=[f"{skill['name']}: MANA -> {skill['cost_mana']}" for skill in player.skills] + ["Voltar"]
        ).execute()
    if(selected_item != "Voltar"):
        selected_item = selected_item.split(":", 1)  # get name of item in string
        item = find_dict_by_value(player.skills, "name", selected_item[0])
        return item
    else:
        return False

def weapon_item_choice(player) -> dict:
    print("\n")
    selected_item = inquirer.select(
        message="Selecione uma arma\n",
        choices=[f"{item['name']}: ATK -> {item['atk']}" for item in player.weapons] + ["Voltar"]).execute()
    if(selected_item != "Voltar"):
        selected_item = selected_item.split(":", 1)  # get name of item in string
        item = find_dict_by_value(player.weapons, "name", selected_item[0])
        return item
    else:
        return False

def shield_item_choice(player) -> dict:
    print("\n")
    selected_item = inquirer.select(
        message="Selecione um item mágico\n",
        choices=[f"{item['name']}: DEF -> {item['den']}, RESISTÊNCIA MÁGICA: -> {item['magic_den']}" for item in player.shields] + ["Voltar"]).execute()
    if(selected_item != "Voltar"):
        selected_item = selected_item.split(":", 1)  # get name of item in string
        item = find_dict_by_value(player.shields, "name", selected_item[0])
        return item
    else: 
        return False

def exploration(player) -> dict:
    pass

def fight(player, enemy) -> bool:
    DEFENSE = 0
    MAGIC_RESISTENCE = 0
    ENEMY_DEFENSE = 0
    ENEMY_MAGIC_RESISTENCE = 0
    print(f"\n Um(a) {enemy.name} se aproxima!\n")
    sleep(0.5)
    player_choose_op = True
    turn = random.choice([True, False])
    while enemy.hp > 0:
        if(player_choose_op):
            turn = not turn
            sleep(1)
            print(f""" --- {enemy.name} ---
                | HP: {enemy.hp:.2f}
                | ATK: {enemy.atk:.2f}
                | MAGIC ATK: {enemy.magic_atk:.2f}
                | DEF: {enemy.den:.2f}
                | RESISTÊNCIA MÁGICA: {enemy.magic_den:.2f}
                | ATAQUE CRÍTICO: {enemy.critical_atk:.2f}%\n""")
            player.status()
        sleep(2)
        # Player's turn
        if (turn == True):
            DEFENSE = 0
            MAGIC_RESISTENCE = 0
            player.recuperacao_mana()
            sleep(1)
            print("\n")
            player_choice = inquirer.select(
                message="Selecione uma opção:",
                choices=["Atacar", "Magia", "Habilidade", "Defender",
                         "Curar", "Passar a vez", "Fugir"],
            ).execute()


            if(player_choice == "Curar"):
                if(use_item(player,"Poção de vida")):
                    player.hp = player.MAX_HP
                    print(f"\nVocê se curou.\nHP atual: {player.hp}")
                    sleep(1.5)
                else:
                    print("\nVocê não possui poções")
                    sleep(1.5)
            
            # Magic damage
            if (player_choice == "Magia"):
                magic_item = magic_item_choice(player)
                if(magic_item): #Magic weapon choice
                    player_choose_op = True
                    if (player.mana >= magic_item['cost_mana']):
                        sleep(0.5)
                        magical_atk = magic_item['magic_atk'] + player.bonus_magic_atk()
                        magical_atk -= (magical_atk*(ENEMY_MAGIC_RESISTENCE)/100)
                        player.mana -= magic_item['cost_mana']
                        if (magical_atk > enemy.magic_den):
                            enemy.magic_den -= magical_atk
                            print(
                                f"\nVocê causou {magical_atk} de dano mágico!", end="\n")
                            enemy.hp = enemy.hp - (magical_atk-enemy.magic_den)
                            sleep(1.5)
                        else:
                            print(
                                f"Seu ataque não causou dano em {enemy.name}", end="\n")
                            enemy.magic_den -= magical_atk
                            print(
                                f"\nMas a resistência mágica de {enemy.name} foi reduzida para {enemy.den}")
                            sleep(1.5)
                    else:
                        print(
                            f"\nMana insuficiente. Requer {magic_item['cost_mana'] - player.mana} de mana.\n")
                        sleep(1.5)
                else: #If player didn't chose a magic weapon.
                    player_choose_op = False
                    pass
            # Fisical damage
            if (player_choice == "Atacar"):
                attack_item = weapon_item_choice(player)
                if(attack_item): #Verifies if player choose an item
                    player_choose_op = True
                    full_atk = player.atk + player.bonus_atk() + attack_item['atk']
                    full_atk -= (full_atk*(ENEMY_DEFENSE)/100)
                    if (full_atk > enemy.den):
                        enemy.den -= full_atk
                        print(f"\nVocê causou {full_atk} de dano!", end="\n")
                        enemy.hp = enemy.hp - (full_atk-enemy.den)
                        sleep(1.5)
                    else:
                        print(
                            f"\nSeu ataque não causou dano em {enemy.name}", end="\n")
                        enemy.den -= full_atk
                        print(
                            f"\nMas a defesa de {enemy.name} foi reduzida para {enemy.den}")
                        sleep(1.5)
                else:
                    player_choose_op = False
                    pass

            if(player_choice == "Habilidade"):
                skill = skill_choice(player)
                if(skill): #Verifies if player choose an skill
                    player_choose_op = True
                    if (player.mana >= skill['cost_mana']): #If player has mana
                        player.mana -= skill['cost_mana']
                        damage = skill['skill'](player)
                        full_atk = damage*(ENEMY_MAGIC_RESISTENCE)/100
                        if (full_atk > enemy.magic_den):
                            enemy.magic_den -= full_atk
                            print(f"\nVocê causou {full_atk} de dano!", end="\n")
                            enemy.hp = enemy.hp - (full_atk-enemy.magic_den)
                            sleep(2)
                        else:
                            print(
                                f"\nMas seu ataque não causou dano em {enemy.name}", end="\n")
                            enemy.magic_den -= full_atk
                            sleep(1)
                            print(
                                f"\nMas a resistência mágica de {enemy.name} foi reduzida para {enemy.magic_den}")
                            sleep(2)
                    else:
                        print(
                            f"\nMana insuficiente. Requer {magic_item['cost_mana'] - player.mana} de mana.\n")
                        sleep(1.5)
                else:
                    player_choose_op = False
                    pass
            if (player_choice == "Defender"):
                defense_item = shield_item_choice(player)
                if(defense_item): #Verifies if player choose a defense item
                    player_choose_op = True
                    DEFENSE = defense_item['den']
                    MAGIC_RESISTENCE = defense_item['magic_den']
                    print(f"\nVocê usou {defense_item['name']} para se defender!")
                    sleep(2)
                else:
                    player_choose_op = False
                    pass

            elif (player_choice == "Fugir"):
                if random.random() <= 0.25:
                    print('\nVocê conseguiu fugir!', end="\n")
                    sleep(2)
                    break
                    return True
                else:
                    print(f'\n{enemy.name} bloqueou a sua fuga.', end="\n")
                    
            elif (player_choice == "Passar a vez"):
                print("\nVocê passou a vez!\n")
                sleep(1.5)
                pass

        # Enemy's turn
        elif (turn == False):
            enemy_choice = random.choice(ENEMY_CHOICES)
            ENEMY_DEFENSE = 0
            ENEMY_MAGIC_RESISTENCE = 0
            # FISICAL ATTK ENEMY
            if (enemy_choice == "atk"):
                if(DEFENSE>0):
                    print("\nVocê se defendeu do ataque...")
                full_den_player = player.den + player.bonus_den()
                atk = enemy.atk - (DEFENSE/100)*enemy.atk
                sleep(1)
                if (atk > full_den_player):
                    if (random.random() <= (enemy.critical_atk)/100):
                        sleep(0.3)
                        print(
                            f"\n{enemy.name} te acertou um ataque crítico! {atk} de dano\n", end="\n")
                        player.hp = player.hp - atk
                    else:
                        print(
                            f"\n{enemy.name} te atacou! {atk} de dano\n", end="\n")
                        player.hp = player.hp - (atk - full_den_player)
                        player.den -= atk
                else:
                    player.den -= atk
                    sleep(0.2)
                    print(
                        f"\nO ataque de {enemy.name} não teve efeito.", end="\n")
                    sleep(0.5)
                    print(f"Mas sua defesa foi reduzida para {player.den}")
                    
            # MAGIC ATK ENEMY
            elif (enemy_choice == "magic_atk"):
                if(MAGIC_RESISTENCE > 0):
                    print("\nVocê se defendeu do ataque...")
                full_den_player = player.magic_den + player.bonus_magic_den()
                sleep(1.5)
                magic = enemy.magic_atk - (MAGIC_RESISTENCE/100)*enemy.magic_atk
                if (magic > full_den_player):
                    if (random.random() <= (enemy.critical_atk)/100):
                        sleep(0.3)
                        print(
                            f"\n{enemy.name} te acertou um ataque crítico! {magic} de dano\n", end="\n")
                        player.hp = player.hp - (magic)
                        sleep(1.5)
                    else:
                        print(
                            f"\n{enemy.name} te atacou com magia! {magic} de dano\n", end="\n")
                        player.hp = player.hp - (magic - full_den_player)
                        player.magic_den -= magic
                        sleep(1.5)
                else:
                    player.magic_den -= magic
                    sleep(0.2)
                    print(f"\nA magia de {enemy.name} não teve efeito.", end="\n")
                    sleep(1.5)
                    print(
                        f"Mas sua resistencia mágica foi reduzida para {player.magic_den}")
                    sleep(1.5)
            #ENEMY DEFENSE
            elif(enemy_choice == "den"):
                print(f"\n{enemy.name} se defendeu!")
                ENEMY_DEFENSE = enemy.MAX_DEN
                ENEMY_MAGIC_RESISTENCE = enemy.MAGIC_MAX_DEN
                sleep(1.5)


        # Verifies if player is dead
        if player.hp <= 0:
            sleep(1.5)
            print("\nVocê morreu...")
            if (use_item(player, "Anjo Guardião")):  # Verifier is player has anjo guardiao in its inventory
                player.hp = player.MAX_HP
                sleep(1.5)
                print("Mas o Anjo Guardião ressuscitou você...\n")
                sleep(1.5)
            else:
                for x in range(1, 10):
                    print("==", end="", flush=True)
                    sleep(0.1)
                for char in "\n\n     GAME OVER      \n\n":
                    print(char, end="", flush=True)
                    sleep(0.1)
                for x in range(1, 10):
                    print("==", end="", flush=True)
                    sleep(0.1)
                print("\n", end="\n")
                sleep(1)
                break
                return False

    # Verifies if enemy is dead:
    if enemy.hp <= 0:
        sleep(0.5)
        print(f"\nVocê matou {enemy.name}.")
        player.xp += 200
        player.level_up()
        player.money += enemy.money
        sleep(0.7)
        print(f'[!] {enemy.xp} pontos de xp adquiridos! Atual: {player.xp}', end="\n")
        sleep(1.5)
        print(f'[$] {enemy.money} moedas adquiridas! Atual: {player.money}', end="\n")
        sleep(4)
        player.magic_den = player.MAGIC_MAX_DEN
        player.den = player.MAX_DEN
        player.mana = player.MAX_MANA
        player.hp += player.hp*0.3
        player.level_up
        return True






if (__name__ == "__main__"):
    lista = [{"name":"Shuriken_laminada", "cost_mana": 15, "skill": "shuriken_laminada"},
              {"name":"Corte Sombrio", "cost_mana": 25, "skill": "corte_sombrio"}]
    selected_item = inquirer.select(
        message="Selecione uma habilidade\n",
        choices=[f"{skill['name']}: MANA -> {skill['cost_mana']}" for skill in lista]).execute()
    selected_item = selected_item.split(":", 1)  # get name of item in string
    item = find_dict_by_value(lista, "name", selected_item[0])
    print(item['name'])

