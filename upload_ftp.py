# -*- coding: cp1252 -*-
from libs import ftplib
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

''' Doc '''
# Subir un archivo al servidor
#file_name = 'C:/test.zip'
#upload = UploadFile(file_names=file_name).simple

# Generar zip con varios directorios.
_BACKUPS = 'C:/Users/TomaS/backups/'
_REPORTE = 'C:/xampp/htdocs/nomi-reporte'
_REPOSITORIO = 'C:/Users/TomaS/repositorio/nomiservicios/'

directorios = [
	{ 'dir':'Y:', 'zip_file':''+_BACKUPS+'cfdi.zip'},
	{ 'dir':'X:', 'zip_file':''+_BACKUPS+'mssql.zip'},
	{ 'dir':'W:', 'zip_file':''+_BACKUPS+'mysql.zip'},
	{ 'dir':''+_REPOSITORIO+'api-nomiserv', 'zip_file':''+_BACKUPS+'apinomiserv.zip'},
	{ 'dir':''+_REPOSITORIO+'', 'zip_file':''+_BACKUPS+'nomiserv.zip'},
	{ 'dir':''+_REPOSITORIO+'', 'zip_file':''+_BACKUPS+'docmycloud.zip'},
	{ 'dir':''+_REPORTE+'', 'zip_file':''+_BACKUPS+'nomireporte.zip'}
]

zipper = GenerateZip(directorios=directorios).manydir
if zipper:
	# Subir lista de ficheros
	_RUTA = 'C:/Users/TomaS/backups/'
	ficheros = [
		{'nombre': 'backup-cfdi.zip', 'archivo': r''+_RUTA+'cfdi.zip'},
		{'nombre': 'backup-mssql.zip', 'archivo': r''+_RUTA+'mssql.zip'},
		{'nombre': 'backup-mysql.zip', 'archivo': r''+_RUTA+'mysql.zip'},
		{'nombre': 'backup-apinomiserv.zip', 'archivo': r''+_RUTA+'apinomiserv.zip'},
		{'nombre': 'backup-nomiserv.zip', 'archivo': r''+_RUTA+'nomiserv.zip'},
		{'nombre': 'backup-docmycloud.zip', 'archivo': r''+_RUTA+'docmycloud.zip'},
		{'nombre': 'backup-nomireporte.zip', 'archivo': r''+_RUTA+'nomireporte.zip'}
	]
	upload = UploadFile(file_names=ficheros).multiple
	print('Respaldo Finalizado : ',upload)

