import sys
from utils.Utils import menu, exit
from functions.CreateBak import BakMi

def end():
    print(exit())
    sys.exit(0)

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
        elif not fileName:
            print("Informe um nome de arquivo a criar ou comando.")