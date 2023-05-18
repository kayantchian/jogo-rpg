from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from InquirerPy.base.control import Choice
from time import sleep
import random
from items import Items

class Personagem():
    def __init__(self, hp, atk, den, magic_atk, magic_den, name):
        self.__MAX_HP = hp
        self.__hp = hp
        self.__atk = atk
        self.__den = den
        self.__NAME = name
        self.__magic_atk = magic_atk
        self.__magic_den = magic_den
        self.__MAX_DEN = den
        self.__MAGIC_MAX_DEN = magic_den
        
    @property
    def MAGIC_MAX_DEN(self):
        return self.__MAGIC_MAX_DEN  
    @MAGIC_MAX_DEN.setter
    def MAGIC_MAX_DEN(self, new_magic_den):
        self.__MAGIC_MAX_DEN = new_magic_den
    @property
    def MAX_DEN(self):
        return self.__MAX_DEN    
    @MAX_DEN.setter
    def MAX_DEN(self, new_den):
        self.__MAX_DEN = new_den
    @property 
    def magic_atk(self):
        return self.__magic_atk
    @magic_atk.setter
    def magic_atk(self, new_atk):
        self.__magic_atk=new_atk
    @property
    def magic_den(self):
        return self.__magic_den
    @magic_den.setter
    def magic_den(self, new_den):
        if new_den > 0 and new_den < self.MAGIC_MAX_DEN:
            self.__magic_den = new_den       
        elif new_den >= self.MAGIC_MAX_DEN:
            self.__magic_den = self.MAGIC_MAX_DEN
        elif new_den <= 0:
            self.__magic_den = 0
    @property
    def name(self):
        return self.__NAME           
    @property
    def MAX_HP(self):
        return self.__MAX_HP
    @MAX_HP.setter
    def MAX_HP(self, new_hp):
        self.__MAX_HP = new_hp
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, new_hp):
        if new_hp > 0 and new_hp < self.MAX_HP:
            self.__hp = new_hp
        elif new_hp <= 0:
            self.__hp = 0
        elif new_hp >= self.MAX_HP:
            self.__hp = self.MAX_HP     
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self, new_atk):
        if new_atk >= 0:
            self.__atk = new_atk
        else: 
            self.__atk = 0
    @property
    def den(self):
        return self.__den
    @den.setter
    def den(self, new_den):
        if new_den > 0 and new_den < self.MAX_DEN:
            self.__den = new_den       
        elif new_den >= self.MAX_DEN:
            self.__den = self.MAX_DEN
        elif new_den <= 0:
            self.__den = 0
            
class Player(Personagem):
    def __init__(self, hp, atk, den, magic_atk, magic_den, name, age, classe):
        super().__init__(hp, atk, den, magic_atk, magic_den, name)
        #Player's stats
        self.__level = 1
        self.__mana = 10
        self.__AGE = age
        self.__CLASS = classe
        self.__money = 0
        self.__xp = 0
        self.__MAX_MANA = self.__mana
        #Player's equipament and weapons/shield
        self.__magic_weapons = Items.BASIC_MAGIC_WEAPONS 
        self.__inventory = Items.BASIC_ITEMS
        self.__equip = Items.BASIC_EQUIP   
        self.__weapons = Items.BASIC_WEAPONS
        self.__shields = Items.BASIC_SHIELDS
    
    @property
    def shields(self):
        return self.__shields
    @property
    def weapons(self):
        return self.__weapons
    @property
    def MAX_MANA(self):
        return self.__MAX_MANA
    @MAX_MANA.setter
    def MAX_MANA(self, new_mana):
        self.__MAX_MANA = new_mana
    @property
    def magic_weapons(self):
        return self.__magic_weapons
    @property   
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self, new_mana):
        if(new_mana > 0 and new_mana < self.MAX_MANA):
            self.__mana = new_mana
        elif(new_mana <= 0):
            self.__mana = 0
        elif(new_mana >= self.MAX_MANA):
            self.__mana = self.MAX_MANA
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
        if(new_money>0):
            self.__money = new_money 
        else:
            self.__money = 0
    @property
    def xp(self):
        return self.__xp
    @xp.setter
    def xp(self, new_xp):
        self.__xp = new_xp
    @property
    def classe(self):
        return self._CLASS  

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, new_level):
        self.__level = new_level
    
    #level up
    def level_up(self):
        if self.xp >= 0 and self.xp <= 100:
            self.level = 1
        elif self.xp > 100 and self.xp <= 200:
            self.level = 2
            self.MAX_HP += self.MAX_HP*0.5
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += 10
            self.MAX_MANA += 10
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 200 and self.xp <= 300:
            self.level = 3
            self.atk += self.atk*0.3
            self.MAX_HP += self.MAX_HP*0.5
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 300 and self.xp <= 400:
            self.level = 4
            self.MAX_HP += self.MAX_HP*0.75
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 400 and self.xp <= 500:
            self.level = 5
            self.MAX_HP += self.MAX_HP*0.75
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 500 and self.xp <= 600:
            self.level = 6
            self.MAX_HP += self.MAX_HP*0.75
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 600 and self.xp <= 700:
            self.level = 7
            self.MAX_HP += self.MAX_HP*0.75
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 700 and self.xp <= 800:
            self.level = 8
            self.MAX_HP += self.MAX_HP*0.75
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 800 and self.xp <= 900:
            self.level = 9
            self.MAX_HP += self.MAX_HP*0.80
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")
        elif self.xp > 900 and self.xp <= 1000:
            self.level = 10
            self.MAX_HP += self.MAX_HP
            self.atk += self.atk*0.3
            self.MAX_DEN += self.MAX_DEN * 0.3
            self.magic_atk += self.magic_atk * 0.2
            self.MAX_MANA += self.MAX_MANA*0.5
            print(f"[!] você subiu de nível: {self.level}")

    
    #Calculates the bonus attack from player's equipament
    def bonus_atk(self) -> int:
        if len(self.equip)>0 or len(self.shields)>0:
           equip = sum([equip['atk'] for equip in self.equip])
           shield = sum([shield['atk'] for shield in self.shields])
           return shield + equip
        else:
            return 0
    #Calculates the bonus magical atk from player's equipament
    def bonus_magic_atk(self) -> int:
        if len(self.equip)>0 or len(self.shields)>0:
            equip = sum([equip['magic_atk'] for equip in self.equip])
            shield = sum([shield['magic_atk'] for shield in self.shields])
            return shield + equip
        else:
            return 0
        
    #Calculates the bonus defense from player's equipament
    def bonus_den(self) -> int:
        #if len(self.equip)>0 or len(self.weapons)>0 or len(self.magic_weapons)>0 or len(self.shields)>0:
        if len(self.equip)>0 or len(self.shields)>0:
            equip = sum([equip['den'] for equip in self.equip])
            #magic = sum([magic_equip['den'] for magic_equip in self.magic_weapons])
            #weapon = sum([weapon['den'] for weapon in self.weapons])
            shield = sum([shield['den'] for shield in self.shields])
            return shield + equip
        else:
            return 0
        
     #Calculates the bonus magical defense from player's equipament   
    def bonus_magic_den(self) -> int:
        #if len(self.equip)>0 or len(self.weapons)>0 or len(self.magic_weapons)>0 or len(self.shields)>0:
        if len(self.equip)>0 or len(self.shields)>0:
            equip = sum([equip['magic_den'] for equip in self.equip])
            #magic = sum([magic_equip['magic_den'] for magic_equip in self.magic_weapons])
            #weapon = sum([weapon['magic_den'] for weapon in self.weapons])
            shield = sum([shield['magic_den'] for shield in self.shields])
            return shield + equip
        else:
            return 0
     
    def recuperacao_mana(self):
        if(self.mana < self.MAX_MANA):
            self.mana += self.MAX_MANA*0.2
            
    #Show player's status
    def status(self):
        print(f"""\n --- Você ---
                | LEVEL: {self.level}
                | HP: {self.hp}
                | MANA: {self.mana}
                | MAGIC ATK: {self.magic_atk} (Bonus: +{self.bonus_magic_atk()})
                | ATK: {self.atk} (Bonus: +{self.bonus_atk()})
                | DEF: {self.den} (Bonus: +{self.bonus_den()})
                | RESISTÊNCIA MÁGICA: {self.magic_den} (Bonus: +{self.bonus_magic_den()})""")
        print("", end="\n")
    
    #Show player's inventory
    def invent(self):
        sleep(0.5)
        if len(self.inventory)>0:
            print("\n=== INVENTÁRIO ===\n")
            for item in self.inventory:
                print(f"   {item['name']}   ")
            print("\n=================\n")
        else:
            sleep(1.5)
            print("\nVocê não tem itens no inventário.\n")
     
     #Show player's equipaments       
    def equipament(self):
        sleep(1)
        print("\n=== EQUIPAMENTO ===\n")
        categoria = inquirer.select(
                    message="Selecione um tipo de equipamento:",
                    choices=["Armadura", "Armas", "Escudos", "Armas Mágicas", Choice(value=False, name="Sair"), ]).execute()
        if(categoria == "Armadura"):
            if(len(self.equip)>0):
                for equip in self.equip:
                    print(f"   {equip['name']} -> DEF {equip['den']} RESISTÊNCIA MÁGICA: {equip['magic_den']}")
            else:
                sleep(1.5)
                print("\nNada aqui..\n")
        if(categoria == "Armas Mágicas"):
            if(len(self.magic_weapons)>0):
                for magic in self.magic_weapons:
                    print(f"   {magic['name']} -> MAGIC ATK:{magic['magic_atk']} ATK {magic['atk']}")
            else:
                sleep(1.5)
                print("\nNada aqui..\n")
        if(categoria == "Armas"):
            if(len(self.weapons)>0):
                for weapon in self.weapons:
                    print(f"   {weapon['name']} -> ATK {weapon['atk']} MAGIC ATK {weapon['magic_atk']}")
            else:
                sleep(1.5)
                print("\nNada aqui.\n")
        if(categoria == "Escudos"):        
            if(len(self.shields)>0):
                for shield in self.shields:
                    print(f"   {shield['name']} -> DEF {shield['den']} RESISTÊNCIA MÁGICA: {shield['magic_den']}")
            else:
                sleep(1.5)
                print("\nNada aqui.\n")
                                    
    def buy_item(self, item):
        print(f"\nSaldo atual: {self.money}\n")
        items_limit = lambda item: sum([1 for equip in self.inventory if equip['name'] == item['name']])
        max_limit = items_limit(item)
        if(max_limit < item['limit']):
            if(self.money >= item['price']):
                self.money -= item['price']
                sleep(1.5)
                print(f"\nVocê comprou {item['name']}", end="\n")
                self.inventory.append(item)
                self.invent()
            else:
                sleep(1)
                print(f"\n[!] Saldo insuficiente, faltam:{item['price'] - self.money}\n moedas")
        else:
            sleep(0.5)
            print(f"\nLimite de compra do item {item['name']} atingido. Máximo: {item['limit']}\n")
                   
    def buy_equip(self, item):
        print(f"\nSaldo atual: {self.money}\n")
        equips_limit = lambda item: sum([1 for equip in self.equip if equip['name'] == item['name']])
        max_limit = equips_limit(item)
        if max_limit < item['limit']:
            if(self.money >= item['price']):
                self.money -= item['price']
                sleep(1.5)
                print(f"\nVocê comprou {item['name']}", end="\n")
                self.equip.append(item)
                
            else:
                sleep(1)
                print(f"\n[!] Saldo insuficiente, faltam:{item['price'] - self.money}\n moedas")
        else:
            sleep(0.5)
            print(f"\nLimite de compra do item {item['name']} atingido. Máximo: {item['limit']}\n")
              
    def buy_weapon(self, item):
        print(f"\nSaldo atual: {self.money}\n")
        equips_limit = lambda item: sum([1 for equip in self.weapons if equip['name'] == item['name']])
        max_limit = equips_limit(item)
        if max_limit < item['limit']:
            if(self.money >= item['price']):
                self.money -= item['price']
                sleep(1.5)
                print(f"\nVocê comprou {item['name']}", end="\n")
                self.weapons.append(item)
                
            else:
                sleep(1)
                print(f"\n[!] Saldo insuficiente, faltam:{item['price'] - self.money}\n moedas")
        else:
            sleep(0.5)
            print(f"\nLimite de compra do item {item['name']} atingido. Máximo: {item['limit']}\n")
              
    def buy_shield(self, item):
        print(f"\nSaldo atual: {self.money}\n")
        equips_limit = lambda item: sum([1 for equip in self.shields if equip['name'] == item['name']])
        max_limit = equips_limit(item)
        if max_limit < item['limit']:
            if(self.money >= item['price']):
                self.money -= item['price']
                sleep(1.5)
                print(f"\nVocê comprou {item['name']}", end="\n")
                self.shields.append(item)
                
            else:
                sleep(1)
                print(f"\n[!] Saldo insuficiente, faltam:{item['price'] - self.money}\n moedas")
        else:
            sleep(0.5)
            print(f"\nLimite de compra do item {item['name']} atingido. Máximo: {item['limit']}\n")
              
    def buy_magic_weapon(self, item):
        print(f"\nSaldo atual: {self.money}\n")
        equips_limit = lambda item: sum([1 for equip in self.magic_weapons if equip['name'] == item['name']])
        max_limit = equips_limit(item)
        if max_limit < item['limit']:
            if(self.money >= item['price']):
                self.money -= item['price']
                sleep(1.5)
                print(f"\nVocê comprou {item['name']}", end="\n")
                self.magic_weapons.append(item)
                
            else:
                sleep(1)
                print(f"\n[!] Saldo insuficiente, faltam:{item['price'] - self.money}\n moedas")
        else:
            sleep(0.5)
            print(f"\nLimite de compra do item {item['name']} atingido. Máximo: {item['limit']}\n")
              
        
      
      
def perform_player_creation() -> object:
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
            "Orc", "Elfo"
            ],validate=lambda selection: len(selection) >= 1,
    invalid_message="Selecione uma opção!",
    ).execute()
    if(classe == "Humano"):
        hp = 100
        atk = 20
        den = 25
        magic_atk = 0
        magic_den = 0
        return Player(hp, atk, den, magic_atk, magic_den, name, age, classe)
    elif(classe=="Orc"):
        hp = 250
        atk = 25
        den = 5
        magic_atk = 0
        magic_den = 5
        return Player(hp, atk, den, magic_atk, magic_den, name, age, classe)
    elif(classe=="Elfo"):
        hp = 100
        atk = 15
        den = 0
        magic_atk = 15
        magic_den = 10
        return Player(hp, atk, den, magic_atk, magic_den, name, age, classe)
    
if(__name__ == "__main__"):
    magic_weapons = [{"name":"Lâmina de lumen", "price":0, "magic_atk" : 10, "magic_den" : 0, "cost_mana": 10, 'limit': 1}]
    def bonus_atk(lista) -> int:
        if len(lista)>0:
            return sum([equip['magic_atk'] for equip in lista])
        else:
            return 0
    print(bonus_atk(magic_weapons))