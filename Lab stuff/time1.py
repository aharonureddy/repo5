import time

print(time.time())
print(time.ctime(time.time()))

start = time.time()
for x in range(10000000):
	y=x*x
end = time.time()
print(end - start)

print("sleeping")
time.sleep(2)
print("wokeup")
