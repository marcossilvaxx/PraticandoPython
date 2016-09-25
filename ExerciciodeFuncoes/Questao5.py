def somaImposto(taxaImposto, custo):
    resultado = custo + (taxaImposto / 100 * custo)
    print("O novo valor de custo com Imposto é:", resultado)

taxaImposto = eval(input("Informe a taxa de imposto:\n"))
custo = eval(input("Informe o custo do item:\n"))

somaImposto(taxaImposto, custo)


