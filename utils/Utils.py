class Strings():
    _Menu = """
                ╔══════════════════════════════╗
                ║                              ║
                ║      E m p a c o t a r       ║
                ║           . B A K            ║
                ║                              ║
                ╠══════════════════════════════╣
                ║                              ║
                ║ • Coloque arquivos e pastas  ║
                ║  que deseje empacotar num ar-║
                ║  quivo .bak na pasta inputs. ║
                ║                              ║
                ║ • Para sair digite (sair),   ║
                ║  (exit) ou (q) quando quiser ║
                ║                              ║
                ╚══════════════════════════════╝"""
    
    _Exit = """
                ╔══════════════════════════════╗
                ║                              ║
                ║       E n c e r a n d o      ║
                ║                              ║
                ╠══════════════════════════════╣
                ║                              ║
                ║           Até mais.          ║
                ║                              ║
                ╚══════════════════════════════╝"""

    _Sucess = """
                ╔══════════════════════════════╗
                ║                              ║
                ║       O p e r a ç ã o        ║
                ║      C o n c l u i d a       ║
                ║                              ║
                ╠══════════════════════════════╣
                ║                              ║
                ║    Arquivo .bak gerado com   ║
                ║            sucesso!          ║
                ║                              ║
                ╚══════════════════════════════╝"""

def menu():
    return Strings._Menu

def sucess():
    return Strings._Sucess

def exit():
    return Strings._Exit
