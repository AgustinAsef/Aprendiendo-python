import re 

# Busqueda simple
# re es el modulo buildin utilizado generalmente para utilizar expreciones regulares
cadena = 'Esta es una cadena de caracteres para probar las expreciones regulares'

re.search('e', cadena) #devuelve la primera coincidencia

re.findall('e', cadena) #devuelve todas las cioncidencias

#esta forma es sencible a las mayusculas o las minusculas

# si quisiera ignorar la diferencia entra mayusculas y minusculas utilizo

re.findall('e', cadena, flags=re.IGNORECASE) #devuelve TODAS las cioncidencias

# Busqueda avanzada

# \d busca digitos numericos del 0 al 9
re.findall(r'\d', cadena) #la 'r' antes de la exprecion regular se utiliza para avisa que vamos a utilizar una
# \w se utiliza para caracteres alfanumericos mayusculas o minusculas y el guion bajo
# \s se utiliza para saltos de lineas y espacios
# \. buscabusca todo menos saltos de linea
# \ cancela carcteres especiales (se utiliza previo a un caracter especial para buscarlo)
# \n busca los saltos en linea

# si utlizamos la letra mayuscula en vez de minuscula la funcion se convierte en lo opuesto

#encontrando patron complejo

re.findall(r'\d\.\s', cadena)

# en esta cadena estamos buscando un numero, seguido de un ., seguido de un espacio o salto de linea

# para buscar si un caracter o string esta en el inicio de una linea
re.findall(r'^Esta', cadena)

# para buscar el final
re.findall(r'regulares$')

# para buscar un patron que se repita n catidad de veces
re.findall(r'\d{3}', cadena) #esto va a buscar 3 numeros seguidos

# para buscar al menos n cantidad de veces y maximo m cantidad de veces
re.findall(r'\d{3,4}', cadena) #esto va a buscar 3 numeros seguidos ma
# re.findall(r'\d{n,m}', cadena)

