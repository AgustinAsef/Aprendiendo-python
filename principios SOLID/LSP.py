# LSP, o principio de sustitucion de liskov
# est eprincipio estable que todas las clases hijo tienen que poder ser sustituidas por sus clases padre
# es decir que la clase padre A debe de poder usarse en todos los lugares donde sus clases hijos se usen

class Ave:
  def __init__(self):
    print('un ave')
    
  def volar():
    print('el ave vuela')

class Pinguino(Ave):
  def __init__(self):
    print('el pinguino es un ave')
    
  def volar():
    print('pero el pinguino no puede volar')
    
# estas clases no estarrian respetando el proncipio de sustitucion 
# ya que la clase pinguino no podria hacer todo los que hacen las aves
# la solucion para esto es crear mas sub clases


class Ave: # deberia definir todo lo que SI pueden hacer las aves
  def __init__(self):
    print('un ave')

class Aves_voladoras(Ave): # se crean sublcases para identificar los subgrupos
  pass

class Aves_no_voladoras(Ave):
  pass

class Pinguino(Aves_no_voladoras): # y ahora si pinguino respeta el principio
  def __init__(self):
    print('el pinguino es un ave')