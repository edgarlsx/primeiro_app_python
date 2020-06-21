#Listas / Tuplas 
#Lista pode Alterar os Elementos do Objeto
#Tupla NÂO pode alterar os objetos

listaInt = [1, 3, 5, 7]
listaStr = ['cachorro', 'gato', 'passaro', 'lobo']

for x in listaInt:
    print(x)

tupla = (1, 3, 5, 7)
tuplaStr = tuple(listaStr)

for x in tuplaStr:
    print('Tupla: {}'.format(x))


listaStr.sort()

if 'lobo' in listaStr:
    print('nao exite na lista sera incluido')
    listaStr.append('lobo')
else: 
    print ('existe na lista')
    listaStr.remove('lobo')

print(listaStr)