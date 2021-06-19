#creating custom module for scraping current date and time
#why use this? cause custom API are easy to remember and
#I don't have to scrape current date and time over and over again

from datetime import datetime
class Date:
	def __init__(self):
		self.__current=datetime.date(datetime.now())
		self.data=str(self.__current).split('-')
		self.year=self.data[0]
		self.date=self.data[2]
		self.month=self.data[1]
		self.date_int=int(self.data[2])
		
	def current_date(self):
		currentDate=self.date+'/'+self.month+'/'+self.year
		return currentDate

class Time:
	def __init__(self):
		self.current=datetime.time(datetime.now())
		self.data=str(self.current).split(':')
		self.hour=self.data[0]
		self.minute=self.data[1]
		self.seconds=self.data[2]

	def current_time(self):
		currentTime=self.hour+':'+self.minute+':'+self.seconds
		return currentTime

"""--EXAMPLE--"""
"""
time=Time()
date=Date()

print("Current time:\n")
print(time.current_time())

print("\nToday is: "+date.current_date())

"""