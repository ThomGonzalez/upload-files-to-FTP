from libs.ziplib import GenerateZip
from client_ftp import UploadFile


class Backup(object):

	def toserver(self):

		_BACKUPS = 'C:/backups/'

		directorios = [
			{ 'dir':'Y:', 'zip_file':''+_BACKUPS+'cfdi.zip'},
			{ 'dir':'X:', 'zip_file':''+_BACKUPS+'mssql.zip'},
		]

		zipper = GenerateZip(directorios=directorios).manydir
		if zipper:
			print('Generación archivos ZIP Finalizado : ', zipper)

			_RUTA = 'C:/backups/'
			ficheros = [
				{'nombre': 'backup-cfdi.zip', 'archivo': r''+_RUTA+'cfdi.zip'},
				{'nombre': 'backup-mssql.zip', 'archivo': r''+_RUTA+'mssql.zip'},
			]

			upload = UploadFile(file_names=ficheros).multiple
			if upload:
				print('Respaldo Finalizado : ', upload)

backup = Backup().toserver()
