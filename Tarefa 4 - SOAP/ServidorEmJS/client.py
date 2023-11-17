from zeep import Client

def main():
    # URL do servidor SOAP em JavaScript
    url_js = 'http://localhost:8000/QAjuda?wsdl'
    
    # Crie um cliente SOAP para o servidor em JavaScript
    client_js = Client(url_js)
    
    print('### QAjuda Investimentos')
    while True:
        print('\nMENU:')
        print('[ 1 ] Quero Ganhar X por mês')
        print('[ 2 ] Quero Investir X por mês')
        print('[ 3 ] Quanto devo gastar com moradia')
        print('[ 4 ] Plano de investimento')
        print('[ 0 ] Sair')
        op = input('> ')
        if op == '1':
            # Exemplo de chamada ao método QueroGanharX do servidor em JavaScript
            valor = float(input('Digite que deseja ganhar: '))
            anos = int(input('Digite o número de anos: '))
            result_quero_ganhar_x = client_js.service.QueroGanharX(valor=valor, anos=anos)
            print("Resultado QueroGanharX:", result_quero_ganhar_x.investimentoMensal)
        elif op == '2':
            # Exemplo de chamada ao método QueroInvestir do servidor em JavaScript
            valor = float(input('Digite o valor disponível para investir por mês: '))
            anos = int(input('Digite o número de anos: '))
            result_quero_investir = client_js.service.QueroInvestir(valor=valor, anos=anos)
            print("Resultado QueroInvestir:", result_quero_investir.montanteFinal)
        elif op == '3':
            # Exemplo de chamada ao método ValorMoradia do servidor em JavaScript
            sal = float(input('Digite o valor do salário: '))
            result_valor_moradia = client_js.service.ValorMoradia(sal=sal)
            print("Resultado ValorMoradia:", result_valor_moradia.mensagem)
        elif op == '4':
            # Exemplo de chamada ao método PlanoDeInvestimento do servidor em JavaScript
            sal = float(input('Digite o valor do salário: '))
            valor_aluguel = float(input('Digite o valor do aluguel: '))
            valor_bonus = float(input('Digite o valor do bônus: '))
            result_plano_investimento = client_js.service.PlanoDeInvestimento(sal=sal, valorAluguel=valor_aluguel, valorBonus=valor_bonus)
            plano = result_plano_investimento.plano
            print(f"Valor para férias: {plano['valorParaFerias']}")
            print(f"Valor investido durante o ano: {plano['valorInvestidoAno']}")
            print(f"Rendimento mensal: {plano['rendimentoMensal']}")
        elif op == '0':
            break
        else:
            print('[ --Opcao inválida!-- ]')

if __name__ == '__main__':
    main()
