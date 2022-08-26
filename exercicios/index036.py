a=int(input('Primeiro numero: '))
b=int(input('Segundo numero: '))
c=int(input('Terceiro numero: '))
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print(f"Maior: {maior}")
print(f"Menor: {menor}")