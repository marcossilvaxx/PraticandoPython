class Pessoa:
    def __init__(self):
        self.nome = str(input("Informe o nome da pessoa:\n"))
        self.idade = eval(input("Informe a idade da pessoa:\n"))
        self.peso = eval(input("Informe o peso da pessoa:\n"))
        self.altura = eval(input("Informe a altura da pessoa:\n"))
        print("Construtor Finalizado.")
    def Envelhecer(self):
        anos = eval(input("Quantos anos envelheceu?\n"))
        self.idade += anos
        print("Nova idade: %i anos" % self.idade)
    def Engordar(self):
        massa = eval(input("Quanto engordou?\n"))
        self.peso += massa
        print("Novo peso: %.2f Kg" % self.peso)
    def Emagrecer(self):
        massa = eval(input("Quanto emagreceu?\n"))
        self.peso -= massa
        print("Novo peso: %.2f Kg" % self.peso)
    def Crescer(self):
        comprimento = eval(input("Quanto cresceu?\n"))
        self.altura += comprimento
        print("Nova altura: %.2f m" % self.altura)

marcos = Pessoa()

marcos.Envelhecer()
marcos.Engordar()
marcos.Emagrecer()
marcos.Crescer()


