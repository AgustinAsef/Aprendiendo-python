# Metodos especiales
# funciones pre establecidas dentro de py llamados a travez de palabras reservadas

class Persona: 
  def __init__(self, nombre, edad, ciudadania): #metodo especial __init__ el cual sirve apra crear la clase
    self.nombre = nombre 
    self.edad = edad
    self.ciudadania = ciudadania
  
  def __str__(self): #__sstr__ establece como debe mostrarse esta clase a travez de una cadena de texto
    return f'Mis datos son {self.nombre}, {self.edad}, {self.ciudadania}'
  
  def __add__(self, otro): #sobrecarga de operadores: dentro de py todo es una clase y gracias a esto nosotros podriamos definir cosas como sumar instancias a travez de metodos especiales
    return Persona(self.edad + otro.edad, self.nombre + otro.nombre, self.ciudadania + otro.ciudadania) 

agustin = Persona('agustin gomez', 20, 'argentino')
pedro = Persona('pedro sanchez', 25, 'colombiano')

nueva_persona = agustin + pedro #esto hereda tanto los metodos como lo definido en __add__