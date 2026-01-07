from character.player import *
from character.enemy import *
from mechanics import *
from InquirerPy import inquirer
from random import choice, random, randint
from time import sleep
from levels.quests import *

def level1(player):
    print("\n🌲 Você adentra a Floresta Negra. O ar é úmido e pesado...\n")
    sleep(2)

    enemy = Enemy(
        choice(ENEMY_FLORESTA),
        *perform_enemy_creation(choice(ENEMY_LEVELS))
    )

    if not fight(player, enemy):
        return False

    print(f"\nApós derrotar {enemy.name}, você sente o corpo relaxar.")
    player.hp += 30
    print(f"Você recupera 30 de HP. HP atual: {player.hp}")
    sleep(1.5)

    # Quest opcional
    if random() <= 0.75:
        quest_carlos(player)
        print("\nVocê segue mais atento após ajudar o viajante...\n")
        sleep(1.5)

    # Emboscada
    if random() <= 0.50:
        enemy = Enemy(
            choice(ENEMY_FLORESTA),
            *perform_enemy_creation("normal")
        )
        crit = randint(5, 12)
        print(f"\n⚠️ Um {enemy.name} surge das sombras e ataca!")
        print(f"Dano crítico recebido: {crit}")
        player.hp -= crit
        sleep(1)

        if not fight(player, enemy):
            return False

    print("\n🌙 Ao anoitecer, você avista uma estrada antiga ao longe...\n")
    sleep(2)
    return True
