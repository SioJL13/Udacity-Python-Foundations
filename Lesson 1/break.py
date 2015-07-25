import webbrowser
import time
import sys

#Original mini-project that opens a website every 10 seconds
#we choose to have 3 breaks.
def original():
	breaks = 3
	counter = 0

	print("This program started on: " + time.ctime())
	while(breaks != counter):
		time.sleep(10)
		webbrowser.open("http://www.youtube.com")
		counter +=1

#This version takes argument inside the command line using the sys library.
def improved():
	try:
		if (type(int(sys.argv[1])) is int and len(sys.argv[1]) > 1) and len(sys.argv[2])>2:
			time_interval = sys.argv[1]
			url = sys.argv[2]
			#print time_interval
			#print url
	except:
		print "Page and time not found. Opening default url and time"
		time_interval = 10
		url = "http://www.reddit.com"

		for breaks in range(0,3):
			time.sleep(float(time_interval))
			webbrowser.open(url)

improved()
