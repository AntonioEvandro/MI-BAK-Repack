from utils.Utils import sucess

def finale(inputs, name, outputs, size):
    print(sucess())
    print(f"\nArquivos em: " + inputs + ", usados para criar: " + name + r".bak" + ".\nVeja o resultado em: " + outputs + ".")
    print(f"\nTamanho total: {size}.\nNão esqueça de usar o tamanho total em bytes nos campos do descript.xml antes de zipar.")