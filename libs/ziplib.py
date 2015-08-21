import zipfile
import os


class Base(object):	

	def __init__(self, **kwargs):
		self._pathfile = kwargs.get('pathfile')
		self._directorio = kwargs.get('directorio')
		self._directorios = kwargs.get('directorios')

	def zipfile_one(self):
		''' Comprime solo un archivo. '''
		self.nombre = self._pathfile[0]
		self.dir = self._pathfile[1]
		zipf = zipfile.ZipFile(self.nombre, 'w', zipfile.ZIP_DEFLATED)
		zipf.write(self.dir)
		zipf.close()
		return True

	def zipfile_many(self):
		pass

	def zipfile_dir(self):
		''' Zip directorios de forma recursiva '''
		zipf = zipfile.ZipFile(self._directorio['zip_file'], 'w', compression=zipfile.ZIP_DEFLATED)
		root_len = len(os.path.abspath(self._directorio['dir']))
		for root, dirs, files in os.walk(self._directorio['dir']):
			archive_root = os.path.abspath(root)[root_len:]
			for f in files:
				fullpath = os.path.join(root, f)
				archive_name = os.path.join(archive_root, f)
				zipf.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
		zipf.close()
		return self._directorio['zip_file']

	def zipfile_manydir(self):
		''' Zip comprime lista de directorios '''
		for item in self._directorios:
			zipf = zipfile.ZipFile(item['zip_file'], 'w', compression=zipfile.ZIP_DEFLATED)
			root_len = len(os.path.abspath(item['dir']))
			for root, dirs, files in os.walk(item['dir']):
				archive_root = os.path.abspath(root)[root_len:]
				for f in files:
					fullpath = os.path.join(root, f)
					archive_name = os.path.join(archive_root, f)
					zipf.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
		zipf.close()
		return True


class GenerateZip(Base):
	
	def __init__(self, **kwargs):
		super(GenerateZip, self).__init__(**kwargs)

	@property		
	def file(self):
		return self.zipfile_one()

	@property	
	def filedir(self):
		return self.zipfile_dir()

	@property
	def manydir(self):
	    return self.zipfile_manydir()
	
# Documentación 
# Generar zip con un archivo.
path = ('test.zip', 'C:\CFDI_JAVA\CFDI-DEMO.xml')
zipper = GenerateZip(pathfile=path).file

# Generar zip con un direcctorio
#dir_zip = {'dir':'C:\JAVA', 'zip_file':'C:/Users/thomgonzalez/test.zip'}
#zipper = GenerateZip(directorio=dir_zip).filedir

# Generar zip con varios directorios.
#directorios = [
#	{'dir':'C:\JAVA', 'zip_file':'C:/Users/thomgonzalez/test1.zip'},
#	{'dir':'C:\BDRH', 'zip_file':'C:/Users/thomgonzalez/test2.zip'},
#]
#zipper = GenerateZip(directorios=directorios).manydir
