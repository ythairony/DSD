from spyne import Application, ServiceBase, Unicode, rpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

class QAjudaService(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def QueroGanharX(self, valor, anos):
        valor = float(valor)
        anos = float(anos)

        taxa_mes = 0.009

        montante_estimado = valor / taxa_mes

        taxa_anual = ((1 + taxa_mes) ** 12) - 1

        taxa_real = taxa_anual / 12

        investimento_mensal = montante_estimado / (((1 + taxa_real) ** (anos * 12) - 1) / taxa_real) * (1 + taxa_real)

        total_investido = investimento_mensal * (anos * 12)

        return f"Terá que investir {investimento_mensal:.2f} por mês paraa atingir a renda de {total_investido:.2f}"


    @rpc(Unicode, Unicode, _returns=Unicode)
    def QueroInvestir(self, valor, anos):
        try:
            valor = float(valor)
            anos = float(anos)
            taxa_mes = 0.009
            taxa_anual = ((1 + taxa_mes) ** 12) - 1
            taxa_real = taxa_anual / 12

            montante_final = valor * (((1 + taxa_real) ** (anos * 12) - 1) / taxa_real) * (1 + taxa_real)

            total_investido = valor * (anos * 12)
            renda_passiva = montante_final * taxa_mes

            return f"Seu investimento após {anos} anos será de: {total_investido:.2f}, seu patrímonio acumulado será: {montante_final:.2f} e seu renda passiva será: {renda_passiva:.2f}"
        except ValueError:
            return "Os valores fornecidos não são números válidos."

    @rpc(Unicode, _returns=Unicode)
    def ValorMoradia(self, sal):
        sal = float(sal)
        # Sua lógica para ValorMoradia aqui
        return f"Seu valor com aluguel ou parcela de financiamento deverá ser no máximo {float(sal)/3:.2f}."

    @rpc(Unicode, Unicode, Unicode, _returns=Unicode)
    def PlanoDeInvestimento(self, sal, valorAluguel, valorBonus):
        valor_para_investir = ((sal - valor_aluguel) * 0.1) * 12
        valor_para_investir += valor_bonus * 0.5
        valor_para_investir += sal * 0.7

        valor_para_ferias = (sal / 3) + (sal * 0.3)

        resultado = {
            "valorParaFerias": valor_para_ferias,
            "valorInvestidoAno": valor_para_investir,
            "rendimentoMensal": valor_para_investir * 0.009
        }

        return f"O valor a ser gasto com suas férias é de {resultado['valorParaFerias']:.2f}\nValor investido durante o ano será {resultado['valorInvestidoAno']:.2f}\nSeu valor investido renderá {resultado['rendimentoMensal']:.2f} todos os meses no ano seguinte."


if __name__ == '__main__':
    application = Application([QAjudaService], 'qajudaservice.soap', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
    wsgi_application = WsgiApplication(application)

    # server = make_server('127.0.0.1', 8000, wsgi_application)
    server = make_server('10.24.24.9', 8000, wsgi_application)

    # print("Servidor SOAP rodando em http://127.0.0.1:8000")
    print("Servidor SOAP rodando em http://10.24.24.9:8000")
    server.serve_forever()
