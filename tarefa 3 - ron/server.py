import Pyro4

@Pyro4.expose
class WordGuessGame:
    def __init__(self, word):
        self.word_to_guess = word.lower()
        self.guessed_word = ['_'] * len(word)
        self.attempts_left = 5

    def victory(self):
        self.guessed_word = ['_'] * len(self.word_to_guess) # reseta as letras adivinhadas
        self.attempts_left = 5 # reseta as tentativas
        return "Parabéns! Você adivinhou a palavra!"

    def guess_word(self, guess):
        guess = guess.lower()
        # caso o palpite seja a palavra, retorna vitória
        if guess == self.word_to_guess:
            return self.victory()

        # caso o palpite esteja na palavra e seja menor que 2
        if (guess in self.word_to_guess) and (len(guess)<2):
            for i in range(len(self.word_to_guess)):
                # verifica se alguma letra da palavra é o palpite
                if self.word_to_guess[i] == guess:
                    self.guessed_word[i] = guess
            # notifica o acerto da palavra ou da letra
            if (''.join(self.guessed_word) == self.word_to_guess):
                self.guessed_word = ['_'] * len(self.word_to_guess) # reseta as letras adivinhadas
                return self.victory()
            else: return "Você acertou a letra: " + ' '+guess + " DEBUG - guessed word = " + ''.join(self.guessed_word)
        #caso o palpite nem esteja na palavra e sem seja a palavra
        else:
            self.attempts_left -= 1
            if self.attempts_left == 0:
                return f"Você perdeu! A palavra era: {self.word_to_guess}"
            return f"Palpite incorreto. Tentativas restantes: {self.attempts_left}"

def main():
    # Defina a palavra a ser adivinhada aqui
    word_to_guess = "python"  
    game = WordGuessGame(word_to_guess)

    # simplificação para os comandos mais comuns
    Pyro4.Daemon.serveSimple(
        {
            game: "wordguessgame",
        },
        ns = True # nameserver
    )

if __name__ == "__main__":
    main()
