def embaralhar(s):
    import random
    import string
    embaralha = random.sample(s, len(s))
    string = "".join(embaralha)
    print(string.lower())

s = str(input("Informe uma palavra:\n"))

embaralhar(s)