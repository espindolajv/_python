text=input("Digite uma frase: ").strip().lower()
print('A letra "A" apareceu {} vezes'.format(text.count('a')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(text.find('a')+1))
print('A letra "A" apareceu pela ultima vez na posição {}'.format(text.rfind('a')+1))
