import zeep

#wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
#client = zeep.Client(wsdl=wsdl)
#print(client.service.Method1("ah meu deus como eh bom ser da botinha", "e tomar guarana"))

wsdl = 'QAjudaFinancas.wsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.vezesDois(3))