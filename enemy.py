from player import Personagem
from random import randint

def perform_enemy_creation(enemy_level):
    if(enemy_level == "normal"):
        hp = randint(150,200)
        atk = randint(15,25)
        den = randint(10,20)
        xp = randint(10,20)
        money = randint(7,14)
        return hp, atk, den, xp, money
    elif(enemy_level == "hard"):
        hp = randint(250,400)
        atk = randint(25,40)
        den = randint(20,30)
        xp = randint(20,50)
        money = randint(25,50)
        return hp, atk, den, xp, money
    elif(enemy_level== "easy"):
        hp = randint(70,100)
        atk = randint(9,15)
        den = randint(9,15)
        xp = randint(5,10)
        money = randint(1,7)
        return hp, atk, den, xp, money

class Enemy(Personagem):
    def __init__(self, name, hp, atk, den, xp, money, critical = 0):
        super().__init__(hp, atk, den, name)
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
            

FLORESTA = []

ESTRADA_ANTIGA = []

CIDADE_ABANDONADA = []
    