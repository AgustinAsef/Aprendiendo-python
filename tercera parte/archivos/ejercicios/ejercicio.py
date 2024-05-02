#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd

nombres = ["Lucas", "Pedro", "Camila"]
apellidos = ["Sosa","Morena", "Sanchez"]

#registrando en archivo txt
with open("nombre_y_apellidos.txt","w") as archivo_txt:
  archivo_txt.write('Los datos son:\n') 
  for n, a in zip(nombres, apellidos):
    archivo_txt.writelines(f'\nnombre: {n}, apellido: {a}\n------------')

#para resolver este ejercicio con una for en una sola linea
#se crea el bucle dentro de una lista con la instruccion adelante

  
#[archivo_txt.writelines(f'\nnombre: {n}, apellido: {a}\n------------') for n, a in zip(nombres, apellidos)]

#recordar cerrarr los archivos txt depues de utilizarlos (with lo hace automaticamente)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

df = pd.read_csv('C:\\Users\\agust\\Desktop\\avtividades\\python\\tercera parte\\archivos\\ejercicios\\nombres.csv')

#cambiar el tipo de dato de una columna
df['edad'] = df['edad'].astype(str)

#cambiar un dato de la columna
df['apellido'].replace('gomez', 'asef', inplace=True)

#eliminar filas con datos faltantes (axis 0 elimina las filas, axis 1 elimina las columnas)
df.dropna(axis=0)

#eliminar filas repetidas
df.drop_duplicates()

