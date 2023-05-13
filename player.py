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
        self.__money = 0
        self.__xp = 10
        self.__inventory = []
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

    
    #Show player's inventory
    def invent(self):
        if len(self.inventory)>0:
            for item in self.inventory:
                print(f"{item}")
        else:
            print("\nVocê não tem itens no inventário.\n")
                         
    
    def fight(self,enemy):
        print(f"\n Um(a) {enemy.name} se aproxima!\n")
        sleep(1)
        turn = random.choice([True, False])
        while enemy.hp > 0:
            turn = not turn
            print(f"\n{enemy.name}: {enemy.hp} HP", end="\n")
            print(f"Você: {self.hp} HP", end="\n")
            print("", end="\n")
            sleep(1.5)
            #Player's turn
            if(turn == True):
                sleep(1)
                player_choice = inquirer.select(
        message="Selecione uma opção:",
        choices=["Atacar","Item","Passar a vez", "Fugir"],
    ).execute()
                if(player_choice == "Atacar"):
                    if(self.atk > enemy.den):
                        print(f"\nVocê causou {self.atk} de dano!", end="\n")
                        enemy.hp = enemy.hp - self.atk
                        print(f"{enemy.name}: {enemy.hp} HP", end="\n")
                    else:
                        print(f"\nSeu ataque não causou dano em {enemy.name}", end="\n")
                        enemy.den -= self.atk
                        print(f"Mas a defesa de {enemy.name} foi reduzida para {enemy.den}")
                
                elif(player_choice == "Fugir"):
                    if random.random() <= 0.25:
                        print('\nVocê conseguiu fugir!', end="\n")
                        sleep(2)
                        break
                    else:
                        print(f'\n{enemy.name} bloqueou a sua fuga.', end="\n")
                elif(player_choice == "Passar a vez"):
                    pass
                
            #Enemy's turn        
            elif(turn == False):
                sleep(1)
                if(enemy.atk > self.den):
                    print(f"\n{enemy.name} te atacou! {enemy.atk} de dano\n", end="\n")
                    self.hp -= enemy.atk
                else:
                    self.den -= enemy.atk
                    print(f"\nO ataque de {enemy.name} não teve efeito.", end="\n")
                    sleep(0.5)
                    print(f"Mas sua defesa foi reduzida para {self.den}")
            #Verifies if player is dead
            if self.hp <= 0:
                for x in range(1, 10):
                    print("==", end="", flush=True)
                    sleep(0.1)
                for char in "\n\n     GAME OVER      \n\n":
                    print(char, end="", flush=True)
                    sleep(0.1)
                for x in range(1, 10):
                    print("==", end="", flush=True)
                    sleep(0.1)
                break
        #Verifies if enemy is dead:
        if enemy.hp <= 0:
            print(f"\n{enemy.name} morreu!")
            self.xp += enemy.xp
            print(f'{enemy.xp} pontos de xp adquiridos! Atual: {self.xp}' , end="\n")           
                
                
    def comprar_item(self, item):
        if(self.money >= item['price']):
            self.money -= item['price']
            self.inventory.append(item['name'])
            self.invent()
        else:
            print(f"\n[!] Saldo insuficiente: {self.money}\n")

    
      
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
        atk = 15
        den = 22
        return Player(hp, atk, den, name, age, classe)
    elif(classe=="Orc"):
        hp = 250
        atk = 25
        den = 12
        return Player(hp, atk, den, name, age, classe)
    

