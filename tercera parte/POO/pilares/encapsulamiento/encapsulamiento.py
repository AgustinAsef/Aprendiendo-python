#Encapsulamiento 

class clase_priv:
  def __init__(self):
    self._atributo_privado = 'privado' # el '_' antes de la declaracion de atributos en las clases implica que estos son ""privados"", si bien es posible acceder a ellos
                                        # mediante el uso de variables comunes, por convencion no deberia accederse
                                        
priv = clase_priv()
priv._atributo_privado # devolveria el valor del atributo privado

class realmente_priv:
  def __init__(self):
    self.__atributo_realmente_privado = 'realmente privado' # el uso de '__' (dos guiones bajos) antes de la declaracion de la variable implica que esta es realmente privada
                                                              # por lo que para acceder a estas variables requeriremos del uso de seters y geters
                         
  # esta es la forma "vieja" de acceder a las propiedades privadas
                             
  def get_atributo_realmente_privado(self): # esto es un geter, una funcion con el unico objetivo de retornar ese valor
    return self.__atributo_realmente_privado
  
  def set__atributo_realmente_privado(self, nuevo_dato): # esto es un seter, una funcion con el unico objetivo de modificar el valor de la propiedad
    self.__atributo_realmente_privado = nuevo_dato
  
real_priv = realmente_priv()

# real_priv.__atributo_realmente_privado
# esto deberia devolverme una excepción (un error)

real_priv.get_atributo_realmente_privado() # a travez de un geter si se peude acceder a la propiedad privada

real_priv.set__atributo_realmente_privado('ahora no es tan privado') # a travez de un seter se modifica la propiedad

# actualmente la forma correcta de hacer esto es con el uso de decoradores
# los decoradores son una forma de acceder a funciones ejecutando codigo antes y/o despues de otra, para luego retornarla

# esto es la vieja forma de realizar una decoracion

def decorador(funcion):
  def funcion_modificada():
    #esto es anted de la funcion
    print('antes')
    funcion()
    #esto es despues de la funcion
    print('despues')
  return funcion_modificada

def llamado():
  print('aqui decorador')
  
#para ejecutarlas correctamente debo asignarle una variable

#llamando_decorador = decorador(llamado)

# llamando_decorador()

@decorador #se utiliza el @ para especificar que funcion es la dedoradora, por lo que no es necesario que se llame "decorador" especificamente
def saludo():
  print('Este es el decorador obtimo')
  
saludo()