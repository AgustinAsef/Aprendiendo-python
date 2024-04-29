#Diccionario
diccionario = {'nombre' : 'nombre', 'edad' : 'edad', 'ciudad' : 'ciudad'} #Son colecciones no ordenadas de pares clave-valor
diccionario_vacio = dict() #Los elementos se acceden mediante la clave en lugar de su posición

#Metodos de los diccionarios
diccionario.keys() #devuelve las keys del mismo

diccionario.get('key') #retorna el valor de la key pasada

diccionario.clear() #elimina todos los elementos de un diccionario

diccionario.pop('key') #elimina elementos por clave

diccionario.items() #retorna un elemento iterable