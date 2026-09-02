import sys
from utils.Utils import menu, exit

def end():
    print(exit())
    sys.exit(0)

def start():
    print(menu())
    while True:
        try:
            fileName = input("Nome do arquivo final ou comando:\n   ")
        except (EOFError, KeyboardInterrupt):
            raise
        if fileName in ("exit", "sair", "q"):
            break