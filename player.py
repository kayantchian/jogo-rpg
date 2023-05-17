from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from time import sleep
import random
from items import Items

class Personagem():
    def __init__(self, hp, atk, den, magic_den, name):
        self.__MAX_HP = hp
        self.__hp = hp
        self.__atk = atk
        self.__den = den
        self.__NAME = name
        self.__magic_den = magic_den
        self.__MAX_DEN = den
        self.__MAGIC_MAX_DEN = magic_den
    @property
    def MAGIC_MAX_DEN(self):
        return self.__MAGIC_MAX_DEN     
    @property
    def MAX_DEN(self):
        return self.__MAX_DEN          
    @property
    def magic_den(self):
        return self.__magic_den
    @magic_den.setter
    def magic_den(self, new_den):
        if new_den > 0 & new_den < self.MAGIC_MAX_DEN:
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
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, new_hp):
        if new_hp > 0 & new_hp < self.MAX_HP:
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
        if new_den > 0 & new_den < self.MAX_DEN:
            self.__den = new_den       
        elif new_den >= self.MAX_DEN:
            self.__den = self.MAX_DEN
        elif new_den <= 0:
            self.__den = 0
            
class Player(Personagem):
    def __init__(self, hp, atk, den, magic_den, name, age, classe):
        super().__init__(hp, atk, den, magic_den, name)
        self.__mana = 10
        self.__AGE = age
        self.__CLASS = classe
        self.__money = 950
        self.__xp = 10
        self.__MAX_MANA = self.__mana
        self.__magic_items = Items.BASIC_MAGIC_ITEMS 
        self.__inventory = Items.BASIC_ITEMS
        self.__equip = Items.BASIC_EQUIP   
        self.__weapons = Items.BASIC_WEAPONS

    @property
    def weapons(self):
        return self.__weapons
    @property
    def MAX_MANA(self):
        return self.__MAX_MANA
    @property
    def magic_items(self):
        return self.__magic_items
    @property   
    def mana(self):
        return self.__mana
    @mana.setter
    def mana(self, new_mana):
        if(new_mana > 0 & new_mana < self.MAX_MANA):
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

    #Calculates the bonus attack from player's equipament
    def bonus_atk(self) -> int:
        if len(self.equip)>0 or len(self.weapons)>0:
           re1 = sum([equip['atk'] for equip in self.equip])
           re2 = sum([weapon['atk'] for weapon in self.weapons])
           return re1 + re2
        else:
            return 0
    #Calculates the bonus magical atk from player's equipament
    def magic_atk(self) -> int:
        if len(self.magic_items)>0  or len(self.weapons)>0:
            re1 = sum([magic_equip['magic_atk'] for magic_equip in self.magic_items])
            re2 = sum([weapon['magic_atk'] for weapon in self.weapons])
            return re1 + re2
        else:
            return 0
    #Calculates the bonus attack from player's equipament
    def bonus_den(self) -> int:
        if len(self.equip)>0 or len(self.weapons)>0:
            re1 = sum([equip['den'] for equip in self.equip])
            re2 = sum([weapon['den'] for weapon in self.weapons])
            return re1 + re2
        else:
            return 0
    def bonus_magic_den(self) -> int:
        if len(self.magic_items)>0 or len(self.weapons)>0:
            re1 = sum([equip['magic_atk'] for equip in self.magic_items])
            re2 = sum([weapon['magic_atk'] for weapon in self.weapons])
            return re1 + re2
        else:
            return 0
     
    def recuperacao_mana(self):
        if(self.mana < self.MAX_MANA):
            self.mana += 1
            
    #Show player's status
    def status(self):
        print(f"""\n --- Você ---
                | HP: {self.hp}
                | MANA: {self.mana}
                | ATK: {self.atk}
                | MAGIC: {self.magic_atk()}
                | DEF: {self.den}
                | RESISTÊNCIA MÁGICA: {self.magic_den}""")
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
        sleep(2)
        if len(self.equip)>0 or len(self.magic_items)>0 or len(self.weapons)>0:
            print("\n=== EQUIPAMENTO ===\n")
            for equip in self.equip:
                print(f"   {equip['name']}   ")
            for magic in self.magic_items:
                print(f"   {magic['name']}   ")
            for weapon in self.weapons:
                print(f"   {weapon['name']}   ")
            print("\n=================\n")
        else:
            sleep(1.5)
            print("\nVocê não tem itens equipados.\n")

                                    
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
                self.equipament()
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
                self.equipament()
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
            "Orc",
            ],validate=lambda selection: len(selection) >= 1,
    invalid_message="Selecione uma opção!",
    ).execute()
    if(classe == "Humano"):
        hp = 100
        atk = 10
        den = 17
        magic_den = 10
        return Player(hp, atk, den, magic_den, name, age, classe)
    elif(classe=="Orc"):
        hp = 150
        atk = 15
        den = 10
        magic_den = 10
        return Player(hp, atk, den, magic_den, name, age, classe)
    
if(__name__ == "__main__"):
    magic_items = [{"name":"Lâmina de lumen", "price":0, "magic_atk" : 10, "magic_den" : 0, "cost_mana": 10, 'limit': 1}]
    def bonus_atk(lista) -> int:
        if len(lista)>0:
            return sum([equip['magic_atk'] for equip in lista])
        else:
            return 0
    print(bonus_atk(magic_items))