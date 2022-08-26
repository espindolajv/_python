frase=input("Digite uma frase: ")
print(frase)
print(len(frase))
print(frase.count('o'))
print(frase.find(""))
print("joao" in  frase)
print(frase.replace("joao","victor"))
frase.upper()#colocar em maisculo
frase.lower()#colocar em minisculo
frase.capitalize()#colocar somente a primeira letra pra maiscula 
print(frase.strip())#tira os espaço inuteis podendo colocar R ou L
print(frase.title())#colocar a inicial de todas as frase em maiscula    
print(frase.split())
print("_".join(frase))
