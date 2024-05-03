# Propiedades
# las propiedades se utilizan para realizar seters, geters, y deleters de una forma mas optima
class Usuario:
  def __init__(self, nombre, contrasena):
    self.__nombre = nombre
    self.__contrasena = contrasena
  
  @property #utilizando la propiedad property la clase sobreentiende que el geter se convierta en propiedad y nos habilita a hacer el resto
  def nombre_p(self):
    return self.__nombre
  
  @nombre_p.setter #para crear propiedades relacionadas al mismo valor utilizamos la propiedad ya declarada.lo que vamos a hacer
  def nombre_p(self, nuevo_nombre):
    self.__nombre = nuevo_nombre

  @nombre_p.deleter
  def nombre_p(self):
    del self.__nombre
    
  @property
  def contrasena_p(self):
    return self.__contrasena

  @contrasena_p.setter
  def constrasena_p(self, nueva_contrasena):
    self.__contrasena = nueva_contrasena
  
  @contrasena_p.deleter
  def contrasena_p(self):
    del self.__contrasena


usuario = Usuario('Juan', '13579') # creando la instancia de clase
del usuario.nombre_p # accediendo al deletter
usuario.nombre_p = 'Pedro' # modificando su valor con un seter
print(usuario.nombre_p) # accediendo a su valor con getter

