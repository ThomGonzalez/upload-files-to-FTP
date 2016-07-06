# -*- coding: utf-8
import os

# Variable para la ruta al directorio.
path = 'C:\\CFDI\\RECIBO_TXT\\TMMGT'
# Lista vacia para incluir los ficheros
lstFiles = []
# Lista con todos los ficheros del directorio:
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros

# Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
 
for root, dirs, files in lstDir:
	for fichero in files:
		(nombreFichero, extension) = os.path.splitext(fichero)
		if(extension == ".RNO"):
			lstFiles.append(nombreFichero+extension)
			#print (nombreFichero+extension)
			 
print(lstFiles)            
print ('LISTADO FINALIZADO')
print ("longitud de la lista = ", len(lstFiles))
