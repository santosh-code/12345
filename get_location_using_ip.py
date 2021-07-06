import requests
r = requests.get('https://get.geojs.io/')
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()['ip']
url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
geo_request = requests.get(url)
geo_data = geo_request.json()
geo_data = geo_request.json()
print(geo_data)
