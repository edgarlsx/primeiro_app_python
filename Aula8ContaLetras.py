def contaLetras(listaObj):
    contador = []
    for x in listaObj:
        qtde = len(x)
        contador.append(qtde)
    #end for

    return contador

if __name__ == '__main__':
    lista = ['paralelepipedo', 'systemas']
    print(contaLetras(lista))

