import math
co=float(input("Valor do cateto oposto: "))
ca=float(input("Valor do cateto adjacente: "))
print("Valor da hipotenusa: {:.2f}".format(math.sqrt(co**2+ca**2)))
print("Valor da hipotenusa: {:.2f}".format(math.hypot(co,ca))) #hypot=calculo da hipotenusa
