#--- Trabalhando com datas ---#

from datetime import date, time, datetime

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S') )
    print(data_atual.strftime('%c'))
    print(data_atual.weekday)
    
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])

    data_criada = datetime(2018, 6, 20, 15, 30, 20)

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual)
    print(data_atual_str)
    print(type(data_atual_str))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, secound=30)
    print(horario)
    horario_str = horario.strftime('$H:%M:%S')
    print(horario_str)
    print(type(horario_str))


if __name__ == '__main__':
    trabalhando_com_date()