# Funcion sumar 5 valores
def suma_5_parametros():
    a=input("Ingrese el 1° numero: ")
    b=input("Ingrese el 2° numero: ")
    c=input("Ingrese el 3° numero: ")
    d=input("Ingrese el 4° numero: ")
    e=input("Ingrese el 5° numero: ")
    print("El resutado de la suma es:",(float(a)+float(b)+float(c)+float(d)+float(e)))

def main() :
    opcion_elegida = 0
    while opcion_elegida != 9:
        print("Hola, selecione la operacion que desea realizar\n 1 - Sumar\n 9 - Salir\n  ")
        opcion_elegida = input('Elegir opcion :  ')
        if int(opcion_elegida) == 1:
            suma_5_parametros()
        if int(opcion_elegida) == 9:
            print('Adios! ')
            exit()
if __name__ == '__main__':
    main();