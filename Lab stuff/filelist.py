import os

for myfile in os.listdir():
	print(os.path.getsize(myfile), myfile)