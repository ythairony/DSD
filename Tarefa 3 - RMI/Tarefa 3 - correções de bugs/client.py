import Pyro4

def main():
    try:
        # proxy: interface que intermedia para o objeto real
        forca = Pyro4.Proxy("PYRONAME:jogo_da_forca") 
        print("Conectado ao servidor RMI do Jogo da Forca.")
    except:
        print("erro : algo deu errado XD não conseguimos conectar")

    while True: # laço infinito
        palpite = input("Faça um palpite (letra ou palavra completa): ")
        # o proxy atua como se fosse o próprio objeto
        resultado = forca.adivinhar(palpite)
        print(resultado)

        if "Parabéns! Você adivinhou a palavra!" in resultado or "Você perdeu!" in resultado:
            jogar_novamente = input("Deseja jogar novamente? (S/N)").lower()
            if jogar_novamente != "s":
                break

if __name__ == "__main__":
    main()
