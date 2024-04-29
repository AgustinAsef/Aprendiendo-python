#Listas
lista = ['dato', 'dato', 12, 34, 'dato', 'dato'] #conjunto de datos separados porr ','
lista_vacia = list() #las listas son iterables

#metodos de las listas
len(lista) #devuelve el largo de la lista

lista.append('nuevo elemento') #agrega un nuevo elemento al final de la lista

lista.insert(2, 'nuevo elemento') #agrega un nuevo elemento en una pocision especifica

lista.extend(['nuevo dato', 'nuevo dato', 'nuevo dato']) #agrega varrios elementos, recibe una lista

lista.pop(1) #elimina elementos por su indice, puede eliminar desde el final usando numeros negativos

lista.remove('dato') #elimina un elemento especifico por su valor

lista.clear() #elimina todos los elementos de la lista

lista.sort() #se utiliza para ordenarr una lista en orden ascendente, puede ordenarce al revez utilizando la prop reverse=true

lista.reverse() #invierte el lugar de los lementos de una lista