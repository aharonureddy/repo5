# Create a dictionary in which the keys are numbers
#within the range 1 to 20 and the value for each key is the cube of the number.

cubes={}
for n in range(1,21):
    cubes[n]=n**3
    
print(cubes)
