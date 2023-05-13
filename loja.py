from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from player import Player
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
                    message="Selecione um item",
                    choices=[item['name'] for item in Loja.ITEMS]).execute()
                price_selected_item = [item for item in Loja.ITEMS if item["name"] == selected_item]
                return price_selected_item
            if(op=="Equipamentos"):
                selected_item = inquirer.select(
                    message="Selecione um item",
                    choices=[item['name'] for item in Loja.EQUIPAMENTOS]).execute()
                price_selected_item = [item for item in Loja.EQUIPAMENTOS if item["name"] == selected_item]
                return price_selected_item
                
if(__name__ == "__main__"):
    Loja = Loja()
    Loja.menu()