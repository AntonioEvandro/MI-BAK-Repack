from functions.CreateBak import BakMi

if __name__ == "__main__":
    inputFiles = r"inputs"
    outputs = r"outputs"
    fileName = input("Nome do arquivo final: ")
    BakMi(inputFiles, outputs, fileName)