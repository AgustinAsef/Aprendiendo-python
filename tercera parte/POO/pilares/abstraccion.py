# Abstraccion
# la abstraccion es la acción de aislar los componentes esenciales de un objeto de aquellos que no lo son

class Auto():
  def __init__(self):
    self.estado = 'apagado'
    
  def encender_el_auto(self):
    print('chequeo de sistemas')
    self.estado = 'encendido'
    print('encendido')
  
  def conducir_el_auto(self): # en conceptos de abstrraccion, el usuario solo quiere conducir el auto, no tiene nocion de todos los procesos que ocurren detras
    if(self.estado == 'apagado'):
      self.encender_el_auto()
    print('conduce el auto')
    
    
mi_auto = Auto()
# mi_auto.conducir_el_auto()

# creacion de clases abstractas y metodos abstractos
# la creacion declases abstractass implica la creacion de clases que no se implementan de por si 
# si no que se utilizan como plantillas para otras clases

from abc import ABC, abstractclassmethod

class Persona(ABC): # la prop 'ABC' declara que la clase es una clase abstracta
  @abstractclassmethod # mientras que el decorador abstractclassmethod establece que los metodos son abstractos, aunque depende de 'ABC'
  def __init__(self, nombre, nacimiento, nacionalidad, sexo):
    self.nombre = nombre
    self.nacimiento = nacimiento
    self.nacionalidad = nacionalidad
    self.sexo = sexo
    
  @abstractclassmethod # este metodo abstracto sera definido segun la clase que herede de esta
  def hacer_actividad(self):
    pass
  
  def decir_nombre(self): # este metodo que no lo es lo tendra predefinido cualquier clase que herede de esta
    print(f'Hola, mi nombre es {self.nombre}')
    
class Estudiante(Persona):
  def __init__(self, nombre, nacimiento, nacionalidad, sexo):
    super().__init__(nombre, nacimiento, nacionalidad, sexo)
    
  def hacer_actividad(self): # el estudiante usara este metodo para avisar que esta estudiando
    print('estoy estudiando')
    
class Trabajador(Persona):
  def __init__(self, nombre, nacimiento, nacionalidad, sexo):
    super().__init__(nombre, nacimiento, nacionalidad, sexo)
    
  def hacer_actividad(self):  # el estudiante usara este metodo para avisar que esta trabajando
    print('estoy trabajando')
    

estudiante = Estudiante('Pedro', '02/08/1999', 'Colombiano', 'M')  
trabajador = Trabajador('Juan', '08/05/1985', 'Peruano', 'M')

estudiante.decir_nombre()
estudiante.hacer_actividad()
print('-------------------------------------------------------')
trabajador.decir_nombre()
trabajador.hacer_actividad()