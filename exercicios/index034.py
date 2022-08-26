dis=int(input('Distancia da viagem em Km: '))
if dis<=200:
    print("O preço da passagem é R${}".format(dis*0.50))
else:
    print("O preço da passagem é R${}".format(dis*0.45))