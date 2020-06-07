#!/usr/bin/python3
#Emre Ertürk 170709007


import os
import requests	
import sys
from multiprocessing import Pool
from multiprocessing import Process
import glob
import shutil
import urllib.request
import hashlib
import threading



print("parent process id: " , os.getpid())			#Print parent id to screen.
pid = os.fork()							#Create child process using fork.

if (pid > 0):							#If pid of process is greater than 0 that means it is parent process.
	os.wait()						#os.wait() method is used by a process to wait for completion of a child process.


if (pid == 0):							#If pid of process is equal to 0 that means it is child process.
	print("child process id: ", os.getpid())		#Print child id to screen.

	array =["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg", "http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]

	
	file_name = ["1.jpeg", "2.png", "3.jpg", "4.jpeg", "5.jpg"]		#I gave name to every photo. My hash_controller function needs directory as parameter. If I used uuid4 technique I could not check duplicate files using multiprocessing method. I need .jpeg .png and .jpg types.


	

	
	def download_file(url, file_name):
		
		r = requests.get(url, stream = True)				#requests.get method makes a request to a url, and return the status code.
		if r.status_code == 200:					#If status code equal to 200 that means url is working.
			r.raw.decode_content = True				#For requests the work-around is to set the decode_content attribute on the raw object to True.

			with open(file_name, 'wb') as f:			#Create a file named file_name. 'wb' means write and binary.
				shutil.copyfileobj(r.raw, f)			#shutil.copyfileobj() method is used to copy the contents of a file object to another file object.

			print("Image Downloaded------>", file_name)		#Print information and file_name
		else:
			print("!!!Image Couldn't Downloaded!!!")		#Print if image was not downloaded



	
	
	for x in range(len(array)):						#
		download_file(array[x], file_name[x])				#For every element in the array call download_file and give name from file_name array  


	os._exit(0)								#os.exit(0) method is used to exit the process.
	
directory1= glob.glob("/home/emre/Desktop/final/*.jpeg")			#I used globl library becasue i wanted to assign directory to variable.
directory2= glob.glob("/home/emre/Desktop/final/*.png")
directory3= glob.glob("/home/emre/Desktop/final/*.jpg")


def hash_controller(directory):
	
	hash_list = []								#An array that get hash codes of images
	for f in directory:
		with open(f, "rb") as file:					#file.read() method for reading the content of the file.
			data = file.read()
			gethash = hashlib.md5(data).hexdigest()			#Convert to hexdigest hash code and assing to gethash varible.
			hash_list.append(gethash)				#Add hash codes to an array.
			print("Scanning......." + ": " + f)				#Print file name
			print("Hash code of file " + " is: " + gethash + "\n")	#Print hash code and file name								
	for i in range(0, len(hash_list)):					#This for loop for the finding duplicate hash codes
		for j in range(i + 1, len(hash_list)):
			if hash_list[i] == hash_list[j]:
				print("********************")
				print("Duplicate files found")
				print("This hash code was found two times: " + hash_list[i])
				print("********************")
			

p = Pool(2)									#Multiprocessing pool method.
p.map(hash_controller, [directory1, directory2, directory3])



'''
p1 = Process(target=hash_controller, args=(directory1,))			#Process object calling its start() method. Process follows the API of threading.Thread
p2 = Process(target=hash_controller, args=(directory2,))
p1.start()
p2.start()
'''

'''
t1 = threading.Thread(target=hash_controller, args=(directory1,))		#Usage of threading.
t2 = threading.Thread(target=hash_controller, args=(directory2,))
t3 = threading.Thread(target=hash_controller, args=(directory3,))
t1.start()
t2.start()
t3.start()
'''

'''
hash_controller(directory1)							#Normal usage of functions
hash_controller(directory2)
hash_controller(directory3)
'''



































