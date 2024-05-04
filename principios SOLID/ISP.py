# ISP, principio de segregacion de interfaz
# este principio establece que ningun cliente debe depender de interfaces que no utiliza
# en este caso lo aplicariamos a los metodos de las clases

from abc import ABC, abstractclassmethod

class Trabajador(ABC):
  
  @abstractclassmethod
  def comer(self):
    pass
  
  @abstractclassmethod
  def trabajar(self):
    pass
  
  @abstractclassmethod
  def dormir(self):
    pass
  
class Humano(Trabajador):
  
  def comer(self):
    print('estoy comiendo')
  
  def trabajar(self):
    print('estoy trabajando')
  
  def dormir(self):
    print('estoy durmiendo')

class Robot(Trabajador):
  
  def comer(self): # en este caso, al robot recibir la clase trabajador requeriria 
    pass #establecer los metodos comer y dormir, aunque un robot no los haga, por lo que no respeta el principio
  
  def trabajar(self):
    print('estoy trabajando')
  
  def dormir(self):
    pass
