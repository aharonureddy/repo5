import filecmp

file1 = "factorial.py"
file2 = "functions1.py"

print(filecmp.cmp(file1, file2))