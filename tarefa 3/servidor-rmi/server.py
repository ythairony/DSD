import Pyro4

@Pyro4.expose
class WordGuessGame:
    def __init__(self, word):
        self.word_to_guess = word.lower()
        self.guessed_word = ['_'] * len(word)
        self.attempts_left = 5

    def guess_word(self, guess):
        guess = guess.lower()  # Converta o palpite para minúsculas 

        if guess == self.word_to_guess:
            return "Parabéns! Você adivinhou a palavra!"
        elif guess in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    self.guessed_word[i] = guess
            return "Você acertou a letra: " + ' '.join(self.guessed_word)
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                return f"Você perdeu! A palavra era: {self.word_to_guess}"
            return f"Palpite incorreto. Tentativas restantes: {self.attempts_left}"

def main():
    # Defina a palavra a ser adivinhada aqui
    word_to_guess = "python"  
    game = WordGuessGame(word_to_guess)
    Pyro4.Daemon.serveSimple(
        {
            game: "wordguessgame"
        },
        ns=False
    )

if __name__ == "__main__":
    main()
