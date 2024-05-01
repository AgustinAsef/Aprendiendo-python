#Bucles 

#iterar sobre  cada elemento de la secuencia iterable.
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for element in lista:
  print('se ejecutara una vez por cada elemento')
  
#para iterar sobre diccionarios
diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Ejemplo'}
for item in diccionario.items():
  print('requiere acceder al item')
  
#ejecutar un bloque de código mientras una condición especificada sea verdadera
while len(lista) > 9:
    print('no se ha cumplico la condicion')
  