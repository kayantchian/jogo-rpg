
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
    def __init__(self):
        self.atk = 100

    def shuriken_laminada(self, enemy):
        damage = self.atk + self.atk*0.40
        enemy.hp -= damage
        print(f"\nVocê usou a shuriken laminada e causou {damage}")
        return damage

    def corte_sombrio(self, enemy):
        damage = self.atk + self.atk * 0.50
        enemy.hp -= damage
        return damage
    SKILLS = [{"name":"Shuriken Laminada", "cost_mana": 15, "skill": shuriken_laminada},
              {"name":"Corte Sombrio", "cost_mana": 25, "skill": corte_sombrio}]


if(__name__ == "__main__"):
    player = Assassino()
    #Upgrade da habiliade
    decorator = upgrade_skill(value=0.3)
    player.shuriken_laminada = decorator(player.shuriken_laminada)

    #Executa a habiliade depois do upgrade
    player.shuriken_laminada()
