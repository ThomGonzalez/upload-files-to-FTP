# -*- coding: cp1252 -*-

import ftplib
import os

# Datos FTP
ftp_servidor = 'server'
ftp_usuario  = 'user'
ftp_clave    = 'pass'
ftp_raiz     = '/public_html' # Carpeta del servidor donde queremos subir el fichero

# Datos del fichero a subir
# Ruta al fichero que vamos a subir
fichero_origen = r'C:/apache-maven-3.2.5-bin.zip'

fichero_destino = 'mifichero.zip' # Nombre que tendrá el fichero en el servidor
 
# Conectamos con el servidor
try:
	s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
	try:
		f = open(fichero_origen, 'rb')
		s.cwd(ftp_raiz)
		s.storbinary('STOR ' + fichero_destino, f)
		f.close()
		s.quit()
	except:
		print("No se ha podido encontrar el fichero")+fichero_origen
except:
	print("No se ha podido conectar al servidor")+ftp_servidor
