class Quadrado:
    def __init__(self):
        self.lado = eval(input("Informe o tamanho do lado:\n"))
        print("Construtor finalizado.")
    def mudarLado(self):
        self.lado = eval(input("Informe o novo tamanho do lado:\n"))
    def retornarLado(self):
        return self.lado
    def calcularArea(self):
        return self.lado * self.lado

quadradin = Quadrado()

pergunta = str(input("Deseja mudar o valor do lado? (S/N)\n"))

if pergunta == "S":
    quadradin.mudarLado()

pergunta = str(input("Deseja ver o valor do lado? (S/N)\n"))

if pergunta == "S":
    print(quadradin.retornarLado())

pergunta = str(input("Deseja ver a área do quadrado? (S/N)\n"))

if pergunta == "S":
    print(quadradin.calcularArea())