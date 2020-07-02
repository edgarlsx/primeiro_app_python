#-- Trabalhando com exceptions --#

#lista = [1, 10]

#try:
#    divisao = 10 / 1
#    numero = lista[1]
#    #x = a


#except ZeroDivisionError:
#    print('Não consegue dividir por 0')

#except BaseException as ex:
#    print('Erro: {}'.format(ex))

#else:
#    print('Executa esse bloco caso Não ocorra erro.')

#finally:
#    print('Sempre executa esse bloco.')


try:
  x = ____
  elementos = ['terra', 'ar', 'fogo', 'agua']
  elementos.pop(x)
except:
  print('Elemento não encontrado')
else:
  print('Elemento {} removido.'.format(x))
finally:
  print('Busca completa')