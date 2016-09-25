def imprimir(n):

############## USANDO WHILE #############
    print("\nUsando While\n")

    aux = 1

    while aux <= n:
        print((str(aux) + " ") * aux)
        aux += 1


################ USANDO FOR #############
    print("\nUsando For")

    for x in range(n + 1):
        print((str(x) + " ") * x)

n = eval(input("Informe um número:\n"))

imprimir(n)