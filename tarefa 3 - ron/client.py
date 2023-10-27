import Pyro4



def main():
    uri = "PYRO:wordguessgame@localhost:59273"
    game = Pyro4.Proxy(uri)
    print("Conectado ao servidor RMI do Jogo da Forca.")

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
