# -*- coding: cp1252 -*-
import ftplib
import os


class Base(object):
	'''
	Datos FTP
	'''
	_ftp_servidor = 'server'
	_ftp_usuario = 'user'
	_ftp_password = 'pass'
	_ftp_raiz = '/public_html'

	def __init__(self, filenames=None):
		self.fichero_origen = filenames

	def conexion(self):
		''' 
		Conectamos con el servidor 
		'''
		try:
			server = ftplib.FTP(self._ftp_servidor, self._ftp_usuario, self._ftp_password)
			try:
				files = open(self.fichero_origen, 'rb')
				server.cwd(self._ftp_raiz)
				server.storbinary('STOR ' + 'mifichero.zip', files)
				files.close()
				server.quit()
			except:
				print('No se ha podido encontrar el fichero %s') %(self.fichero_origen,)
		except:
			print('No se ha podido conectar al servidor %s') %(self._ftp_servidor,)

		return True


class UploadFile(Base):

	_estatus = None

	def __init__(self, **kwargs):
		super(UploadFile, self).__init__(**kwargs)
		self._estatus = self.conexion()

	@property
	def data(self):
	    return self._estatus
	
# Ruta del fichero
fichero_origen = r'C:/apache-maven-3.2.5-bin.zip'
upload = UploadFile(filenames=fichero_origen).data
print(upload)
