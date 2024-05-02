#Modulos

#los modulos con conjunto de funciones en un archivo py al cual se puede acceder de manera remota

#existen 3 tipos de modulos
#modulos de py
#modulos de terceros
#modulos de terceros

#para importar modulos dentro de la misma ruta
import modulo_de_prueba as m_s

#parra ejecutar funciones dentro del modulo
m_s.saludar('juan')

#para importar directamente una funcion especifica
from modulo_de_prueba import saludar

#para importar modulos en otras rutas se debe agregar el modulo a los modulos de py con la funcion sys
import sys

#agrego la ruta del archivo
sys.path.append('C:\\Users\\agust\\Desktop\\avtividades\\python\\tercera parte\\modulo_de_prueba')

#asi deberia poder acceder al modulo desde el import directamente y a sus funciones
#import modulo_de_prueba as m_s

