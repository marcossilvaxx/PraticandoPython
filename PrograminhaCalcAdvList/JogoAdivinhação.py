'''
Fazer um simples jogo de adivinhação
'''


def jogo_adivinhaçao(num):

    import random

    while num != 0:
        # Compara com um número aleatório
        # Se o número informado for igual ao número aleatório, apresenta a mensagem de vitória
        if (num == random.randint(1, 10)):
            print("Parabéns! Você adivinhou o número!")

        # Se o número informado não for igual ao número aleatório, apresenta a mensagem de derrota
        else:
            print("Que pena! Não foi dessa vez!")

        num = eval(input("Informe um número entre 1 e 10(Para sair, digite 0):\n"))
        # Se o usuário digitar 0, o programa exibe uma mensagem e se encerra. (o loop acaba)
        if num == 0:
            print("Jogo da adivinhação encerrado. Obrigado por jogar!")
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


