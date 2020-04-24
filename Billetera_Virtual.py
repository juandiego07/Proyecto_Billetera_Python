""" Clase Cripto Moneda """
import abc import ABC, abstractmethod

class moneda(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

""" Conexion a Archivo  db = open('db.txt', 'w') db.write('Primera línea') db.close()"""

""" Validar Opcion de Menu"""
def ValidarOpcion(opc1):
    datos = "123456"
    a = set(datos)
    b = set(opc1)
    if len(b-a)>0:
        return True
    else:
        return False

""" Procedimiento Menu Principal"""

def MenuBilletera():
    while True:
        print("1.- Recibir cantidad: ")
        print("2.- Transferir monto: ")
        print("3.- Mostrar balance una moneda: ")
        print("4.- Mostrar balance general: ")
        print("5.- Mostrar histórico de transacciones: ")
        print("6.- Salir del programa ")
        opc = input("Elija un opcion: ")
        if ValidarOpcion(opc):
            print("Elija una opción correcta")
        else:
            print("Continuar con el programa")
            break

""" Cuerpo del Programa """
MenuBilletera()
