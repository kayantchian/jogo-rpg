from time import sleep
import random
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from player import *
from enemy import *


def anjo_guardiao(player) -> bool:
    if (len(player.inventory) > 0):
        for item in player.inventory:
            item.get('name') == "Anjo Guardião"
            player.inventory.remove(item)
            return True
        return False
    else:
        return False


def find_dict_by_value(items, key, value):
    for item in items:
        if item.get(key) == value:
            return item
    return None


def magic_item_choice(player):
    print("\n")
    selected_item = inquirer.select(
        message="Selecione um item mágico\n",
        choices=[f"{item['name']}: MANA -> {item['cost_mana']}, MAGIC ATK -> {item['magic_atk']}" for item in player.magic_weapons]).execute()
    selected_item = selected_item.split(":", 1)  # get name of item in string
    item = find_dict_by_value(player.magic_weapons, "name", selected_item[0])
    return item


def weapon_item_choice(player):
    print("\n")
    selected_item = inquirer.select(
        message="Selecione uma arma\n",
        choices=[f"{item['name']}: ATK -> {item['atk']}" for item in player.weapons]).execute()
    selected_item = selected_item.split(":", 1)  # get name of item in string
    item = find_dict_by_value(player.weapons, "name", selected_item[0])
    return item


def shield_item_choice(player):
    print("\n")
    selected_item = inquirer.select(
        message="Selecione um item mágico\n",
        choices=[f"{item['name']}: DEF -> {item['den']}, RESISTÊNCIA MÁGICA: -> {item['magic_den']}" for item in player.shields]).execute()
    selected_item = selected_item.split(":", 1)  # get name of item in string
    item = find_dict_by_value(player.shields, "name", selected_item[0])
    return item


def fight(player, enemy) -> bool:
    DEFENSE = 0
    MAGIC_RESISTENCE = 0
    print(f"\n Um(a) {enemy.name} se aproxima!\n")
    sleep(1)
    turn = random.choice([True, False])
    while enemy.hp > 0:
        turn = not turn
        print(f""" --- {enemy.name} ---
              | HP: {enemy.hp}
              | ATK: {enemy.atk}
              | MAGIC ATK: {enemy.magic_atk}
              | DEF: {enemy.den}
              | RESISTÊNCIA MÁGICA: {enemy.magic_den}
              | ATAQUE CRÍTICO: {enemy.critical_atk}%\n""")
        player.status()
        sleep(1.5)
        # Player's turn
        if (turn == True):
            DEFENSE = 0
            MAGIC_RESISTENCE = 0
            player.recuperacao_mana()
            sleep(1)
            player_choice = inquirer.select(
                message="Selecione uma opção:",
                choices=["Atacar", "Magia", "Defender",
                         "Item", "Passar a vez", "Fugir"],
            ).execute()
            # Magic damage
            if (player_choice == "Magia"):
                magic_item = magic_item_choice(player)
                if (player.mana >= magic_item['cost_mana']):
                    sleep(0.5)
                    magical_atk = magic_item['magic_atk'] + player.bonus_magic_atk()
                    player.mana -= magic_item['cost_mana']
                    if (magical_atk > enemy.magic_den):
                        enemy.magic_den -= magical_atk
                        print(
                            f"\nVocê causou {magical_atk} de dano mágico!", end="\n")
                        enemy.hp = enemy.hp - (magical_atk-enemy.magic_den)
                    else:
                        print(
                            f"Seu ataque não causou dano em {enemy.name}", end="\n")
                        enemy.magic_den -= magical_atk
                        print(
                            f"Mas a resistência mágica de {enemy.name} foi reduzida para {enemy.den}")
                else:
                    print(
                        f"\n Mana insuficiente. Requer {magic_item['cost_mana'] - player.mana} de mana.\n")

            # Fisical damage
            if (player_choice == "Atacar"):
                attack_item = weapon_item_choice(player)
                full_atk = player.atk + player.bonus_atk() + attack_item['atk']
                if (full_atk > enemy.den):
                    enemy.den -= full_atk
                    print(f"\nVocê causou {full_atk} de dano!", end="\n")
                    enemy.hp = enemy.hp - full_atk
                else:
                    print(
                        f"\nSeu ataque não causou dano em {enemy.name}", end="\n")
                    enemy.den -= full_atk
                    print(
                        f"Mas a defesa de {enemy.name} foi reduzida para {enemy.den}")

            if (player_choice == "Defender"):
                defense_item = shield_item_choice(player)
                DEFENSE = defense_item['den']
                MAGIC_RESISTENCE = defense_item['magic_den']
                print(f"\nVocê usou {defense_item['name']} para se defender!")

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
                pass

        # Enemy's turn
        elif (turn == False):
            enemy_choice = random.choice(ENEMY_CHOICES)
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
                sleep(1)
                magic = enemy.magic_atk - (MAGIC_RESISTENCE/100)*enemy.magic_atk
                if (magic > full_den_player):
                    if (random.random() <= (enemy.critical_atk)/100):
                        sleep(0.3)
                        print(
                            f"\n{enemy.name} te acertou um ataque crítico! {magic} de dano\n", end="\n")
                        player.hp = player.hp - (magic)
                    else:
                        print(
                            f"\n{enemy.name} te atacou com magia! {magic} de dano\n", end="\n")
                        player.hp = player.hp - (magic - full_den_player)
                        player.magic_den -= magic
                else:
                    player.magic_den -= magic
                    sleep(0.2)
                    print(f"\nA magia de {enemy.name} não teve efeito.", end="\n")
                    sleep(0.5)
                    print(
                        f"Mas sua resistencia mágica foi reduzida para {player.magic_den}")

        # Verifies if player is dead
        if player.hp <= 0:
            sleep(1.5)
            print("\nVocê morreu...")
            if (anjo_guardiao(player)):  # Verifier is player has anjo guardiao in its inventory
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
        print(f"\n{enemy.name} morreu!")
        player.xp += enemy.xp
        player.money += enemy.money
        print(f'{enemy.xp} pontos de xp adquiridos! Atual: {player.xp}', end="\n")
        print(f'{enemy.money} moedas adquiridas! Atual: {player.money}', end="\n")

        player.magic_den = player.MAGIC_MAX_DEN
        player.den = player.MAX_DEN
        player.mana = player.MAX_MANA
        return True


if (__name__ == "__main__"):
    lista = [{"name": "Lâmina de lumen", "price": 0, "magic_atk": 10,
              "magic_den": 0, "cost_mana": 10, 'limit': 1}]
    selected_item = inquirer.select(
        message="Selecione um item mágico\n",
        choices=[f"{item['name']}: MANA -> {item['cost_mana']}" for item in lista]).execute()
    selected_item = selected_item.split(":", 1)  # get name of item in string
    print(selected_item)
    item = find_dict_by_value(lista, "name", selected_item[0])
    print(item)
