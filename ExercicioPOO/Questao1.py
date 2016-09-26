class Bola:
    def __init__(self):
        self.cor = str(input("Informe a cor da bola:\n"))
        self.circunf = eval(input("Informe a circunferência da bola:\n"))
        self.material = str(input("Informe o material da bola:\n"))
        print("Construtor finalizado.")
    def trocaCor(self):
        self.cor = str(input("Informe a nova cor da bola:\n"))
    def mostraCor(self):
        print("A cor é:", self.cor)

bola = Bola()
bola.trocaCor()
bola.mostraCor()