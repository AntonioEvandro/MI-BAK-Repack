from utils.Utils import sucess

def finale(inputs, name, outputs, size):

    finale =  f"""
                ════════════════════════════════
                    Arquivos em: \033[33m{inputs}\033[0m      
                    usados para criar:
                        \033[32m{name + r".bak"}\033[0m.
                    Tamanho total: \033[32m{size}\033[0m.
                    Veja o resultado em: \033[33m{outputs}\033[0m.

                ════════════════════════════════"""
    print(sucess(), finale + "\n\033[31mNão esqueça\033[0m de usar o\033[32m tamanho total em bytes\033[0m nos campos do\033[34m descript.xml\033[0m antes de zipar.")
