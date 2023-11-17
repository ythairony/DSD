import zeep

wsdl = 'weatherService.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.getWeather('new york'))