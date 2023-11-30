import zeep

wsdl = 'tarotService.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.TarotRequest(past=True, present=False, future=False, all=False))