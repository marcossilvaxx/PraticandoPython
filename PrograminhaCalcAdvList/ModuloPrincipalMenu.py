'''
Módulo principal - Menu
'''

import time

def main():
    print("Jogo da Adivinhação - 1 | Calculadora Simples - 2 |  Lista de Favoritos(Frutas) - 3")
    escolha = eval(input("Qual das opções você quer usar?:\n"))

    if escolha == 1:
        import JogoAdivinhacao
        num = eval(input("Informe um número entre 1 e 10:\n"))
        JogoAdivinhacao.jogo_adivinhaçao(num)

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
        


if __name__ == "__main__":

    a = "Inicializando menu"

    for x in range(0,3):
        a = a + "."
        print(a)
        time.sleep(1)
    main()
