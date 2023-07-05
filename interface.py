from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
import sys
from game import Game
from tqdm import tqdm


class Interface():
    
    def creditos() -> None:
        __AUTHOR__ = "\n\n  Feito por Kayan Tchian  \n\n"
        for x in range(1, 15):
            print("==", end="", flush=True)
            time.sleep(0.1)
        for char in __AUTHOR__:
            print(char, end="", flush=True)
            time.sleep(0.1)
        for x in range(1, 15):
            print("==", end="", flush=True)
            time.sleep(0.1)
        time.sleep(2)
        print("\n\n\n\n\n\n")

    def main(self):
        op = True
        while(op):
            op = inquirer.select(
                message="Selecione uma opção:\n",
                choices=[
                    "Novo Jogo",
                    "Créditos",
                    Choice(value=False, name="Sair"),
                ],
                default="Novo Jogo",
            ).execute()
            if op == "Novo Jogo":
                for i in tqdm(range(4)):
                    time.sleep(i)
                game = Game()
                if(game.game()):
                    print("Você zerou o jogo!")
                    Interface.creditos()
            elif op == "Créditos":
                Interface.creditos()
            else:
                sys.exit(0)


if __name__ == "__main__":
    jogo = Interface()
    jogo.main()


# perform_inicial_questions()
