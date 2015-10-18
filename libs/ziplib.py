import sys
import os
import zipfile


class Base(object):	
	
	_directorios = []

	def __init__(self, **kwargs):
		self._pathfile = kwargs.get('pathfile')
		self._directorio = kwargs.get('directorio')
		self._directorios = kwargs.get('directorios')

	#Comprime solo un archivo.
	def fileZip(self):
		self.nombre = self._pathfile[0]
		self.ruta = self._pathfile[1]
		zipf = zipfile.ZipFile(self.nombre, 'w', zipfile.ZIP_DEFLATED)
		zipf.write(self.ruta)
		zipf.close()
		return True

	#Zip directorios de forma recursiva
	def directoryZip(self):
		zipf = zipfile.ZipFile(self._directorio['nombreArchivo'], 'w', compression=zipfile.ZIP_DEFLATED)
		root_len = len(os.path.abspath(self._directorio['ruta']))
		for root, dirs, files in os.walk(self._directorio['ruta']):
			archive_root = os.path.abspath(root)[root_len:]
			for f in files:
				fullpath = os.path.join(root, f)
				archive_name = os.path.join(archive_root, f)
				zipf.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
		zipf.close()
		return self._directorio['nombreArchivo']

	""" 
	Método comprime archivos .zip de lista de directorios.
	"""
	def manyDirectoryZip(self):
		try:
			for item in self._directorios:
				zipf = zipfile.ZipFile(item['nombreArchivo'], 'w', zipfile.ZIP_DEFLATED, allowZip64=True)
				root_len = len(os.path.abspath(item['ruta']))
				for root, dirs, files in os.walk(item['ruta']):
					archive_root = os.path.abspath(root)[root_len:]
					for f in files:
						fullpath = os.path.join(root, f)
						archive_name = os.path.join(archive_root, f)
						zipf.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
						print('ruta: ',root)
						print(f)
			zipf.close()
			return True
		except Exception as e:
			error = {'message': e.args}
			print('error', error['message'])
			return False


class GenerateZip(Base):
	
	def __init__(self, **kwargs):
		super(GenerateZip, self).__init__(**kwargs)

	@property		
	def file(self):
		return self.fileZip()

	@property	
	def directory(self):
		return self.directoryZip()

	@property
	def directories(self):
	    return self.manyDirectoryZip()
