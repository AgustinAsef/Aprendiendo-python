#Strings
string_con_comillas_simples = "string"
string_con_comillas_triples = """string
                                  string
                                    strring""" #se utilizan para incertar texto y que se respete el formato del mismo
string_vacio = str() #para crear stings sin valor o no iniciados

#Carácteres de escape
caracter_para_salto_de_linea = "\n"
caracter_para_tabulcaion = "\t"


#Metodos de los strings
string_de_prueba = 'hola mi nombre es Agustin'

#Convertir str a mayusculas
string_de_prueba.upper() #convierte en mayusculas, resultado = HOLA MI NOMBRE ES AGUSTIN

string_de_prueba.lower() #converrte en minuscula, resultado = hola mi nombre es agustin

string_de_prueba.capitalize() #converte la primera en mayuscula, resultado = Hola mi nombre es Agustin

string_de_prueba.find('hola') #devuelve el index donde encontro el caracter resultado = 0, si no lo encuentra devuelve -1
                                                              
string_de_prueba.index('hola') #devuelve el index donde se encontro, perro si no lo encuentra devuelve un error

string_de_prueba.isnumeric() #devuelve true si el str es un numero

string_de_prueba.isalpha() #devuelve true si el string contiene letras

string_de_prueba.count('h') #devuelve la cantidad de caracteres dentro del str que coincide con el buscado 

len(string_de_prueba) #cuenta la cantidad de caracteres

string_de_prueba.startswith('H') #comprueba si el str empieza con la letra especificada

string_de_prueba.endswith('n') #comprueba si el str finaliza con la letra especificada