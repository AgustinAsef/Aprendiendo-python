# OCP, principio de abierto/cerrado
# este principio establece que las entidades deben estar abiertas a la extencion 
# pero cerradas para la modificacion

# en el siguiente codigo muestra una clase notificacion que requiere que
# otras clases definan una funcion para diferentes tipos de notificaciones

class Notificacion():
  def __init__(self, mensaje):
    self.mensaje = mensaje
  
  def enviar_notificacion(self):
    raise NotImplementedError
    
class Notificar_por_mail():
  def enviar_notificacion(self):
    print('se envio una notificacion via mail')
    
class Notificar_por_msm():
  def enviar_notificacion(self):
    print('se envio una notificacion via msm')
    
class Notificar_por_pop_up():
  def enviar_notificacion(self):
    print('se envio una notificacion via pop up')        

# no se implementa asi pero es un ejemplo para explicar el concepto