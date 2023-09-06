tupla = ('leão', 'macaco', 'zebra', 'girafa')

animal = input("Digite o nume de um animal: ").lower()

if animal in tupla:
    print("O animal está presente na tupla")
else:
    print("O animal não está presente na tupla")

    