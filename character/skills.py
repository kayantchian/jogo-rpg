from time import sleep

def upgrade_skill(value):
    def decorator(skill):
        def wrapper(*args, **kwargs):
            resultado = skill(*args, **kwargs)
            damage = resultado
            bost_damage = damage + damage*value
            return bost_damage
        return wrapper
    return decorator

class Assassino():
    def shuriken_laminada(player, enemy):
        damage = player.atk + player.atk*0.40
        enemy.hp -= damage
        sleep(0.5)
        print(f"\nVocê usou a Shuriken Laminada e causou {damage}!\n")
        sleep(1)
        return damage
    def corte_sombrio(player, enemy):
        damage = player.atk + player.atk * 0.50
        enemy.hp -= damage
        sleep(0.5)
        print(f"\nVocê usou o Corte Sombrio e causou {damage}!\n")
        sleep(1)
        return damage
    def marca_fatal(player, enemy):
        damage = player.atk + player.atk * 0.75
        enemy.hp -= damage
        sleep(0.5)
        print(f"\nVocê usou a Marca Fatal e causou {damage}!\n")
        sleep(1)
        return damage   
    SKILLS = [{"name":"Shuriken Laminada", "cost_mana": 15, "skill": shuriken_laminada},
              {"name":"Corte Sombrio", "cost_mana": 20, "skill": corte_sombrio},
              {"name":"Marca Fatal", "cost_mana": 35, "skill": marca_fatal}]

class Clerigo():
    def exorcismo_estiloso(player, enemy):
        damage = player.atk + player.atk*0.40
        enemy.hp -= damage
        sleep(0.5)
        print(f"""\nVocê força {enemy.name} ajoelhar-se e com seu crucifixo
        começa a exorcizá-lo, deixando-o fraco e sem energia...""")
        sleep(0.7)
        print(f"\nSeu ataque causou {damage}!\n")
        sleep(1)
        return damage
    def confissao_sacerdotal(player, enemy):
        damage = player.atk + player.atk * 0.50
        enemy.hp -= damage
        sleep(0.5)
        print(f"""\nCom sua influência divina, você faz com que {enemy.name} se sinta
        oprimido e confesse suas fraquezas, te dando mais chance de atacar!""")
        sleep(0.7)
        print(f"Seu ataque causou {damage}!\n""")
        sleep(1)
        return damage
    def tribunal_inquisicao(player, enemy):
        damage = player.atk + player.atk * 0.75
        enemy.hp -= damage
        sleep(0.5)
        print(f"\nVocê usou a Marca Fatal e causou {damage}!\n")
        sleep(1)
        return damage   
    SKILLS = [{"name":"Shuriken Laminada", "cost_mana": 15, "skill": shuriken_laminada},
              {"name":"Corte Sombrio", "cost_mana": 20, "skill": corte_sombrio},
              {"name":"Marca Fatal", "cost_mana": 35, "skill": marca_fatal}]
class Assassino():
    def shuriken_laminada(player, enemy):
        damage = player.atk + player.atk*0.40
        enemy.hp -= damage
        sleep(0.5)
        print(f"\nVocê usou a Shuriken Laminada e causou {damage}!\n")
        sleep(1)
        return damage
    def corte_sombrio(player, enemy):
        damage = player.atk + player.atk * 0.50
        enemy.hp -= damage
        sleep(0.5)
        print(f"\nVocê usou o Corte Sombrio e causou {damage}!\n")
        sleep(1)
        return damage
    def marca_fatal(player, enemy):
        damage = player.atk + player.atk * 0.75
        enemy.hp -= damage
        sleep(0.5)
        print(f"\nVocê usou a Marca Fatal e causou {damage}!\n")
        sleep(1)
        return damage   
    SKILLS = [{"name":"Shuriken Laminada", "cost_mana": 15, "skill": shuriken_laminada},
              {"name":"Corte Sombrio", "cost_mana": 20, "skill": corte_sombrio},
              {"name":"Marca Fatal", "cost_mana": 35, "skill": marca_fatal}]


if(__name__ == "__main__"):
    player = Assassino()
    #Upgrade da habiliade
    decorator = upgrade_skill(value=0.3)
    player.shuriken_laminada = decorator(player.shuriken_laminada)

    #Executa a habiliade depois do upgrade
    player.shuriken_laminada()
