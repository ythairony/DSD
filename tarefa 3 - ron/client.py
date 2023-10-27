import Pyro4



def main():
    try:
        game = Pyro4.Proxy("PYRONAME:wordguessgame")
        print("Conectado ao servidor RMI do Jogo da Forca.")
    except:
        print("erro :()")

    while True:
        guess = input("Faça um palpite (letra ou palavra completa): ")
        result = game.guess_word(guess)
        print(result)

        if "Parabéns! Você adivinhou a palavra!" in result or "Você perdeu!" in result:
            play_again = input("Deseja jogar novamente? (S/N)").lower()
            if play_again != "s":
                break

if __name__ == "__main__":
    main()
