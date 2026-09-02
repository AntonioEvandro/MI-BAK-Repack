import os
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

def name(f, p):
    outputs = r"outputs"
    while True:
        try:
            fileName = input("Nome do arquivo final.\n  Digite o nome que deseje ou enter para usar o nome do pacote na pasta:\n   ")
        except (EOFError, KeyboardInterrupt):
            raise
        if fileName in ("exit", "sair", "q"):
            break
        elif fileName:
            BakMi(f, outputs, fileName, p)
            break
        elif not fileName:
            #print("Informe um nome de arquivo a criar.")
            BakMi(f, outputs, p, p)
            break

def start():
    print(menu())
    inputFiles = r"inputs"
    package = ""
    while True:
        try: package = input("Nome do pacote na pasta inputs:\n    ")
        except (EOFError, KeyboardInterrupt):
            raise
        if package in ("exit", "sair", "q"):
            end()
            break
        elif package:
            if os.path.exists(inputFiles + "/" + package):
                inputFiles = inputFiles + "/" + package
                name(inputFiles, package)
                proceed()
            else:
                print("\033[31mNome de pacote não encontrado\033[0m\n    Verifique a pasta \033[33minputs\033[0m\n")
        elif not package:
            print("Informe o nome do pacote do aplicativo em inputs/\n")
        