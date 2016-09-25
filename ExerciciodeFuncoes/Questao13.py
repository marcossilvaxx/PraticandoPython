def moldura(linhas, colunas):
    for i in range(linhas + 2):
        if i == 0 or i == (linhas + 1):
            print("+" + ("-" * colunas) + "+")
        else:
            print("|" + (" " * colunas) + "|")


linhas = eval(input("Informe o número de linhas:\n"))
colunas = eval(input("Informe o número de colunas:\n"))

moldura(linhas, colunas)