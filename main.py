import requests as requests
from datetime import datetime

""" FUNCION PARA VALIDAR EL INGRESO DE UNA MONEDA DE BINANCE """
def ValidarMoneda(a): 
    url = 'https://api.binance.com/api/v3/ticker/price'
    data = requests.get(url)
    data_json = data.json()
    for bitcoin in data_json:
        symbol = bitcoin['symbol']
        price = bitcoin['price']
        if symbol == a:
            return a
            break
        else:
            continue
    print('Moneda no encontrada')
    return ValidarMoneda(input(mensaje))

""" FUNCION QUE RETORNA EL PRECIO DE LA MONEDA INTRODUCIDA POR EL USUARIO """
def ValidarPrecio(a):
    url = 'https://api.binance.com/api/v3/ticker/price'
    data = requests.get(url)
    data_json = data.json()
    for bitcoin in data_json:
        symbol = bitcoin['symbol']
        price = bitcoin['price']
        if symbol == a:
            return price
            break
        else:
            continue
    return 0

""" FUNCION PARA VALIDAR DATOS NUMERICOS O ALFABETICOS """
def ValidarDato(dato, opc, mens):
    a = set(dato)
    b = set(opc)
    if (b-a) > 0:
        print('Caracteres Invalidos')
        return ValidarDato(dato, opc, mens)
    else:
        return opc

""" METODO QUE MUESTRA EN PANTALLA EL MENÚ PRINCIPAL DEL SISTEMA """
def menu1():
    print('\nMenu Principal')
    print('\n1.-Recibir cantidad: ')
    print('2.-Transferir monto:  ')
    print('3.-Mostrar balance una moneda: ')
    print('4.-Mostrar balance general: ')
    print('5.-Mostrar histórico de transacciones: ')
    print('6.-Salir del programa: ')

""" METODO QUE GUARDA EN UN ARCHIVO DE TEXTO LA CONSIGNACION RECIBIDA EN CRIPTO MONEDAS """
def recibircantidad(mensaje):
    cod = '1194418306'
    name = ValidarMoneda(input(mensaje))
    num = float(input('Ingrese la catidad de '+str(name)+' a recibir: '))
    monto = num * float(ValidarPrecio(name))
    try:
        db = open('db.csv', 'rt')
        for x in db:
            a, b, c, d, e, f, g, h, i = x.rstrip("\\n").split(";")
            if b == name:
                cant = float(d)
                saldo = float(f)
            else:
                cant = 0
                saldo = 0
        db.close()
    except IOError:
        db = open('db.csv', 'at')
        cant = 0
        saldo = 0
    cant = cant + num
    saldo = saldo + monto
    now = datetime.now()
    date = now.strftime('%d/%m/%Y %H:%M:%S')
    codrem = input('Ingrese el código del remitente: ')
    tipo = 'Consignacion'
    db = open('db.csv', 'at')
    db.write(cod+';'+str(name)+';'+str(num)+';'+str(cant)+';'+str(monto)+';' + str(saldo)+';'+date+';'+codrem+';'+tipo+'\n')
    db.close

""" METODO QUE GUARDA EN UN ARCHIVO DE TEXTO LA TRANFERENCIA REALIZADA EN CRIPTO MONEDAS """
def transferirmonto(mensaje):
    cod = '1194418306'
    name = ValidarMoneda(input(mensaje))
    num = float(input('Ingrese la catidad de '+str(name)+' a transferir: '))
    monto = num * float(ValidarPrecio(name))
    try:
        db = open('db.csv', 'rt')
        for x in db:
            a, b, c, d, e, f, g, h, i = x.rstrip("\\n").split(";")
            if b == name:
                cant = float(d)
                saldo = float(f)
            else:
                cant = 0
                saldo = 0
        db.close()
    except IOError:
        db = open('db.csv', 'at')
        cant = 0
        saldo = 0
    cant = cant - num
    saldo = saldo - monto
    now = datetime.now()
    date = now.strftime('%d/%m/%Y %H:%M:%S')
    codrem = input('Ingrese el código del remitente: ')
    tipo = 'Transferencia'
    db = open('db.csv', 'at')
    db.write(cod+';'+str(name)+';'+str(num)+';'+str(cant)+';'+str(monto)+';' + str(saldo)+';'+date+';'+codrem+';'+tipo+'\n')
    db.close

""" METODO QUE MUESTRA EL BALANCE DE UNA CRIPTOMONEDA ESPECIFICA """
def mostrarbalance(mensaje):
    name = ValidarMoneda(input(mensaje))
    try:
        db = open('db.csv', 'rt')
        for i in db:
            a, b, c, d, e, f, g, h = i.rstrip("\\n").split(";")
            result = '\nDe la moneda '+b+' tiene la cantidad de: ' +c+' y su equivalente en USD es: '+e+'\n'
        db.close()
    except IOError:
        print('No existe monedas en la billetera')
    print(result)

""" METODO QUE MUESTRA EL BALANCE GENERAL DE LAS CRIPTOMONEDAS  """
def mostrarbalancegeneral():
    dic = dict()
    total = dict()
    suma = 0
    try:
        db = open('db.csv', 'rt')
        for x in db:
            a, b, c, d, e, f, g, h, i = x.rstrip("\\n").split(";")
            dic[b] = 'La moneda '+b+' tiene una cantidad de ' +d+' y un monto en USD de: '+f
            total[b] = f
        db.close()
        for key in dic:
            print('\n'+dic[key])
            suma = suma + float(total[key])
        print('\nEl monto total en dolares es de: '+str(suma))
    except IOError:
        print('No existe monedas en la billetera')


def mostrarhistorico():
    try:
        db = open('db.csv', 'rt')
        for x in db:
            a, b, c, d, e, f, g, h, i = x.rstrip("\\n").split(";")
            print('La transacción se realizó el '+g+' con la moneda '+b+', fue una '+i+', el usuario es '+h+' por un cantidad de '+c+' por un monto en USD de '+e)
        db.close()
    except IOError:
        print('No existe monedas en la billetera')


while True:
    menu1()
    mensaje = ''
    opc = input('\nElija un opcion: ')
    if opc == '6':
        break
    elif opc == '1':
        mensaje = 'Ingrese la moneda a recibir: '
        recibircantidad(mensaje)
    elif opc == '2':
        mensaje = 'Ingrese la moneda a transferir: '
        transferirmonto(mensaje)
    elif opc == '3':
        mensaje = 'Ingrese la moneda a mostrar su balance: '
        mostrarbalance(mensaje)
    elif opc == '4':
        mostrarbalancegeneral()
    elif opc == '5':
        mostrarhistorico()
    else:
        print('Elija una opcion valida')
        continue
