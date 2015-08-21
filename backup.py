from libs.ziplib import GenerateZip
from client_ftp import UploadFile


class Backup(object):

	def toserver(self):
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
			print('Generación archivos ZIP Finalizado : ',zipper)
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
			if upload:
				print('Respaldo Finalizado : ',upload)

backup = Backup().toserver()
