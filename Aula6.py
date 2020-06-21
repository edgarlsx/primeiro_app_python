# --- Conjuntos --- #

conjunto1 = {1, 2, 3, 4}
conjunto2 = {5, 6, 7, 8}
conjunto1.add(5)

conjuntoUniao = conjunto1.union(conjunto2)

cjInterseccao = conjunto1.intersection(conjunto2)
cjdiferenca1 = conjunto1.difference(conjunto2)
cjdiferenca2 = conjunto2.difference(conjunto1)
cjDifSimetrica = conjunto1.symmetric_difference(conjunto2)


print('Conjunto União, junta ou mais conjuntos: {}'.format(conjuntoUniao))
print('Conjunto Interseccao, pega os valores iguais dos conjuntos: {}'.format(cjInterseccao))
print('Conjunto Diferença, pega as diferenças dos conjuntos 1 e 2: {}'.format(cjdiferenca1))
print('Conjunto Diferença, pega as diferenças dos conjuntos 2 e 1: {}'.format(cjdiferenca2))
print('Conjunto Diferença Simetrica, pega as diferenças simetrica dos conjuntos 1 e 2: {}'.format(cjDifSimetrica))


conjuntoA = {1, 2, 3,}
conjuntoB = {1, 2, 3, 4, 5, 6,}

cjSubSet = conjuntoB.issubset(conjuntoA)
cjSuperSet = conjuntoB.issuperset(conjuntoA)
print('Conjunto SubSet, Conjunto B NÂO é sub conjunto de A: {}'.format(cjSubSet))
print('Conjunto SuperSet, Conjunto A é sub conjunto de B: {}'.format(cjSuperSet))


listaStr = ['cachorro', 'gato', 'passaro', 'lobo']
cjStr = set(listaStr)
listaStr = list(cjStr)

print('Conjunto da lista: {}'.format(cjStr))
print('Lista do conjunto: {}'.format(listaStr))