# -*- coding: cp1252 -*-
import ftplib
import os


class Base(object):
	'''
	Datos FTP para subir archivos al servidor.
	'''
	_ftp_servidor = 'server'
	_ftp_usuario = 'user'
	_ftp_password = 'pass'
	_ftp_raiz = '/public_html'

	def __init__(self, file_names=None):
		self.file_names = file_names
		self.conexion()

	def conexion(self):
		''' Conectamos con el servidor '''
		try:
			self.server = ftplib.FTP(self._ftp_servidor, self._ftp_usuario, self._ftp_password)
		except:
			print('No se ha podido conectar al servidor: '+self._ftp_servidor)

	def simple_upload(self):
		try:
			files = open(self.file_names, 'rb')
			self.server.cwd(self._ftp_raiz)
			self.server.storbinary('STOR '+ 'fichero.zip', files)
			files.close()
			self.server.quit()
		except:
			print('No se ha podido encontrar el fichero: '+self.file_names)
		return True 

	def multiple_upload(self):
		try:
			for fichero in self.file_names:
				files = open(fichero['archivo'], 'rb')
				self.server.cwd(self._ftp_raiz)
				self.server.storbinary('STOR '+fichero['nombre'], files)
				files.close()

			self.server.quit()
		except:
			print('No se ha podido encontrar el fichero: '+fichero['nombre'])
		return True

class UploadFile(Base):

	_estatus = None

	def __init__(self, **kwargs):
		super(UploadFile, self).__init__(**kwargs)
		self._estatus = self.multiple_upload()

	@property
	def data(self):
	    return self._estatus
	
# Lista de ficheros
ficheros = [
	{'nombre': 'apache1.zip', 'archivo': r'C:/apache-maven-3.2.5-bin.zip'},
	{'nombre': 'apache2.zip', 'archivo': r'C:/apache-maven-3.3.1-bin.zip'}
]

upload = UploadFile(file_names=files).data
print(upload)
