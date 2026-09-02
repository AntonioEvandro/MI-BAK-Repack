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
                ╚══════════════════════════════╝"""
    
    _Sair = """
                ╔══════════════════════════════╗
                ║                              ║
                ║       E n c e r a n d o      ║
                ║                              ║
                ╠══════════════════════════════╣
                ║                              ║
                ║           Até mais.          ║
                ║                              ║
                ╚══════════════════════════════╝"""

    _Sucesso = """
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
    return Strings._Sucesso

def exit():
    return Strings._Sair
