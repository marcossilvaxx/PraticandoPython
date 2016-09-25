def conversao(hora, periodo):
    horaInt = int(hora[0:2] + hora[3:])
    if periodo == "A":
        if horaInt > 1200:
            result = horaInt - 1200
            if result <= 959 and result >= 100:
                result = str(result)[:1] + ":" + str(result)[1:]
            elif result > 959:
                result = str(result)[:2] + ":" + str(result)[2:]
            elif result <= 99:
                result = "00" + ":" + str(result)
            print(result,"AM")
        elif horaInt == 1200:
            print("00:00")
        else:
            print("O horário já está em AM.")
    elif periodo == "P":
        if horaInt <= 1200:
            result = horaInt + 1200
            result = str(result)[:2] + ":" + str(result)[2:]
            print(result,"PM")
        else:
            print("O horário já está em PM.")

def saida():
    conversao(hora, periodo)

while True:
    hora = str(input("Informe a hora:\n"))
    periodo = str(input("Informe o período (AM = A, PM = P):\n"))

    saida()