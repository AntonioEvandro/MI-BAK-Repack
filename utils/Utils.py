class Strings():
    _Menu = """
                ╔════════════════════════════════════════╗
                ║                                        ║
                ║       \033[34mE m p a c o t a r   . B A K\033[0m      ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║ • Coloque pastas e arquivos em uma pas-║
                ║  ta, com o mesmo nome do pacote do app ║
                ║  que deseje empacotar, na pasta inputs.║
                ║                                        ║
                ║ • Para sair digite (sair), (exit) ou   ║
                ║  (q) quando quiser                     ║
                ║                                        ║
                ╚════════════════════════════════════════╝"""
    
    _Exit = """
                ╔════════════════════════════════════════╗
                ║                                        ║
                ║            \033[31mE n c e r a n d o\033[0m           ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║                Até mais.               ║
                ║                                        ║
                ╚════════════════════════════════════════╝"""

    _Sucess = """
                ╔════════════════════════════════════════╗
                ║                                        ║
                ║            \033[32mO p e r a ç ã o\033[0m             ║
                ║           \033[32mC o n c l u i d a\033[0m            ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║    Arquivo .bak gerado com sucesso!    ║
                ║                                        ║
                ║                                        ║
                ╚════════════════════════════════════════╝"""

def menu():
    return Strings._Menu

def sucess():
    return Strings._Sucess

def exit():
    return Strings._Exit
