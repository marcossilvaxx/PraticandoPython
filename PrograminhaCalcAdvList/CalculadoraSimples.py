'''
Calculadora simples
'''
def soma(nums):
    num = eval(input("Informe um número:\n"))
    soma = num
    for i in range(0,nums - 1):
        num = eval(input("Informe um número:\n"))
        soma = soma + num
    print("A soma dos números é:", soma)

def subtraçao(nums):
    num = eval(input("Informe um número:\n"))
    subtraçao = num
    for i in range(0, nums - 1):
        num = eval(input("Informe um número:\n"))
        subtraçao = subtraçao - num
    print("A subtração dos números é:", subtraçao)

def multiplicaçao(nums):
    num = eval(input("Informe um número:\n"))
    multiplicaçao = num
    for i in range(0, nums - 1):
        num = eval(input("Informe um número:\n"))
        multiplicaçao = multiplicaçao * num
    print("A multiplicação dos números é:", multiplicaçao)

def divisao(nums):
    num = eval(input("Informe um número:\n"))
    divisao = num
    for i in range(0, nums - 1):
        num = eval(input("Informe um número:\n"))
        divisao = divisao / num
    print("A divisão dos números é:", divisao)
        

def calculadora(operaçao, nums):

    import ModuloPrincipalMenu
    
    if operaçao == "Soma" or operaçao == "soma":
        soma(nums)
        pergunta = str(input("Deseja voltar para o menu?\n"))
        if pergunta == "Sim" or pergunta == "sim":
            ModuloPrincipalMenu.main()
        elif pergunta == "Não" or pergunta == "não":
            print("Programa encerrado.")
    elif operaçao == "Subtração" or operaçao == "subtração":
        subtraçao(nums)
        pergunta = str(input("Deseja voltar para o menu?\n"))
        if pergunta == "Sim" or pergunta == "sim":
            ModuloPrincipalMenu.main()
        elif pergunta == "Não" or pergunta == "não":
            print("Programa encerrado.")
    elif operaçao == "Multiplicação" or operaçao == "multiplicação":
        multiplicaçao(nums)
        pergunta = str(input("Deseja voltar para o menu?\n"))
        if pergunta == "Sim" or pergunta == "sim":
            ModuloPrincipalMenu.main()
        elif pergunta == "Não" or pergunta == "não":
            print("Programa encerrado.")
    elif operaçao == "Divisão" or operaçao == "divisão":
        divisao(nums)
        pergunta = str(input("Deseja voltar para o menu?\n"))
        if pergunta == "Sim" or pergunta == "sim":
            ModuloPrincipalMenu.main()
        elif pergunta == "Não" or pergunta == "não":
            print("Programa encerrado.")
    else:
        print("Operação desconhecida. Programa encerrado.")
        pergunta = str(input("Deseja voltar para o menu?\n"))
        if pergunta == "Sim" or pergunta == "sim":
            ModuloPrincipalMenu.main()
        elif pergunta == "Não" or pergunta == "não":
            print("Programa encerrado.")

