'''
Lista de frutas favoritas
'''


def listafav():
    import string
    '''
    Fazer uma lista de frutas favoritas
    '''
    continuar = "Sim"
    listadefav = []

    while continuar == "Sim" or continuar == "sim":
        listadefav = listadefav
        aux = 0
        for x in range(1, 6):
            frutas = str(input("Informe um nome de uma fruta favorita:\n"))
            frutafav = frutas
            frutas = frutas.lower()
            for f in listadefav:
                if frutas == f.lower():
                    aux = aux + 1
            if aux == 1:
                print("Essa fruta já existe na lista de favoritos.")
            elif aux == 0:
                print("Essa fruta ainda não existe na lista de favoritos.")
                listadefav = listadefav + [frutafav]
                print(frutafav,"adicionado(a) à lista de favoritos.")
            aux = 0
            print("Lista de favoritos:", listadefav)
        continuar = str(input("Deseja inserir mais 5 nomes à sua lista de favoritos?\n"))
        if continuar == "Não" or continuar == "não":
            print("Programa encerrado! Sua lista de favoritos atual é:", listadefav)
            pergunta = str(input("Deseja voltar para o menu?\n"))
            if pergunta == "Sim" or pergunta == "sim":
                main()
            elif pergunta == "Não" or pergunta == "não":
                print("Programa encerrado.")
        elif continuar != "Sim" and continuar != "sim":
            print("Comando desconhecido. Programa encerrado.")
            pergunta = str(input("Deseja voltar para o menu?\n"))
            if pergunta == "Sim" or pergunta == "sim":
                main()
            elif pergunta == "Não" or pergunta == "não":
                print("Programa encerrado.")

def main():
    print("Jogo da Adivinhação - 1 | Calculadora Simples - 2 |  Lista de Favoritos(Frutas) - 3")
    escolha = eval(input("Qual das opções você quer usar?:\n"))

    if escolha == 1:
        import JogoAdivinhação
        num = eval(input("Informe um número entre 1 e 10:\n"))
        JogoAdivinhação.jogo_adivinhaçao(num)

    elif escolha == 2:
        import CalculadoraSimples
        operaçao = str(input("Informe qual a operação que você deseja executar:\n"))
        nums = eval(input("Informe quantos números você irá calcular:\n"))
        CalculadoraSimples.calculadora(operaçao, nums)

    elif escolha == 3:
        import ListadeFavoritosFrutas
        ListadeFavoritosFrutas.listafav()

    else:
        print("Comando desconhecido. Programa encerrado.")
