#Polimorfismo
#el polimorfismo es la capacidad de objetos de diferentes clases de responder al mismo mensaje de diferentes maneras
#tipos de polimorfismo:
      #de herencia: cuando los metodos deriban de otras clases padres
      #de sobrecarga de metodos: metodos con el mismo nombre se ejecutaran dependiendo de la cantidad de variables que se le pase
      #de cohercion: donde las clases hijos renombran las clases de las clases padres
      
class Gato():
  def sonido(self):
    return 'Miau'
  
class Perro():
  def sonido(self):
    return 'Guau'
  
def hacer_sonido(animal):
  print(animal.sonido())
  
gato = Gato()
perro = Perro()

hacer_sonido(gato)
hacer_sonido(perro)

#duck typing: dice que si camina como un pato, nada como un pato, hace como un pato y tiene plumas como un pato, yo lo llamare pato
#enlaces dinamicos y enlaces declarados: enlaces dinamicos implica que durante el proceso de ejecucuion se puede actualizar 
  #una variable para que haga referencia a diferentes clases. 
#tipo real y tipo declarado: el tipo real hace referencia a la clase padre de todas las clases 
  # y el tipo declarado es la clase hijo que estamos usando para instanciar la clase
