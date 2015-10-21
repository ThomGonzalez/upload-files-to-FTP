# -*- coding: cp1252 -*-
from libs import ftplib
import os
from logger import Log


class Base(object):
	"""
	Datos FTP para subir archivos al servidor y conexion.
	"""
	_ftp_servidor = 'server'
	_ftp_usuario = 'user'
	_ftp_password = 'pass'
	_ftp_raiz = '/public_html'

	def __init__(self, file_names=None):
		self.file_names = file_names
		self.conexion()

	def conexion(self):
		try:
			self.server = ftplib.FTP(self._ftp_servidor,
									self._ftp_usuario,
									self._ftp_password)
		except:
			message = 'FTP: No se ha podido conectar al servidor.'
			Log(message=message+self._ftp_servidor)

	def archive(self):
		try:
			files = open(self.file_names, 'rb')
			self.server.cwd(self._ftp_raiz)
			self.server.storbinary('STOR '+ 'fichero.zip', files)
			files.close()
			self.server.quit()
		except:
			message = 'No se ha podido encontrar el fichero'
			Log(message=message+self.file_names)
			return False
		return True 

	def archives(self):
		try:
			for fichero in self.file_names:
				files = open(fichero['archivo'], 'rb')
				self.server.cwd(self._ftp_raiz)
				self.server.storbinary('STOR '+fichero['nombre'], files)
				files.close()
			self.server.quit()
		except:
			message = 'No se ha podido encontrar el fichero'
			Log(message=message+fichero['nombre'])
			return False
		return True


class UploadFile(Base):

	def __init__(self, **kwargs):
		super(UploadFile, self).__init__(**kwargs)

	@property
	def default(self):
		return self.archive()

	@property
	def multiple(self):
		return self.archives()

