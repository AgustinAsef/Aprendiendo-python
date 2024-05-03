#herencia
class Persona: #las clase por convencion se crean con mayoscula la primera letra
  def __init__(self, nombre, fecha_de_nacimiento, ciudadania): #la palabra reservada self hace referencia a si mismo como clase
    self.nombre = nombre #se declaran las propiedades de la clase con referencia a las props que va a recivir
    self.fecha_de_nacimiento = fecha_de_nacimiento
    self.ciudadania = ciudadania
  
  def datos(self): #los metodos requieren la prop self para saber que se estan autoreferenciando, asi como tambien pueden recibir otras props
    print(f'Hola, mi nombre es {self.nombre}, naci el {self.fecha_de_nacimiento} y soy {self.ciudadania}')


#la clase trabajador heredaria las propiedades y metodos de la clase Persona


class Trabajador(Persona): #la clase recibe la clase padre
  def __init__(self, nombre, fecha_de_nacimiento, ciudadania, trabajo): #por props recibe las propiedades de la clase padre y las nuevas
    super().__init__(nombre, fecha_de_nacimiento, ciudadania) #la palabra reservada super hace referencia a la clase padre y sen inicializan las propiedades heredadas
    self.trabajo = trabajo #se inicializa la propiedad de la clase hijo

  def nuevos_datos(self): #los metodos hijos pueden sobreescribir los metodos del padre si se nombran de la misma manera
        print(f'Hola, mi nombre es {self.nombre}, naci el {self.fecha_de_nacimiento}, soy {self.ciudadania} y trrabajo de {self.trabajo}')
        
#creando una instancia de la clase trabajador
agustin_trabajador = Trabajador('agustin gomez', '06/08/1999', 'argentino', 'vendedor')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#herencia multiple

class NuevoTrabajador:
  def __init__(self, trabajo): #por props recibe las propiedades de la clase padre y las nuevas
     #la palabra reservada super hace referencia a la clase padre y sen inicializan las propiedades heredadas
    self.trabajo = trabajo #se inicializa la propiedad de la clase hijo

class Estudiante(Persona, NuevoTrabajador): #recibe las clases de las cual va a heredar 
  def __init__(self, nombre, fecha_de_nacimiento, ciudadania, trabajo, carrera): #se declara todo lo que va a recibir de cada una
     Persona.__init__(self, nombre, fecha_de_nacimiento, ciudadania) #se establece que propiedades recibe de cada clase (requiere la prop self)
     NuevoTrabajador.__init__(self, trabajo)
     self.carrera = carrera #se definen las propiedades de si misma
  
  def nuevos_nuevos_datos(self):
    print(f'Hola, mi nombre es {self.nombre}, naci el {self.fecha_de_nacimiento}, soy {self.ciudadania}, trrabajo de {self.trabajo} y estudio la carrera de {self.carrera}')

agustrin_estudiante_y_trabajador = Estudiante('agustin gomez', '06/08/1999', 'argentino', 'vendedor', 'cocina')


#para verificar si una clase es una subclase de otra utilizo la funcion issubclass
issubclass(Estudiante, Persona)
#para verificar si una declaracion es una instancia de una clase uso la funcion isinstance
isinstance(agustrin_estudiante_y_trabajador, Estudiante)