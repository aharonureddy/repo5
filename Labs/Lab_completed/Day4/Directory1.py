# Create a class called Directory which can be initialized with a direcotry path.
# If the path does not exist, object creation should fail ( an exception should be thrown ).
# Add the following methods:
# a) getfiles - returns a list of all files in the directory
# b) getfilesbytype(extn) - returns a list of all files with the given extension, e.g: .py, .txt etc. 
# c) getfilesbysize(size) - returns a list of files with the specifed size.


import os

class Directory:
    def __init__(self,dirname):
        if os.path.exists(dirname):
            self.dir = dirname
            self.files=os.listdir(self.dir)
        else:
            raise Exception(f"{dirname} does not exist. Please check the path")
    def getfiles(self):
        return self.files
    
    def getfilesbytype(self,extn):
        flist=[]
        for file in self.files:
            if file.endswith(extn):
                flist.append(file)
        return flist

    def getfilesbysize(self,size):
        flist=[]
        for file in self.files:
            file=self.dir +"/"+file            # Form the absolute path
            if os.path.getsize(file) == size:
                flist.append(file)
        return flist



# Test the class
try:
    mydir = Directory("c://Prathith")
    print(mydir.getfiles())
    print(mydir.getfilesbytype('.txt'))
    print(mydir.getfilesbysize(1126))

    # mydir = Directory("c://pypractice") - non existent directory - raises exception
