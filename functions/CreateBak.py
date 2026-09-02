import os
import tarfile
from functions.Finale import finale

def BakMi(inputs, outputs, name, package):
    """
        Empacota uma pasta de dados no formato de backup compátivel com o MIUI.
    """

    tarTemp = f"{outputs}/{name}.tar"

    print("1. Criando a estrutura de arquivos...")
    with tarfile.open(tarTemp, "w") as tar:
        path = f"apps/{package}"
        tar.add(inputs, arcname=path)

    print("2. Aplicando compressão...")
    with open(tarTemp, "rb") as fIn:
        tarData = fIn.read()

    print("3. Injetando cabeçalho...")
    header = b"ANDROID BACKUP\n2\n0\nnone\n"

    file = outputs + "/" + name + ".bak"
    with open(file, "wb") as fOut:
        fOut.write(header)
        fOut.write(tarData)

    if os.path.exists(tarTemp):
       os.remove(tarTemp)

    byteSize = os.path.getsize(file)

    finale(inputs, name, outputs, byteSize)
