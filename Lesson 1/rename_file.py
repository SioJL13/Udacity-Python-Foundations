import os
def rename_files():
	#get the files names from a given folder
	file_list = os.listdir("/Users/siomarajimenezl/Documents/prank")
	#print file_list
	#working_path = os.getcwd
	#print working_path
	os.chdir("/Users/siomarajimenezl/Documents/prank")

	#for each file, rename filename
	for photos in file_list:
		#old,new
		print ("Old name "+ photos)
		os.rename(photos, photos.translate(None,"0123456789"))
		print("New name " + photos.translate(None,"0123456789"))
	print "Finished"


rename_files()
