#POO o programacion orientada a objetos

#creando una clase
class Persona: #las clase por convencion se crean con mayoscula la primera letra
  def __init__(self, nombre, fecha_de_nacimiento, ciudadania): #la palabra reservada self hace referencia a si mismo como clase
    self.nombre = nombre #se declaran las propiedades de la clase con referencia a las props que va a recivir
    self.fecha_de_nacimiento = fecha_de_nacimiento
    self.ciudadania = ciudadania
  
  def datos(self): #los metodos requieren la prop self para saber que se estan autoreferenciando, asi como tambien pueden recibir otras props
    print(f'Hola, mi nombre es {self.nombre}, naci el {self.fecha_de_nacimiento} y soy {self.ciudadania}')

#crear una instacia de la clase
agustin = Persona('agustin gomez', '06/08/1999', 'argentino')

#llamando a un metodo de la clase
agustin.datos()