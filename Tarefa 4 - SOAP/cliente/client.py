from zeep import Client

class Livro:
    pass

def novoLivro():
    ret = Livro()
    ret.nome = input('Digite o nome do livro: ')
    return ret

def main():
    client = Client('http://127.0.0.1:5000/biblioteca?wsdl')
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
            livro = novoLivro()
            client.service.adicionarLivro(
                livro.nome
            )
        elif op == '2':
            ls = client.service.listarLivros()
            for livro in ls:
                print('')
                print('Nome do livro: ', livro.nome)
        elif op == '3':           
            la = input(f'Nome do livro antigo: ${livro.nome}')
            ln = input(f'\nNome do livro novo: ${livro.nome}')
            ls = client.service.atualizarLivro(la,ln)
        elif op == '4':
            pass
        elif op == '0':
            break
        else:
            print('[ --Opcao inválida!-- ]')

if __name__ == '__main__':
    main()