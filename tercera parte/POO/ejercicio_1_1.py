from abc import ABC, abstractclassmethod

class Personaje():
  
  def __init__(self, nombre, habilidad, poder_de_ataque, defensa):
    self.nombre = nombre
    self.habilidad = habilidad
    self.poder_de_ataque = poder_de_ataque
    self.defensa = defensa
  
  def ataque(self):
    print(f'inflinge {self.poder_de_ataque} puntos de daño')
    
  def defender(self):
    print(f'la defensa evita {self.defensa} puntos del ataque')  

  def __add__(self, otro_personaje):
    return Personaje(
      self.nombre[:len(self.nombre)//2] + otro_personaje.nombre[len(otro_personaje.nombre)//2:],
      self.habilidad + ' y ' + otro_personaje.habilidad,
      ((self.poder_de_ataque + otro_personaje.poder_de_ataque)//2) ** 2,
      ((self.defensa + otro_personaje.defensa)//2) ** 2
      )
    
  def __str__(self):
    return f'mi nombre es {self.nombre}, mis habilidades son {self.habilidad}, tengo {self.poder_de_ataque} de ataque y {self.defensa} de defensa'
    
class Peleador(Personaje):
  def __init__ (self, nombre, habilidad, poder_de_ataque, defensa):
    super().__init__(nombre, habilidad, poder_de_ataque, defensa)

  def __str__(self):
    return 'Te voy a moler a golpes'
    
class Mago(Personaje):
    def __init__ (self, nombre, habilidad, poder_de_ataque, defensa):
      super().__init__(nombre, habilidad, poder_de_ataque, defensa)

    def __str__(self):
      return 'Te voy a hechizar'

zoro = Peleador('zoro', 'espadas multiples', 1200, 500)
grindamer = Mago ('grindamer', 'bola sombra', 1000, 1000)

nuevo_personaje = zoro + grindamer
print(nuevo_personaje)