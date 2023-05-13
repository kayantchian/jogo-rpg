from InquirerPy import prompt
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
import time
import sys
from game import game

def credits() -> None:
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
    print("\n\n\n\n\n\n")
def main():
    op = True
    while(op):
        op = inquirer.select(
            message="Selecione uma opção:",
            choices=[
                "Novo Jogo",
                "Créditos",
                Choice(value=False, name="Sair"),
            ],
            default="Novo Jogo",
        ).execute()
        if op == "Novo Jogo":
            game()
        elif op == "Créditos":
            credits()
        else:
            sys.exit(0)


if __name__ == "__main__":
    main()


# perform_inicial_questions()
