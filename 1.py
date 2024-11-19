import requests


r = requests.get('https://random-d.uk/api/list', params=[])
print(r.text)