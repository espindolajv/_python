print('RADAR DETECTADO!!!!')
print('VELOCIDADE MAXIMA: 80KM/h')
vel=int(input("Velocidade do carro em KM/h: "))
if vel>80:
    print('Velocidade acima da permitida \nMULTA: R${:.2f}'.format((vel-80)*7))
else:
    print('Dentro da velocidade permitida')