from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from player import Player
from mechanics import find_dict_by_value


class Loja():
    
    ITEMS = [{"name" : "Poção de vida", "price": 15, 'limit': 5}, {"name" : "Anjo Guardião", "price" : 100, 'limit': 1}]
    EQUIPAMENTOS = [{"name":"Lâmina de Doran", "price":135, "atk" : 20, "den" : 0, 'limit': 1}, {"name":"Escudo de Doran", "price":105, "atk" : 0, "den" : 25, 'limit': 1}]
    
    def menu(self, categoria) -> dict:
        op = True
        while(op):
            if(categoria=="Itens Mágicos"):                    
                selected_item = inquirer.select(
                    message="Selecione um item mágico\n",
                    choices=[f"{item['name']}: ${item['price']}" for item in Loja.ITEMS]).execute()
                selected_item = selected_item.split(":", 1)  #get name of item in string
                item = find_dict_by_value(Loja.ITEMS, "name",selected_item[0])
                return item
            
            if(categoria=="Equipamentos"):
                selected_item = inquirer.select(
                    message="Selecione um item",
                    choices=[f"{item['name']}: ${item['price']}" for item in Loja.EQUIPAMENTOS]).execute()
                selected_item = selected_item.split(":", 1)  #get name of item in string
                item = find_dict_by_value(Loja.EQUIPAMENTOS, "name",selected_item[0])
                return item
if(__name__ == "__main__"):
    Loja = Loja()
    print(Loja.menu("Itens Mágicos"))