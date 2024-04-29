#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

frase = input("escribe la frase mas larga que puedas en un minuto: ")
palabras = frase.split(' ')
contador_de_palabras = len(palabras)
tiempo_que_se_demoraria = round(contador_de_palabras / 1.66, 2)
tiempo_que_se_demoraria_el_que_habla_rapido = round(tiempo_que_se_demoraria * 0.7, 2)

if(tiempo_que_se_demoraria > 60):
  print("mucho texto")

print(tiempo_que_se_demoraria)
print(tiempo_que_se_demoraria_el_que_habla_rapido)
 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------