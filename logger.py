from utils import CurrentDate


class Log(object):
	
	_message = None

	def __init__(self, message):
		self._message = message
		self.existWriteFile()

	def readFile(self):
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

	def overWriteFile(self):
		""" 
		Crea un nuevo archivo o sobrescribe el contenido existente del archivo.
		Modo de escritura siempre destruir el contenido existente de un archivo.
		"""
		try:
			# Sobrescribir un archivo existente.
			f = open("file.txt", "w")
			try:
				# Escribe una cadena a un archivo.
				f.write('hola') 
				# Escribe una secuencia de cadenas a un archivo.
				f.writelines(lines) 
			finally:
				f.close()
		except IOError:
			pass
		 
	def existWriteFile(self):
		""" 
		Anexar al contenido existente, para mantener un archivo de registro. 
		Nunca dañar el contenido existente de un archivo.
		"""
		try:
			# Este intenta abrir un archivo existente,
			# sino que crea un nuevo archivo si es necesario.
			logfile = open("log.txt", "a")
			try:
				date = CurrentDate().getDate()
				logfile.write(self._message+' Fecha: %s \n' % str(date))
			finally:
				logfile.close()
		except IOError:
			pass
 

 
