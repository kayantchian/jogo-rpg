from time import sleep


'''
def upgrade_skill(value):
    def decorator(skill):
        def wrapper(*args, **kwargs):
            resultado = skill(*args, **kwargs)
            damage = resultado
            bost_damage = damage + damage*value
            return bost_damage
        return wrapper
    return decorator'''

class Assassino():
    def shuriken_laminada(player) -> float:
        damage = player.atk + player.atk*0.20
        damage_ex = damage + damage*0.20
        total = damage_ex + damage
        sleep(1)
        print(f"\nVocê avança no inimigo e lança sua \nshuriken que o acerta...")
        sleep(1.5)
        print(f"ela retorna rapidamente na direção do alvo, \nacertando-o novamente e causando {damage_ex} !\n")
        sleep(2.5)
        return total
    def corte_sombrio(player) -> float:
        damage = player.atk + player.atk * 0.50
        sleep(1)
        print(f"\nVocê atravesa o inimigo com seu corte sombrio!\n")
        sleep(1)
        return damage
    def marca_fatal(player):
        damage = player.atk + player.atk * 0.75
        sleep(1)
        print(f"\nVocê avança e marca o inimigo com sua lâmina, e a \nmarca causa uma explosão imensa no local marcado!\n")
        sleep(1)
        return damage   
    SKILLS = [{"name":"Shuriken Laminada", "cost_mana": 15, "skill": shuriken_laminada},
              {"name":"Corte Sombrio", "cost_mana": 20, "skill": corte_sombrio},
              {"name":"Marca Fatal", "cost_mana": 35, "skill": marca_fatal}]

class Clerigo():
    def __init__(player):
        player.magic_atk = 10
        
    def exorcismo(player) -> float:
        damage = player.magic_atk + player.magic_atk*0.40
        sleep(1)
        print(f"\nVocê força o inimigo ajoelhar-se e com seu crucifixo\ncomeça a exorcizá-lo, deixando-o fraco e sem energia...")
        sleep(1)
        return damage
    def confissao_sacerdotal(player) -> float:
        damage = player.magic_atk + player.magic_atk * 0.60
        sleep(1)
        print(f"\nCom sua influência divina, você faz com que o inimigo se sinta \noprimido e confesse suas fraquezas, te dando mais chance de atacar!")
        sleep(1)
        return damage
    def tribunal_inquisidor(player) -> float:
        damage = player.magic_atk + player.magic_atk * 1.15
        sleep(1)
        print(f"\nVocê usa toda sua aura de virtude para canalizar \numa grande bola de fogo. Ela é lançada no infiel o inimigo\n")
        sleep(2)
        return damage
           
    SKILLS = [{"name":"Exorcismo", "cost_mana": 15, "skill": exorcismo},
              {"name":"Confissão Sacerdotal","cost_mana": 20, "skill": confissao_sacerdotal},
              {"name":"Tribunal Inquisidor","cost_mana": 45, "skill": tribunal_inquisidor}]

class Bebado():
    def shuriken_laminada(player) -> float:
        damage = player.atk + player.atk*0.40
        
        sleep(1)
        print(f"\nVocê usou a Shuriken Laminada e causou {damage}!\n")
        sleep(1)
        return damage
    def corte_sombrio(player) -> float:
        damage = player.atk + player.atk * 0.50
        
        sleep(1)
        print(f"\nVocê usou o Corte Sombrio e causou {damage}!\n")
        sleep(1)
        return damage
    def marca_fatal(player) -> float:
        damage = player.atk + player.atk * 0.75
        
        sleep(1)
        print(f"\nVocê usou a Marca Fatal e causou {damage}!\n")
        sleep(1)
        return damage   
    SKILLS = [{"name":"Shuriken Laminada", "cost_mana": 15, "skill": shuriken_laminada},
              {"name":"Corte Sombrio","cost_mana": 20, "skill": corte_sombrio},
              {"name":"Marca Fatal", "cost_mana": 35, "skill": marca_fatal}]


if(__name__ == "__main__"):
    class A():
        def __init__(self):
            self.magic_atk = 10
    b = Clerigo()
    dano = b.confissao_sacerdotal()
