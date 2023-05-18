from player import Personagem
from random import randint, choice

def perform_enemy_creation(enemy_level) -> object:
    if(enemy_level == "normal"):
        hp = randint(150,200)
        magic_atk = randint(7,10)
        atk = randint(15,25)
        den = randint(10,20)
        magic_den = randint(5,10)
        xp = randint(10,20)
        money = randint(7,14)
        critical_atk = randint(0,10)
        return hp, atk, magic_atk, den, magic_den, xp, money, critical_atk
    elif(enemy_level == "hard"):
        hp = randint(250,400)
        atk = randint(25,40)
        magic_atk = randint(10,25)
        den = randint(20,30)
        magic_den = randint(10,25)
        xp = randint(20,50)
        money = randint(25,50)
        critical_atk = randint(0,25)
        return hp, atk, magic_atk, den, magic_den, xp, money, critical_atk
    elif(enemy_level == "easy"):
        hp = randint(70,100)
        magic_atk = randint(7,10)
        atk = randint(9,15)
        den = randint(9,15)
        magic_den = randint(10,15)
        xp = randint(5,10)
        money = randint(1,7)
        return hp, atk, magic_atk, den, magic_den, xp, money

class Enemy(Personagem):
    def __init__(self, name, hp, atk, magic_atk, den, magic_den, xp, money, critical = 0):
        super().__init__(hp, atk, den, magic_atk, magic_den, name)
        self.__name = name
        self.__xp = xp
        self.__money = money
        self.__critical_atk = critical
        
    @property
    def critical_atk(self):
        return self.__critical_atk
    @property
    def name(self):
        return self.__name
    @property 
    def xp(self):
        return self.__xp
    @property
    def money(self):
        return self.__money

ENEMY_CHOICES = ["atk", "magic_atk"]            
ENEMY_LEVELS = ['easy','normal']

ENEMY_FLORESTA = ["Gárgula", "Ogro", "Troll", "Ciclope", "Gnol", "Goblin", "Kobolds"]

ENEMY_ESTRADA_ANTIGA = []

ENEMY_CIDADE_ABANDONADA = []

if(__name__ == "__main__"):
    enemy = Enemy(choice(ENEMY_FLORESTA), *perform_enemy_creation("hard"))
    print(enemy.name)
    print(enemy.critical_atk)
    