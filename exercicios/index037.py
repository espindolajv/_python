sal=int(input('Salario: '))
if sal>=1250:
    print("Aumento de 10%, total: R${}".format(sal*1.10))
else:
    print('Aumento de 15%, total: R${}'.format(sal*1.15))