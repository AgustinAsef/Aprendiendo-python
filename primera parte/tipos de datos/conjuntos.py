#Conjuntos
conjunto = {1, 2, 3, 4, 5, 6} #Son colecciones no ordenadas de elementos únicos
conjunto_vacio = set() #son modificables, pero no se puede agregar dos veces el mismo elemento

#metodos de los conjuntos
conjunto.add(7) #agrega un elemento

conjunto.remove(2) #elimina el elemento que se le pase, si no lo encuentra devuelve un error

conjunto.discard(2) #elimina un elemento del conjunto, NO devuelve un error si no lo encuentra

conjunto.pop() #devuelve un lemento aleatorio del conjunto y lo elimina del conjunto original

conjunto.clear() #elimina todos los elementos

conjunto.union(conjunto_vacio) #devuelve un conjunto con la union de 2 y elimina los elementos duplicados

conjunto.intersection(conjunto_vacio) #devuelve un conjunto solo con los elementos que se encuentrran presentes en ambos

conjunto.difference(conjunto_vacio) #devuelve un conjunto con los elementos que están presentes en el primer conjunto pero no en el segundo

conjunto.symmetric_difference(conjunto_vacio) #devuelve un conjunto con los elementos que estan en cada conjunto eliminando los que se encuentran en ambos