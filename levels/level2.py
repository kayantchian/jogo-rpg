from character.player import *
from character.enemy import *
from mechanics import *
from InquirerPy import inquirer
from random import choice, random, randint
from time import sleep

def level2(player):
    print("\n🛤️ Você pisa na Estrada Antiga, abandonada há décadas...\n")
    sleep(2)

    # Evento narrativo
    op = inquirer.select(
        message="Você encontra carroça destruída. O que faz?",
        choices=[
            "Investigar os destroços",
            "Ignorar e seguir caminho",
        ]
    ).execute()

    if op == "Investigar os destroços":
        if random() <= 0.6:
            print("\nVocê encontra suprimentos úteis!")
            player.hp += 25
            print(f"HP atual: {player.hp}")
        else:
            enemy = Enemy(
                choice(ENEMY_FLORESTA),
                *perform_enemy_creation("normal")
            )
            print("\nEra uma armadilha!")
            if not fight(player, enemy):
                return False

    sleep(1.5)

    # Combate obrigatório
    enemy = Enemy(
        "Saqueador da Estrada",
        *perform_enemy_creation("normal")
    )

    print("\n⚔️ Um Saqueador bloqueia seu caminho!")
    if not fight(player, enemy):
        return False

    # Evento aleatório
    if random() <= 0.4:
        enemy = Enemy(
            "Mercenário Perdido",
            *perform_enemy_creation("hard")
        )
        print("\n⚠️ Um mercenário experiente decide te testar!")
        if not fight(player, enemy):
            return False

    print("\n🏚️ No horizonte, ruínas de uma cidade abandonada surgem...\n")
    sleep(2)
    return True
