#Función Mínimo 
def minimo(lista): 
    minimo=0 
    for numero in lista: 
        if numero<minimo: minimo=numero 
    return minimo 
    print ("El valor MÍNIMO ingresado es: ", minimo(lista), "\n")