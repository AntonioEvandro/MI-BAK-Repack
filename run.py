from functions.CreateBak import BakMi

if __name__ == "__main__":
    inputFiles = r"inputs"
    outputs = r"outputs"
    fileName = input("Nome do arquivo final: ") + r".bak"
    BakMi(inputFiles, outputs, fileName)
    print("\nArquivos em: " + inputFiles + ", usados para criar: " + fileName + ".\nPasta do .bak resultante: " + outputs + ".")