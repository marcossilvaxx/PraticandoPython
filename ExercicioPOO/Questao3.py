class Retangulo:
    def __init__(self):
        self.comprimento = eval(input("Informe o comprimento do retângulo:\n"))
        self.largura = eval(input("Informe a largura do retângulo:\n"))
        print("Construtor finalizado.")
    def mudarLados(self):
        self.comprimento = eval(input("Informe o novo comprimento do retângulo:\n"))
        self.largura = eval(input("Informe a nova largura do retângulo:\n"))
        print("Valor dos lados alterados.")
    def retornarLados(self):
        return self.comprimento, self.largura
    def calcularArea(self):
        return self.comprimento * self.largura
    def calcularPerimetro(self):
        return self.comprimento + self.largura

retangulo = Retangulo()

pergunta = str(input("Deseja mudar o valor dos lados? (S/N)\n"))

if pergunta == "S":
    retangulo.mudarLados()

pergunta = str(input("Deseja ver o valor dos lados? (S/N)\n"))

if pergunta == "S":
    print(retangulo.retornarLados())

pergunta = str(input("Deseja ver a área do retângulo? (S/N)\n"))

if pergunta == "S":
    print(retangulo.calcularArea())

pergunta = str(input("Deseja ver o perímetro do retângulo? (S/N)\n"))

if pergunta == "S":
    print(retangulo.calcularPerimetro())