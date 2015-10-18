from libs.ziplib import GenerateZip
from client_ftp import UploadFile
from logger import Log

class Backup(object):

	def executeBackups(self):

		_BACKUPS = 'C:/backups/'

		data = [
			{ 'ruta':'C:/test1', 'nombreArchivo': _BACKUPS+'test1.zip'},
			{ 'ruta':'C:/test2', 'nombreArchivo': _BACKUPS+'test2.zip'},
		]

		zipper = GenerateZip(directorios=data).directories
		if zipper:
			Log(message='ZIP: Se generaron los archivos correctamente.')

			_RUTA = 'C:/backups/'
			ficheros = [
				{'nombre': 'test1.zip', 'archivo': r''+_RUTA+'test1.zip'},
				{'nombre': 'test2.zip', 'archivo': r''+_RUTA+'test2.zip'},
			]

			upload = UploadFile(file_names=ficheros).multiple
			if upload:
				print('Respaldo Finalizado : ', upload)

backup = Backup().executeBackups()
