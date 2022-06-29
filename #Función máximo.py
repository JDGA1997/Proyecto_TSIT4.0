#Función máximo 
def maximo(lista): 
    grande=0 
    for numero in lista: 
        if numero>grande: grande=numero 
    return grande
    print ("El valor MÁXIMO ingresado es: ", maximo(lista), "\n")