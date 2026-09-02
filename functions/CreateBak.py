import os
import tarfile
from functions.Finale import finale

def BakMi(inputs, outputs, name, package):
    """
        Empacota uma pasta de dados no formato de backup compátivel com o MIUI.
    """

    tarTemp = f"{outputs}/{name}.tar"

    print("1. Criando a estrutura de arquivos...")
    with tarfile.open(tarTemp, "w", format=tarfile.GNU_FORMAT) as tar:
        path = f"apps/{package}"
        tar.add(inputs, arcname=path)

    print("2. Aplicando compressão...")
    with open(tarTemp, "rb") as fIn:
        tarData = fIn.read()

    print("3. Injetando cabeçalho...") # Ajustar depois para personalizar
    appLabelPlaceholder = f"{package} Zeromiss"
    headerMIUI = (
        f"MIUI BACKUP\n"
        f"2\n"
        f"{appLabelPlaceholder}\n"
        f"102\n"
        f"0\n"
        f"ANDROID BACKUP\n"
        f"5\n"
        f"0\n"
        f"none\n"
    ).encode('utf-8')

    file = outputs + "/" + name + ".bak"
    with open(file, "wb") as fOut:
        fOut.write(headerMIUI)
        fOut.write(tarData)

    if os.path.exists(tarTemp):
       os.remove(tarTemp)

    byteSize = os.path.getsize(file)

    finale(inputs, name, outputs, byteSize)
