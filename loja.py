from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from player import Player
from mechanics import find_dict_by_value
from items import Items

class Loja():
    def menu(self, categoria) -> dict:
        op = True
        while(op):
            if(categoria=="Itens Mágicos"):                    
                selected_item = inquirer.select(
                    message="Selecione um item mágico\n",
                    choices=[f"{item['name']}: ${item['price']}" for item in Items.ITEMS]).execute()
                selected_item = selected_item.split(":", 1)  #get name of item in string
                item = find_dict_by_value(Items.ITEMS, "name",selected_item[0])
                return item
            if(categoria=="Equipamentos"):
                selected_item = inquirer.select(
                    message="Selecione um item",
                    choices=[f"{item['name']}: ${item['price']}" for item in Items.EQUIPAMENTOS]).execute()
                selected_item = selected_item.split(":", 1)  #get name of item in string
                item = find_dict_by_value(Items.EQUIPAMENTOS, "name",selected_item[0])
                return item
            if(categoria=="Armas"):
                selected_item = inquirer.select(
                    message="Selecione um item",
                    choices=[f"{item['name']}: ${item['price']}" for item in Items.ARMAS]).execute()
                selected_item = selected_item.split(":", 1)  #get name of item in string
                item = find_dict_by_value(Items.ARMAS, "name",selected_item[0])
                return item
if(__name__ == "__main__"):
    Loja = Loja()
    print(Loja.menu("Itens Mágicos"))