nome=input("Digite seu nome:")
print("Olá,",nome)
idade=int(input("Digite sua idade:"))
if idade>=18:
    print("Maior de idade")
else:
    print("Menor de idade")
print("{} Voce tem {} anos".format(nome,idade))


