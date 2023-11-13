from zeep import Client

# Substitua pela URL real do seu serviço
url_servico = 'http://localhost/CalcInvestimentos.asmx?wsdl'
cliente = Client(url_servico)

# Chame os métodos SOAP
resultado_quero_ganhar_x = cliente.service.QueroGanharX(valor=1000, anos=5)
resultado_quero_investir = cliente.service.QueroInvestir(valor=1000, anos=5)
resultado_valor_moradia = cliente.service.ValorMoradia(sal=5000)
resultado_plano_investimento = cliente.service.PlanoDeInvestimento(sal=50000, valorAluguel=1000, valorBonus=5000)

# Processe os resultados conforme necessário
print(resultado_quero_ganhar_x)
print(resultado_quero_investir)
print(resultado_valor_moradia)
print(resultado_plano_investimento)
