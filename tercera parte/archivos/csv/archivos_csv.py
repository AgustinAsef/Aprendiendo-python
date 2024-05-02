import pandas as pd

#leer archivo csv con pandas
df = pd.read_csv("archivos\\user_data.csv")

#acceder a los datosss de df
#print(df)

#acceder a una columna especifica
primer_columna = df['nombre']

#accede a una fila con la propiedad .head(cantidad de filas
# a mostrar de arriba para abajo)
primer_fila = df.head(1)

#mostrar filas de abajo para arriba
ultimas_filas = df.tail(2)

#accedientoa un dato especifico
elemento = df.loc[2, "edad"] #recibe la fila y la columna

#tambien se puede hacer con iloc
elemento_dos = df.iloc[2 , 2] #accede a la fila 2 y al elemento 2

#puedo usar slicing para obtener todos los datos de una fila
#o columna
elementos_especificos= df.loc[2,:]
print(elementos_especificos)


#acceder a la cantidad de filas y columnas
filas, columnas = df.shape #devuelve una tupla

#filtar df para obtener los que cumplan con cierta condicion
mayores_de_24 = df.loc[df['edad']>24,:]
print(mayores_de_24)

#slicing, acede a una cadena iterable desde el dato de inicio
#hasta el dato final sin incluirlo
letras = 'abcdefghijklmnopqrstuvwxyz'
letras_elegidas = letras[1:7]

#orderar los datos por numeros
df_ordenado = df.sort_values('edad') #utiliza la propiedad ascending=false

#concatenando df
df_concatenado = pd.concat([df, df])
