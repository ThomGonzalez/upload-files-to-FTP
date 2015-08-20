import os
import zipfile


class Base(object):	

	def __init__(self, **kwargs):
		self._pathfile = kwargs.get('pathfile')
		self._directorio = kwargs.get('directorio')

	def zip_one(self):
		''' Comprime solo un archivo. '''
		self.nombre = self._pathfile[0]
		self.dir = self._pathfile[1]
		zipf = zipfile.ZipFile(self.nombre, 'w', zipfile.ZIP_DEFLATED)
		zipf.write(self.dir)
		zipf.close()
		return True

	def zip_dir(self):
		''' Zip directorios de forma recursiva '''
		zipf = zipfile.ZipFile(self._directorio['zip_file'], 'w', compression=zipfile.ZIP_DEFLATED)
		root_len = len(os.path.abspath(self._directorio['dir']))
		for root, dirs, files in os.walk(self._directorio['dir']):
			archive_root = os.path.abspath(root)[root_len:]
			for f in files:
				fullpath = os.path.join(root, f)
				archive_name = os.path.join(archive_root, f)
				print(f)
				zipf.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
		zipf.close()
		return self._directorio['zip_file']


class GenerateZip(Base):
	
	def __init__(self, **kwargs):
		super(GenerateZip, self).__init__(**kwargs)

	@property		
	def simple(self):
		return self.zip_one()

	@property	
	def directorios(self):
		return self.zip_dir()


path_file = ('ejemplo.zip', 'C:\CFDI_JAVA\CFDI-DEMO.xml')
directorio = {'dir':'C:\CFDI_JAVA', 'zip_file':'C:/Users/TomaS/repositorio/thomgonzalez/Upload-Files-to-FTP/test.zip'}

zipp = GenerateZip(pathfile=path_file).simple
print(zipp)
zipp = GenerateZip(directorio=directorio).directorios
print(zipp)
