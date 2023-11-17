from zeep import Client

url = 'http://localhost:8000/calculator?wsdl'
client = Client(url)

print('Bem vindo à calculadora financeira QAjuda! escolha uma opção:')
opt = int(input())

# Case 1: Quero ganhar x por mês
if opt == 1:
    args = {'operation': '1', 'arg1': input('insira o valor que você quer ganhar:'), 'arg2': input('insira por quantos anos você quer investir:')}
    result_case1 = client.service.performOperation(args)
    print(result_case1.result)

# Case 2: Quero investir
elif opt == 2:
    args = {'operation': '2', 'arg1': input('insira o valor que você pode investir por mês:'), 'arg2': input('insira por quantos anos você quer investir:')}
    result_case2 = client.service.performOperation(args)
    print(result_case2.result)

# Case 3: Quanto gastar com moradia
elif opt == 3:
    args = {'operation': '3', 'arg1': input('informe o quanto você ganha por mês:')}
    result_case3 = client.service.performOperation(args)
    print(result_case3.result)

# Case 4: Plano de investimento
elif opt == 4:
    args = {'operation': '4', 'arg1': input('informe seu salário:'), 'arg2': input('informe o valor do seu aluguel:'), 'arg3': input('informe o valor de bônus da empresa, caso receba:')}
    result_case4 = client.service.performOperation(args)
    print(result_case4.result)