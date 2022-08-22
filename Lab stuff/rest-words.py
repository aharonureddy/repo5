import requests

URL = 'http://garuda.pythonanywhere.com/words'


# GET the meaning of the word water

print(requests.get(URL + "/water").json())


# POST to create a new word and meaning
print(requests.get(URL + "/wellsfargo").json())

payload = {"word":"wellsfargo", "meaning":"bank"}

print(requests.post(URL, data=payload).json())

print(requests.get(URL + "/wellsfargo").json())


# PUT to update an existing word

payload = {"word":"wellsfargo", "meaning":"A Gobal Bank based in the USA"}

print(requests.put(URL, data=payload).json())

print(requests.get(URL + "/wellsfargo").json())


# DELETE

print(requests.delete(URL + "/wellsfargo").json())
print(requests.get(URL + "/wellsfargo").json())

