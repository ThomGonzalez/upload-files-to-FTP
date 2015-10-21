import datetime


class CurrentDate(object):

	def getDate(self):
		now = datetime.datetime.now()
		date = now.strftime('%d/%m/%Y %H:%M:%S')
		return date
