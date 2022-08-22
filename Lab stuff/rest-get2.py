import requests

URL = "http://api.open-notify.org/astros.json"

response = requests.get(URL)

if response.ok:
	people = response.json().get('people')
	for person in people:
		print(person.get('name'))

