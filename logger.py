try:
	f = open("file.txt", "r")
	try:
		# Leer todo el archivo del contenido.
		string = f.read()
		# Leer una línea a la vez
		line = f.readline()
		# Leer todas las líneas en una lista.
		lines = f.readlines()
	finally:
		f.close()
except IOError:
	pass
 
 
""" 
Crea un nuevo archivo o sobrescribe el contenido existente del archivo.
Modo de escritura siempre destruir el contenido existente de un archivo.
"""
try:
	# Esto creará un nuevo archivo o ** sobrescribir un archivo existente **.
	f = open("file.txt", "w")
	try:
		f.write('hola') # Escribe una cadena a un archivo
		f.writelines(lines) # Write a sequence of strings to a file
	finally:
		f.close()
except IOError:
	pass
 
""" 
Anexar se suma al contenido existente, para mantener un archivo de registro. 
# Nunca dañar el contenido existente de un archivo.
"""
try:
	# Este intenta abrir un archivo existente, sino que crea un nuevo archivo si es necesario....
	logfile = open("log.txt", "a")
	try:
		logfile.write('log ')
	finally:
		logfile.close()
except IOError:
	pass