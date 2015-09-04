import os.path, time
from time import ctime

class Base(object):
	
	_file = None

	def __init__(self, ruta):
		self._ruta = ruta

	def creation_date(self):
		# Current time
		date_now = ctime()
		date_create = time.ctime(os.path.getctime(self._ruta))
		if date_now is date_create:
			self._file = self._ruta

		return self._file

	def modification_date(self):
		# Last modified
		date_modified = time.ctime(os.path.getmtime(self._ruta))
		return date_modified

class ReadFiles(Base):
	pass

ruta_file=r'C:/Users/BlackStar/Pictures/logo.jpg'
files = ReadFiles(ruta=ruta_file).creation_date()
print(files)



