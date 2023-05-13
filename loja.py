from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from player import Player

def find_dict_by_value(items, key, value):
    for item in items:
        if item.get(key) == value:
            return item
    return None

class Loja():
    
    ITEMS = [{"name" : "Poção", "price": 5}, {"name" : "Anjo Guardião", "price" : 150}]
    EQUIPAMENTOS = [{"name":"Lâmina de Doran", "price":45}, {"name":"Escudo de Doran", "price":35}]
    
    def menu(self) -> int:
        op = True
        while(op):
            op = inquirer.select(
                message="Selecione uma opção da Loja:",
                choices=["Items","Equipamentos",Choice(value=False, name="Sair"), ]).execute()
            
            if(op=="Items"):                    
                selected_item = inquirer.select(
                    message="Selecione um item\n",
                    choices=[f"{item['name']}: ${item['price']}" for item in Loja.ITEMS]).execute()
                selected_item = selected_item.split(":", 1)  #get name of item in string
                item = find_dict_by_value(Loja.ITEMS, "name",selected_item[0])
                return item
            
            if(op=="Equipamentos"):
                selected_item = inquirer.select(
                    message="Selecione um item",
                    choices=[f"{item['name']}: ${item['price']}" for item in Loja.EQUIPAMENTOS]).execute()
                selected_item = selected_item.split(":", 1)  #get name of item in string
                item = find_dict_by_value(Loja.EQUIPAMENTOS, "name",selected_item[0])
                return item
            
if(__name__ == "__main__"):
    Loja = Loja()
    print(Loja.menu())