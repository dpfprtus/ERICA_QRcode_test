import requests #using VirusTotal API
url = 'https://www.virustotal.com/vtapi/v2/url/report'

params = {'apikey': '45448e873ecdaa8972640463c6172fd776464b71199089db8a6c81f9d9f065a2', 'resource':'site_address'}
response = requests.get(url, params=params)

print(response.json()) #data by json 

url = 'https://www.virustotal.com/vtapi/v2/url/scan'

params = {'apikey': '45448e873ecdaa8972640463c6172fd776464b71199089db8a6c81f9d9f065a2', 'url':'site_address'}

response = requests.post(url, data=params)

print(response.json())
