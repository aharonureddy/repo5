import json

capitals = {'India':'New Delhi',
			"Russia":'Moscow'}

f=open("sample.json","w")
json.dump(capitals, f)
f.close()