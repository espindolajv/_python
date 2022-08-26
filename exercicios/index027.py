cid=input('Em que cidade voce nasceu ?').strip()
print(cid[:].lower()=='taguatinga sul')
if cid.lower()=='taguatinga': 
    print('Qual taguatinga?')
    sul=input('Norte ou Sul? ')
    print(sul[:3].lower()=='sul')
