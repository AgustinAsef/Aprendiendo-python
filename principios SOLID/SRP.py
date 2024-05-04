# SRP, o principio de responsabilidad unica
# establece que una clase debe tener una sola responsabilidad o tarea

class Auto():
  def __init__(self):
    self.posicion = 0
    self.combustible = 100
    
  def mover(self, distancia_recorrida):
    if self.combustible >= distancia_recorrida / 2 :
      self.posicion += distancia_recorrida
      self.combustible -= distancia_recorrida / 2
    else:
      print('no hay combustible suficiente')
      
  def agregar_combustible(self, cantidad):
    self.combustible += cantidad
    
  def obtener_combuustible(self):
    return self.combustible
  
# esta clase no respeta el principio de responsabilidad unica 
# ya que una misma clase se esta encargando de varias tareas.

# la forma optima de realizar esta clase seria la siguiente:

class Auto_optimo(): # de esta forma se crea una clase auto la cual recibe una clase como metodo
  def __init__(self, tanque): # tanque tiene sus propias clases las cuales podrea usar cuando se instancie
    self.kilometrage = 0
    self.tanque = tanque
    
  def mover_auto(self, distancia): # este metodo mueve el auto y utiliza metodos de la clase tanque  que recibe como parametro
    if self.tanque.obtener_combustible() >= distancia / 2 :
      print('el auto se mueve')
      self.kilometrage += distancia
      self.tanque.usar_combustible(distancia / 2) # e incluso le puedo enviar parametros 
    else:
      print('no hay suficiente combustible')

class Tanque(): #esta es la clase tanque de combustible la cual tiene sus propios metodos
  def __init__(self): # y si bien funcionan juntas, son clases separadas unas de otras
    self.combustible = 100
    
  def agregar_combustible(self, cantidad):
    self.combustible += cantidad
    
  def obtener_combustible(self):
    return self.combustible
  
  def usar_combustible(self, cantidad):
    self.combustible -= cantidad


tanque_de_100_ltr = Tanque()
auto = Auto_optimo(tanque_de_100_ltr)
    
  