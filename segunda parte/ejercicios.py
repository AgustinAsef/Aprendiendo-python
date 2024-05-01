#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

profesor = str
asistente = str
companeros = list

def obtener_companeros(cantidad_de_companeros):
  global profesor, asistente
  for i in range(cantidad_de_companeros):
    nombre = input('ingresa el nombre del companero: ')
    edad = int(input('ingresa la edad del companero: '))
    companeros.append((nombre, edad))
  companeros.sort(key = lambda x:x[1])  
  profesor = companeros[-1][0]
  asistente = companeros[0][0]
  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def es_primo (num):
  for i in range(2, num):
    if num%i == 0 : return False
  return True

def obtener_numeros_primos(numero):
  numeros_primos = []
  
  for i in range(2, numero+1):
    if es_primo(i):
      numeros_primos.append(i)

  print(numeros_primos)

obtener_numeros_primos(100)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------