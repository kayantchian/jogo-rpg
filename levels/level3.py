from character.player import *
from character.enemy import *
from mechanics import *
from random import random, randint
from time import sleep

def level3(player):
    print("\n🏚️ A Cidade Abandonada exala morte e silêncio absoluto...\n")
    sleep(2)

    # Evento psicológico
    if random() <= 0.5:
        print("\nSussurros ecoam pelas ruas vazias...")
        sleep(1.5)
        dmg = randint(5, 15)
        print(f"A pressão mental te causa {dmg} de dano.")
        player.hp -= dmg

    # Pré-boss
    enemy = Enemy(
        "Guardião Esquecido",
        *perform_enemy_creation("hard")
    )

    print("\n🛡️ Um Guardião ancestral desperta!")
    if not fight(player, enemy):
        return False

    sleep(2)

    # Boss final
    boss = Enemy(
        "Arconte da Ruína",
        *perform_enemy_creation("hard"),
        critical=30
    )

    print("""
🔥 Das profundezas da cidade, uma entidade surge...
🔥 O Arconte da Ruína encara você.
    """)

    if not fight(player, boss):
        return False

    print("""
🏆 O Arconte cai.
A maldição da região é quebrada.
Você sobreviveu.
    """)
    sleep(2)

    return True
