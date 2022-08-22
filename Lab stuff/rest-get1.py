import requests
import time

URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(URL)

if response.ok:
	print(response.json())
	long = response.json().get('iss_position').get('longitude')
	lat = response.json().get('iss_position').get('latitude')
	timestamp = response.json().get('timestamp')

	print(f"ISS is at the location {lat},{long}, at {time.ctime(timestamp)}")

"""
import requests

URL = "http://api.open-notify.org/iss-now.json"

response = requests.get(URL)

if response.ok:
	print(response.json())
"""