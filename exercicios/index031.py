from random import randint
print('-=-'*20)
print('Estou pensando em um numero entre 0 e 10')
print('-=-'*20)
num=int(input('Em quem numero estou pensando? '))
comp=randint(0,10)
if num==comp:
    print('Parabens, voce acertou!!!')
else:
    print('Errouuuuu!!!!')