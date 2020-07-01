#--- Aprender manipular arquivos Ler / Escrever ---#
import shutil #Importa o utilitário para copiar e mover arquivos.


#-- Cria e escreve arquivo na primeira linha.
def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()

#--- opção a, append no arquivo ---#
def atualiza_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    return texto

def copia_arquivo(arquivo, destino):
    shutil.copy(arquivo, destino)

def move_arquivo(arquivo, destino):
    shutil.move(aquivo, destino)


def media_notas(nome_arquivo):
    arquivo = ler_arquivo(nome_arquivo)
    aluno_nota = arquivo.split('\n')

    lista_aluno = []

    for x in aluno_nota:
        lista_nota = x.split(',')
        aluno = lista_nota[0]
        lista_nota.pop(0)

        media = lambda notas: sum([int(i) for i in notas]) /4
        str_lista_nota = ','.join([str(x) for x in lista_nota])

        lista_aluno.append({'Aluno: {}'.format(aluno) +' - Notas:{}'.format(str_lista_nota) + ' Media: {}'.format(media(lista_nota))})

    return lista_aluno



if __name__ == '__main__':
    diretorio = 'F:/Desenvolvimentos/Python/Estudo/PrimeiroAppPython/'
    nome_arquivo = diretorio + 'teste.txt'

    aluno = 'SP, 10, 10, 6, 6\nRJ, 8, 7, 5, 6\nMG, 9, 8, 5, 6\nAM, 9, 7, 6, 6'

    #escrever_arquivo(nome_arquivo, aluno)
    #atualiza_arquivo(nome_arquivo, aluno)
    #atualiza_arquivo(nome_arquivo, '3 Linha.\n')
    #atualiza_arquivo(nome_arquivo, '4 Linha.\n')

    print (media_notas('teste.txt'))

from datetime import datetime, time
data = datetime(1815, 12, 10, 00, 00, 00).strftime('%d/%m/%Y')
hora = time(hour=13, minute=14, second=00)
print('{} às {}'.format(data, hora))

from datetime import datetime
data_atual = datetime.now()
resultado = data_atual.strftime('%d/%m/%Y %H:%M:%S')
print(resultado)