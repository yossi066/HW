import requests

def getCityPos(cityName):
    g_address = 'http://maps.googleapis.com/maps/api/geocode/json?address='
    city_info = requests.get(g_address+cityName )
    if city_info.status_code != 200:
        # This means something went wrong.
        raise requests.RequestException('GET ERROR {}'.format(city_info.status_code))
    j_city_info = city_info.json()
    lat= (j_city_info['results'][0]['geometry']['location']['lat'])
    lng=(j_city_info['results'][0]['geometry']['location']['lng'])
    return (lat,lng)

def getTemperature(lat,lng):
    resp = requests.get('https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/'+ str(lat) + ','+ str(lng) )
    if resp.status_code != 200:
        # This means something went wrong.
        raise requests.RequestException('GET ERROR {}'.format(resp.status_code))
    j_resp = resp.json()
    timeZone=(j_resp['timezone'])
    f_temp=(j_resp['currently']['temperature'])
    c_temp = round((f_temp - 32) * (5/9) , 2)
    return (timeZone,str(c_temp))


cityName = input('Enter your city : ')
lat,lng = getCityPos(cityName)
timeZone,temperature= getTemperature(lat,lng)
print ('Your time zone is : '+ timeZone)
print ('Your temperature is : '+ temperature + ' celsius')
