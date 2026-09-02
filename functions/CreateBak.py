import os
import tarfile

def BakMi(inputs, outputs, name):
    """
        Empacota uma pasta de dados no formato de backup compátivel com o MIUI.
    """
    tarTemp = outputs + "/" + name + ".tar"

    print("1. Criando a estrutura de arquivos TAR...")
    with tarfile.open(tarTemp, "W") as tar:
        tar.add(inputs, os.path.basename(inputs))

    

    print("\nArquivos em: " + inputs + ", usados para criar: " + name + r".bak" + ".\nPasta do .bak resultante: " + outputs + ".")