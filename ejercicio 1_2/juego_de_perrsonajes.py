from clases import Personaje

personajes = {}

def iniciar_juego():
  opcion_elegida = input ("""
Elige una opcion:
  1: Crear personaje.
  2: Mostrar personajes.
  3: Fusionar personajes.
  4: Eliminar personaje.
  Opcion: """)
  
  if opcion_elegida == "1":
    crear_personaje()
  elif opcion_elegida == "2":
    mostar_personajes()
  elif opcion_elegida == "3":
    fusionar_personajes()
  elif opcion_elegida == "4":
    eliminar_personaje()
  else:
    print("No has elegido una opcion valida.")
    iniciar_juego()
    
# ---------------------------------------------------------------------------------------------

def crear_personaje():
  print("Elegiste crear personajes")
  nombre = input('Elige el nombre de tu personaje: ')
  golpe_especial = input('Elige el golpe especial de tu personaje: ') 
  poder_de_ataque = input('Cuanto poder de ataque tendra tu pesonaje?: ')     
  defensa = input('Cuanta defensa tendra tu pesonaje?: ')
  crear_clase_personaje(nombre, golpe_especial, poder_de_ataque, defensa)
  consultar_personaje(nombre)
  iniciar_juego()

def crear_clase_personaje(nombre, golpe_especial, poder_de_ataque, defensa):
  nuevo_personaje = Personaje(nombre, golpe_especial, int(poder_de_ataque), int(defensa))
  personajes [str(nombre)] = nuevo_personaje
    
# ---------------------------------------------------------------------------------------------

def mostar_personajes():
  print("Elegiste mostrar personajes")
  
  if len(personajes) == 0 :
    print('No hay personajes creados')
    iniciar_juego()
  if len(personajes) == 1:
      print(f"Hay {len(personajes)} personaje creado actualmente:")
  else:
      print(f"Hay {len(personajes)} personajes creados actualmente:")
      
  for clave in personajes:
    print(clave)
  
  consultar = input("Deceas consultar alguno? (si/no): ")
  if consultar.lower() == 'si':
    nombre_a_consultar = input('Que personaje te gustaria consultar? (escribe su nombre): ')
    consultar_personaje(nombre_a_consultar)
  else:
    print('Volviendo al menu principal')
    iniciar_juego()
    
# ---------------------------------------------------------------------------------------------

def fusionar_personajes():
  print("Elegiste fusionar personajes")
  if len(personajes) == 1 :
    print('Solo hay un personaje creado, debes crear mas para fusionarlos')
    iniciar_juego()
  else:
    primer_personaje = input('Cual es el primer personaje que deceas fusionar?: ')
    if primer_personaje in personajes :
      segundo_personaje = input('Cual es el segundo personaje que quierres fusionar?: ')
      if segundo_personaje in personajes:
        nuevo_personaje = personajes[primer_personaje] + personajes[segundo_personaje]
        personajes[str(nuevo_personaje.nombre)] = nuevo_personaje
        print('Se a creado el nuevo personaje, consultalo en el menu principal')
        iniciar_juego()
      else:
        print('No se encontraron coincidencias')
        fusionar_personajes()
    else:
      print('No se encontraron coincidencias')
      fusionar_personajes()
      
# ---------------------------------------------------------------------------------------------
   
def consultar_personaje(nombre):
  if nombre in personajes:
    personajes[nombre].hablar()
    iniciar_juego()
  else:
    print('No se encontraron coincidencias')

# ---------------------------------------------------------------------------------------------

def eliminar_personaje():
  print("elegiste eliminar personaje")
  personaje_a_eliminar = input('Cual es el personaje que deceas eliminar?: ')
  if personaje_a_eliminar in personajes:
    del personajes[personaje_a_eliminar]
  else:
    print('No se encontraron coincidencias')
    eliminar_personaje()
    
iniciar_juego()