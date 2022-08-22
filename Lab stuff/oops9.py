import os
import time
class FileInfo:
	def __init__(self, filename):
		self.filename = filename
	def getsize(self):
		print(f"The size of the file is {os.path.getsize(self.filename)}")
	def getctime(self):
		print(f"The file was created at {time.ctime(os.path.getctime(self.filename))}")
	def getmtime(self):
		print(f"The file was modified at {time.ctime(os.path.getmtime(self.filename))}")
	def getatime(self):
		print(f"The file was last accessed at {time.ctime(os.path.getatime(self.filename))}")



class NewFileInfo(FileInfo):
	def getpath(self):
		print(f"This is the path {os.path.abspath(self.filename)}")


f=NewFileInfo("oops1.py")

f.getsize()
f.getctime()
f.getmtime()
f.getatime()
f.getpath()