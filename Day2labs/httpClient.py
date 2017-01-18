import requests

get = requests.get('https://swapi.co/api/planets/1/?format=wookiee')
print (get.json())