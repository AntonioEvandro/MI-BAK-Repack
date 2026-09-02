import os
import tarfile
import gzip

def BakMi(inputs, outputs, name):
    """
        Empacota uma pasta de dados no formato de backup compátivel com o MIUI.
    """
    tarTemp = outputs + "/" + name + ".tar"

    print("1. Criando a estrutura de arquivos...")
    with tarfile.open(tarTemp, "w") as tar:
        tar.add(inputs, os.path.basename(inputs))

    print("2. Aplicando compressão...")
    with open(tarTemp, "rb") as fIn:
        tarData = fIn.read()

    gzipData = gzip.compress(tarData)

    print("3. Injetando cabeçalho...")
    header = b"ANDROID BACKUP\n2\n1\nnone\n"

    file = outputs + "/" + name + ".bak"
    with open(file, "wb") as fOut:
        fOut.write(header)
        fOut.write(gzipData)

    if os.path.exists(tarTemp):
        os.remove(tarTemp)

    byteSize = os.path.getsize(file)

    print(f"\nArquivos em: " + inputs + ", usados para criar: " + name + r".bak" + ".\nVeja o resultado em: " + outputs + ".")
    print(f"Não esqueça de usar o tamanho total em bytes nos campos do descript antes de zipar.\nTamanho total: {byteSize}.")