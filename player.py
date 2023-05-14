from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from time import sleep
import random

class Personagem():
    def __init__(self, hp, atk, den, name):
        self.__MAX_HP = hp
        self.__hp = hp
        self.__atk = atk
        self.__den = den
        self.__NAME = name
        
    @property
    def name(self):
        return self.__NAME     
        
    @property
    def max_hp(self):
        return self.__MAX_HP
    
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, new_hp):
        self.__hp = new_hp
        
    @property
    def atk(self):
        return self.__atk
    
    @atk.setter
    def atk(self, new_atk):
        self.__atk = new_atk
        
    @property
    def den(self):
        return self.__den
    
    @den.setter
    def den(self, new_den):
        self.__den = new_den       

class Player(Personagem):
    def __init__(self, hp, atk, den, name, age, classe):
        super().__init__(hp, atk, den, name)
        self.__AGE = age
        self.__CLASS = classe
        self.__money = 5
        self.__xp = 10
        self.__inventory = []
        self.__equip = []
        
    @property
    def equip(self):
        return self.__equip
    @property
    def inventory(self):
        return self.__inventory
    @inventory.setter
    def inventory(self, new_inventory):
        self.inventory = new_inventory
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, new_money):
        self.__money = new_money 
    @property
    def xp(self):
        return self.__xp
    @xp.setter
    def xp(self, new_xp):
        self.__xp = new_xp
    @property
    def classe(self):
        return self._CLASS  

    def boost_atk(self):
    
    #Show player's inventory
    def invent(self):
        sleep(2)
        if len(self.inventory)>0:
            print("\n=== INVENTÁRIO ===\n")
            for item in self.inventory:
                print(f"   {item}   ")
            print("\n=================\n")
        else:
            sleep(1.5)
            print("\nVocê não tem itens no inventário.\n")
                                    
                
    def buy_item(self, item):
        print(f"\nSaldo atual: {self.money}\n")
        if(self.money >= item['price']):
            self.money -= item['price']
            sleep(1.5)
            print(f"\nVocê comprou {item['name']}", end="\n")
            print(f"\nSaldo atual: {self.money}")
            self.inventory.append(item['name'])
            self.invent()
        else:
            sleep(2)
            print(f"\n[!] Saldo insuficiente, faltam:{item['price'] - self.money}\n moedas")
            
    def buy_equip(self, item):
        print(f"\nSaldo atual: {self.money}\n")
        if(self.money >= item['price']):
            self.money -= item['price']
            sleep(1.5)
            print(f"\nVocê comprou {item['name']}", end="\n")
            print(f"\nSaldo atual: {self.money}")
            self.equip.append(item['name'])
            self.invent()
        else:
            sleep(2)
            print(f"\n[!] Saldo insuficiente, faltam:{item['price'] - self.money}\n moedas")
            
    
      
      #Abstract function
def perform_player_creation():
    name = inquirer.text(
        message="Nome:",
        validate=lambda result: len(result) > 0,
        invalid_message="O nome não pode ser vazio!",
    ).execute()
    age = integer_val = inquirer.number(
        message="Idade:",
        min_allowed=18,
        max_allowed=60,
        validate=EmptyInputValidator(),
    ).execute()
    classe = inquirer.select(
        message="Classe:",
        choices=[
            "Humano",
            "Orc",
            ],validate=lambda selection: len(selection) >= 1,
    invalid_message="Selecione uma opção!",
    ).execute()
    if(classe == "Humano"):
        hp = 100
        atk = 10
        den = 17
        return Player(hp, atk, den, name, age, classe)
    elif(classe=="Orc"):
        hp = 150
        atk = 15
        den = 10
        return Player(hp, atk, den, name, age, classe)
    

