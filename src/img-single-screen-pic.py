import sys
from PIL import ImageGrab


def sc(path):
	im = ImageGrab.grab()
	im.save(path)

if __name__=="__main__":
	arglen=len(sys.argv)
	if(arglen!=2):
		print("Usage: sc xxx.png")
	else:
		path = sys.argv[1]
		sc(path)