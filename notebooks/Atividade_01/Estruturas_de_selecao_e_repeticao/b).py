import random as rd


n = rd.randrange(1, 100)
palpite = 0

while palpite != n :
    palpite = int(input("Tente adivinhar o numero secreto entre 1 e 100, dê seu palpite: "))
    if palpite < n :
        print("Seu palpite é menor que o numero secreto, tente novamente.")
    elif palpite > n :
        print("Seu palpite é maior que o numero secreto, tente novamente")
    else:
        print("Você acertou!!!")