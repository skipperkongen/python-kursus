# VEJR LIB

"""
{"coord":{"lon":10.59,"lat":55.07},"sys":{"message":0.0366,"country":"Denmark","sunrise":1398656544,"sunset":1398710865},"weather":[{"id":800,"main":"Clear","description":"Sky is Clear","icon":"01d"}],"base":"cmc stations","main":{"temp":284.627,"temp_min":284.627,"temp_max":284.627,"pressure":1023.87,"sea_level":1025.67,"grnd_level":1023.87,"humidity":82},"wind":{"speed":3.32,"deg":52.5},"clouds":{"all":0},"dt":1398677467,"id":2612045,"name":"Svendborg","cod":200}
"""
import urllib2
import json

# function
def hent_vejr(bynavn, landekode):
	print 'Henter vejr for',bynavn, landekode
	try:
		url = 'http://api.openweathermap.org/data/2.5/weather?q=%s,%s' % (bynavn, landekode)
		#print url
		response = urllib2.urlopen(url)
		data = json.load(response)
		return data['weather'][0]['description']
	
	except:
		# Her burde man fange specifikke fejl
		return 'Vejr kunne ikke hentes for bynavn, landekode'

if __name__=='__main__':
	print hent_vejr('Lund', 'dk')