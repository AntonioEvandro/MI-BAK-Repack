def BakMi(inputs, outputs, name):
    """
        Empacota uma pasta de dados no formato de backup compátivel com o MIUI.
    """
    tarTemp = outputs + "/" + name + ".tar"

    print("\nArquivos em: " + inputs + ", usados para criar: " + name + r".bak" + ".\nPasta do .bak resultante: " + outputs + ".")