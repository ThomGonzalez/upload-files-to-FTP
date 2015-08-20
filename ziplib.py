import os
import zipfile


class Base(object):	

	def __init__(self, path_file=None):
		self.path_file = path_file

	def zip_one(self):
		''' Comprime solo un archivo. '''
		zipf = zipfile.ZipFile('ejemplo.zip', 'w', zipfile.ZIP_DEFLATED)
		zipf.write(self.path_file)
		zipf.close()
		return True

	def zipper(self, dir=None, zip_file=None):
		''' Zip directorios de forma recursiva '''
		zipf = zipfile.ZipFile(zip_file, 'w', compression=zipfile.ZIP_DEFLATED)
		root_len = len(os.path.abspath(dir))
		for root, dirs, files in os.walk(dir):
			archive_root = os.path.abspath(root)[root_len:]
			for f in files:
				fullpath = os.path.join(root, f)
				archive_name = os.path.join(archive_root, f)
				print(f)
				zipf.write(fullpath, archive_name, zipfile.ZIP_DEFLATED)
		zipf.close()
		return zip_file



class GenerateZip(Base):
	
	def __init__(self, **kwargs):
		super(GenerateZip, self).__init__(**kwargs)

	@property		
	def simple(self):
		return self.zip_one()


path_file = "C:\CFDI_JAVA\CFDI-DEMO.xml"
#self.simple(path=path, nombre=nombre)
#self.zipper(dir='C:\CFDI_JAVA', zip_file='C:/zipfile/test.zip')
zipp = GenerateZip(path_file=path_file).simple
print(zipp)
