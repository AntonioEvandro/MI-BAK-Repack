import os
import tarfile
import gzip
import shutil
from functions.Finale import finale

def BakMi(inputs, outputs, name, package):
    """
        Empacota uma pasta de dados no formato de backup compátivel com o MIUI.
    """

    print("Adicionando estrutura interna...")
    apps = f"{outputs}/apps"
    appsTemp = f"{outputs}/apps/{package}/"
    shutil.copytree(inputs, appsTemp, dirs_exist_ok=True)

    tarTemp = outputs + "/" + name + ".tar"

    print("1. Criando a estrutura de arquivos...")
    with tarfile.open(tarTemp, "w") as tar:
        tar.add(apps, os.path.basename(apps))

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

    if os.path.isdir(apps):
        shutil.rmtree(apps)
    if os.path.exists(tarTemp):
       os.remove(tarTemp)

    byteSize = os.path.getsize(file)

    finale(inputs, name, outputs, byteSize)
