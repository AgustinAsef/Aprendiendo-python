#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("archivos\\texto_de_dalto.txt",encoding="UTF-8")

#abriendo el archivo con with open
with open("archivos\\texto_de_dalto.txt",encoding="UTF-8") as archivo:
    
    #leemos el archivo
    contenido = archivo.read()
    
    #agregarr lineas
    for i in range(5):
      archivo.write(f"Linea {i} agregada\n")