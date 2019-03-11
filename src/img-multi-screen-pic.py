import sys
import os
import random
import time
from PIL import ImageGrab

#

def sc(folderpath,sleeptime):
	if not os.path.exists(folderpath):
		os.makedirs(folderpath)
		count = 0;
		while True:
			randomname = random.uniform(1,10)
			filename =folderpath.rstrip()+"\\"+str(randomname)+'-'+str(count)+".png"
			if os.path.exists(filename):
				continue
			im = ImageGrab.grab()
			im.save(filename)
			time.sleep(int(sleeptime))
			count=count+1
	else:
		count = 0;
		while True:
			randomname = random.uniform(1,10)
			filename =folderpath.rstrip()+"\\"+str(randomname)+'-'+str(count)+".png"
			if os.path.exists(filename):
				continue
			im = ImageGrab.grab()
			im.save(filename)
			time.sleep(int(sleeptime))
			count=count+1
def scmax(folderpath,sleeptime,maxnum):
	if not os.path.exists(folderpath):
		os.makedirs(folderpath)
		count = 0;
		while count<int(maxnum):
			randomname = random.uniform(1,10)
			filename =folderpath.rstrip()+"\\"+str(randomname)+'-'+str(count)+".png"
			if os.path.exists(filename):
				continue
			im = ImageGrab.grab()
			im.save(filename)
			time.sleep(int(sleeptime))
			count=count+1
	else:
		count = 0;
		while count<int(maxnum):
			randomname = random.uniform(1,10)
			filename =folderpath.rstrip()+"\\"+str(randomname)+'-'+str(count)+".png"
			if os.path.exists(filename):
				continue
			im = ImageGrab.grab()
			im.save(filename)
			time.sleep(int(sleeptime))
			count=count+1

if __name__=="__main__":
	arglen=len(sys.argv)
	if(arglen!=5 and arglen!=7):
		print("Usage: \r\nsc -o save_path -t sleep_time\r\nsc -o save_path -t sleep_time -m maxnum")
	elif arglen==5:
		folder_save_path = sys.argv[2]
		sleeptime = sys.arg[4]
		sc(folder_save_path,sleeptime)
	elif arglen==7:
		folder_save_path = sys.argv[2]
		sleeptime = sys.argv[4]
		maxnum = sys.argv[6]
		scmax(folder_save_path,sleeptime,maxnum)	