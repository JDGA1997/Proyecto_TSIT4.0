![Image text](https://github.com/JDGA1997/Proyecto_TSIT4.0/blob/64467e0f0ea76618aa7ce1799a4f3b26473befa9/Logo%20TSIT4.0%20Modulo%20Programacion%20Inicial.png)

# Proyecto_TSIT4.0

## Aula 5

### Repositorio creado para la realizacion del Proyecto de la carrera de TSIT4.0 del ISPC

##

### Integrantes:

- Juan Diego Gonzalez Antoniazzi

- Agustin Fernandez

- Emma Gutierrez email: emygut@gmail.com

- <Integrante 4>

-karen  del pino

- <Integrante 6>

- Juliana Vanina Lezcano

- <Integrante 8>

- <Integrante 9>

- <Integrante 10>


## Proyecto

#### Este proyecto consiste en el desarrollo e implementación de 5 funciones escritas en lenguaje Python.
#### La modalidad de trabajo consistirá en asignar cada dos integrantes del equipo, una consigna con el fin de agilizar el desarrollo de la tarea y soporte ante cualquier duda surgida.

## Product Backlog

● El usuario debe ingresar 5 números enteros, los cuales serán almacenados en una lista.

● Función Suma: recibe como parámetro la lista y devuelve la suma total de todos sus elementos.

● Función Promedio: recibe como parámetro la lista y devuelve el promedio de sus elementos.

● Función Máximo: recibe como parámetro la lista y devuelve el valor máximo de todos los elementos que contiene.

● Función Mínimo: recibe como parámetro la lista y devuelve el valor mínimo de todos los elementos que contiene.

#Función máximo
def maximo(lista):
	grande=0
	for numero in lista:
		if numero>grande:
			grande=numero
	return grande
print ("El valor MÁXIMO ingresado es: ", maximo(lista), "\n")

#Función Mínimo 
def minimo(lista):
	minimo=0
	for numero in lista:
		if numero<minimo:
			minimo=numero
	 return minimo
#Imprimo el valor mínimo
print ("El valor MÍNIMO ingresado es: ", minimo(lista), "\n")

