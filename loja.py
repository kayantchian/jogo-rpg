from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from player import Player
from mechanics import find_dict_by_value
from items import Items
from time import sleep

class Loja():
    def menu(self, categoria) -> dict:
        op = True
        while(op):
            if(categoria=="Itens"): 
                sleep(0.5)
                print("", end="\n") 
                choices =  [f"{item['name']}:    ${item['price']}" for item in Items.ITEMS] + ["Voltar"]
                selected = inquirer.select(
                    message="Selecione um item mágico\n",
                    choices= choices).execute()
                if(selected!="Voltar"):
                    selected = selected.split(":", 1)  #get name of item in string
                    item = find_dict_by_value(Items.ITEMS, "name",selected[0])
                    return item
                else:
                    return False
            if(categoria=="Armadura"):
                sleep(0.5)
                print("", end="\n") 
                choices = [f"{item['name']}:    ${item['price']}    --> DEF: {item['den']} RESISTÊNCIA MÁGICA: {item['magic_den']}" for item in Items.EQUIPAMENTOS] + ["Voltar"]
                selected = inquirer.select(
                    message="Selecione um item",
                    choices= choices).execute()
                if(selected!="Voltar"):
                    selected = selected.split(":", 1)  #get name of item in string
                    item = find_dict_by_value(Items.EQUIPAMENTOS, "name",selected[0])
                    return item
                else:
                    return False
            if(categoria=="Escudos"):
                sleep(0.5)
                print("", end="\n") 
                choices = [f"{item['name']}:    ${item['price']}    --> DEF: {item['den']} RESISTÊNCIA MÁGICA: {item['magic_den']}" for item in Items.ESCUDOS] + ["Voltar"]
                selected = inquirer.select(
                    message="Selecione um item",
                    choices= choices).execute()
                if(selected!="Voltar"):
                    selected = selected.split(":", 1)  #get name of item in string
                    item = find_dict_by_value(Items.ESCUDOS, "name",selected[0])
                    return item
                else:
                    return False
            if(categoria=="Armas"):
                sleep(0.5)
                print("", end="\n") 
                choices = [f"{item['name']}:    ${item['price']}    --> ATK: {item['atk']} MAGIC ATK: {item['magic_atk']} " for item in Items.ARMAS] + ["Voltar"]
                selected = inquirer.select(
                    message="Selecione um item",
                    choices=choices).execute()
                if(selected!="Voltar"):
                    selected = selected.split(":", 1)  #get name of item in string
                    item = find_dict_by_value(Items.ARMAS, "name",selected[0])
                    return item
                else:
                    return False
            if(categoria=="Armas Mágicas"):
                sleep(0.5)
                print("", end="\n") 
                choices = [f"{item['name']}:    ${item['price']}    --> MAGIC ATK:{item['magic_atk']} ATK: {item['atk']}" for item in Items.MAGICOS] + ["Voltar"]
                selected = inquirer.select(
                    message="Selecione um item",
                    choices=choices).execute()
                if(selected!="Voltar"):
                    selected = selected.split(":", 1)  #get name of item in string
                    item = find_dict_by_value(Items.MAGICOS, "name",selected[0])
                    return item
                else:
                    return False
            
if(__name__ == "__main__"):
    Loja = Loja()
    (Loja.menu("Armas"))