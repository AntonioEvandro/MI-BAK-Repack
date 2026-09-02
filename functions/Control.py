import sys
from utils.Utils import menu, exit
from functions.CreateBak import BakMi

def end():
    print(exit())
    sys.exit(0)

def proceed():
    while True:
        res = input("   Deseja empacotar novamente? (s/n) ")
        if res in ("s", "sim", "yes", "ys", "y"):
            break
        elif res in ("n", "nao", "não", "no", "exit", "sair", "q"):
            return end()
        else:
            print("   Informe uma opção válida!")
            continue

def start():
    print(menu())
    inputFiles = r"inputs"
    outputs = r"outputs"
    while True:
        try:
            fileName = input("Nome do arquivo final ou comando:\n   ")
        except (EOFError, KeyboardInterrupt):
            raise
        if fileName in ("exit", "sair", "q"):
            break
        elif fileName:
            BakMi(inputFiles, outputs, fileName)
            proceed()
        elif not fileName:
            print("Informe um nome de arquivo a criar ou comando.")