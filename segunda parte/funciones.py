#Funciones

#funcione build in son propias de py
tupla = (1, 2, 3)

max(tupla) #devuelve en numero mas grande

min(tupla) #devuelve el numero mas chico

round(1.123 , 3) #redondea a cantidad de numeros despues de la coma como le digas

sum(tupla) #suma los valores de un iterable numerico

#creacion de funciones
#utilizan la palabra reservada def
def nueva_funcion ():
  print('nueva funcion')
  
#para recibir parametros
def funcion_con_parametros(nombre, edad):
  print(nombre, edad)
  
#parametro args '*' o argumento indefinido, converte las props en un solo valor que conlleve el parametro 
def funcion_args (*numeros):
  sum(numeros)
  
#si quisiera recibir mas parametros se colocan antes del parametro args
def funcion_args (letra,*numeros):
  print(letra)
  sum(numeros)
  
#funciones lambda
#como las arrow function de js
nombre = lambda x : x * 2