import sys
import filecmp

# how to handle command line parameters

file1 = sys.argv[1]
file2 = sys.argv[2]

print(filecmp.cmp(file1, file2))
