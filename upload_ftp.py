# -*- coding: cp1252 -*-
import ftplib
from libs.ziplib import GenerateZip
import os


class Base(object):
	''' Datos FTP para subir archivos al servidor.'''
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

	def archive_one(self):
		try:
			files = open(self.file_names, 'rb')
			self.server.cwd(self._ftp_raiz)
			self.server.storbinary('STOR '+ 'fichero.zip', files)
			files.close()
			self.server.quit()
		except:
			print('No se ha podido encontrar el fichero: '+self.file_names)
			return False
		return True 

	def archive_many(self):
		try:
			for fichero in self.file_names:
				files = open(fichero['archivo'], 'rb')
				self.server.cwd(self._ftp_raiz)
				self.server.storbinary('STOR '+fichero['nombre'], files)
				files.close()
			self.server.quit()
		except:
			print('No se ha podido encontrar el fichero: '+fichero['nombre'])
			return False
		return True


class UploadFile(Base):

	def __init__(self, **kwargs):
		super(UploadFile, self).__init__(**kwargs)

	@property
	def simple(self):
		return self.archive_one()

	@property
	def multiple(self):
		return self.archive_many()

	
# Lista de ficheros
ficheros = [
	{'nombre': 'apache1.zip', 'archivo': r'C:/apache-maven-3.2.5-bin.zip'},
	{'nombre': 'apache2.pdf', 'archivo': r'C:/ORGANIGRAMA_FORTIS.pdf'}
]
file_name = 'C:/apache-maven-3.2.5-bin.zip'

upload = UploadFile(file_names=file_name).simple
print(upload)
upload = UploadFile(file_names=ficheros).multiple
print(upload)


# Generar zip con varios directorios.
directorios = [
	{'dir':'C:\CFDI_JAVA', 'zip_file':'C:/Users/TomaS/repositorio/thomgonzalez/Upload-Files-to-FTP/test1.zip'},
	{'dir':'C:\BDRH', 'zip_file':'C:/Users/TomaS/repositorio/thomgonzalez/Upload-Files-to-FTP/test2.zip'},
]
zipper = GenerateZip(directorios=directorios).manydir
print(zipper)
