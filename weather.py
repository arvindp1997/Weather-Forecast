import urllib
import json
import urllib.request
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
city = "dhamra"
apikey = "8272b6c5d8c3dcb24afc605eff6290a4"
u = api_endpoint + "?q=" + city + "&appid=" + apikey
with urllib.request.urlopen(u) as url:
    response = url.read()
parseResponse = json.loads(response.decode('utf-8'))
temperature = parseResponse['main']['temp']
weather = parseResponse['weather'][0]['description']

F = (9.0/(5.0 * temperature)) + 32
print (F)
print (weather)
