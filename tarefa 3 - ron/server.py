import Pyro4

@Pyro4.expose
class WordGuessGame:
    def __init__(self, word):
        self.word_to_guess = word.lower()
        self.guessed_word = ['_'] * len(word)
        self.attempts_left = 5

    def guess_word(self, guess):
        guess = guess.lower()  # Converta o palpite para minúsculas 

        #if guess == self.word_to_guess:
        #    return "Parabéns! Você adivinhou a palavra!"
        
        if guess in self.word_to_guess:
            for i in range(len(self.word_to_guess)):
                if self.word_to_guess[i] == guess:
                    self.guessed_word[i] = guess
            if ''.join(self.guessed_word) == self.word_to_guess:
                self.guessed_word = ['_'] * len(word)
                return "Parabéns! Você adivinhou a palavra!"
            else: return "Você acertou a letra: " + ' '+guess + " DEBUG - guessed word = " + ''.join(self.guessed_word)
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                return f"Você perdeu! A palavra era: {self.word_to_guess}"
            return f"Palpite incorreto. Tentativas restantes: {self.attempts_left}"

def main():
    # Defina a palavra a ser adivinhada aqui
    word_to_guess = "python"  
    game = WordGuessGame(word_to_guess)
    #name_server = Pyro4.locateNS()
    #uri = daemon.register(GreetingMaker)
    #name_server.register("iury taynori", uri)
    Pyro4.Daemon.serveSimple(
        {
            game: "wordguessgame",
        },
        ns = True
    )

if __name__ == "__main__":
    main()
