# http://api.openweathermap.org/data/2.5/weather?q=Lundtofte,dk

"""
{"coord":{"lon":10.59,"lat":55.07},"sys":{"message":0.0366,"country":"Denmark","sunrise":1398656544,"sunset":1398710865},"weather":[{"id":800,"main":"Clear","description":"Sky is Clear","icon":"01d"}],"base":"cmc stations","main":{"temp":284.627,"temp_min":284.627,"temp_max":284.627,"pressure":1023.87,"sea_level":1025.67,"grnd_level":1023.87,"humidity":82},"wind":{"speed":3.32,"deg":52.5},"clouds":{"all":0},"dt":1398677467,"id":2612045,"name":"Svendborg","cod":200}
"""
import sys
import urllib2
import json
import pdb

try:
	sted = sys.argv[1]
	land = sys.argv[2]
	url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s' % (sted, land) # kommentar
	response = urllib2.urlopen(url)
	data = json.load(response)
	print data['weather'][0]['description']

except:
	# Her burde man fange specifikke fejl
	print 'Der gik noget galt'
	sys.exit(1)
finally:
	print 'Afslutter...'



"""
{u'clouds': 
	{
		u'all': 0
	}, 
	u'name': u'Copenhagen', 
	u'coord': {u'lat': 55.68, u'lon': 12.57}, 
	u'sys': {
		u'country': u'DK', 
		u'message': 0.04, 
		u'sunset': 1398710521, 
		u'sunrise': 1398655939}, 
		u'weather': 
			[{
				u'main': u'Clear', 
				u'id': 800, 
				u'icon': u'01d', 
				u'description': u'Sky is Clear'
		}], 
		u'cod': 200, 
		u'base': u'cmc stations', 
		u'dt': 1398675349, 
		u'main': {
			u'pressure': 1015, 
			u'temp_min': 286.15, 
			u'temp_max': 291.48, 
			u'temp': 288.45, 
			u'humidity': 43
		}, 
		u'id': 2618425, 
		u'wind': {
			u'var_end': 50, 
			u'var_beg': 330, 
			u'speed': 2.1, 
			u'deg': 10
		}
	 }
"""