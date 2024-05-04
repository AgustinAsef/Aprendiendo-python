class Personaje():
  def __init__(self, nombre, golpe_especial, poder_de_ataque, defensa):
    self.nombre = nombre
    self.golpe_especial = golpe_especial
    self.poder_de_ataque = poder_de_ataque
    self.defensa = defensa
  
  def hablar(self):
    print(f'{self.nombre}: mis habilidad es {self.golpe_especial}, tengo {self.poder_de_ataque} de ataque y {self.defensa} de defensa')
    
  def __add__(self, otro_personaje):
    return Personaje(
      self.nombre[:len(self.nombre)//2] + otro_personaje.nombre[len(otro_personaje.nombre)//2:],
      self.golpe_especial + ' y ' + otro_personaje.golpe_especial,
      ((self.poder_de_ataque + otro_personaje.poder_de_ataque)//3) ** 2,
      ((self.defensa + otro_personaje.defensa)//3) ** 2
      )  