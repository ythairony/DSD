import Pyro4

@Pyro4.expose
class WordGuessGame:
    def __init__(self, word):
        self.palavra = word.lower()
        self.palavra_montada = ['_'] * len(word)
        self.tentativas_restantes = 5

    def vitoria(self):
        self.palavra_montada = ['_'] * len(self.palavra) # reseta as letras adivinhadas
        self.tentativas_restantes = 5 # reseta as tentativas restantes
        return "Parabéns! Você adivinhou a palavra!"

    def adivinhar(self, palpite):
        palpite = palpite.lower()
        
        if palpite == self.palavra:
            return self.vitoria()

        # caso o palpite esteja na palavra e seja menor que 2
        if (palpite in self.palavra) and (len(palpite)<2):
            for i in range(len(self.palavra)):
                # verifica se alguma letra da palavra é o palpite
                if self.palavra[i] == palpite:
                    self.palavra_montada[i] = palpite
            # notifica o acerto da palavra ou da letra
            if (''.join(self.palavra_montada) == self.palavra):
                self.palavra_montada = ['_'] * len(self.palavra) # reseta as letras adivinhadas
                return self.vitoria()
            else: return "Você acertou a letra: " + ' '+palpite + " DEBUG - guessed word = " + ''.join(self.palavra_montada)
        #caso o palpite nem esteja na palavra e sem seja a palavra
        else:
            self.tentativas_restantes -= 1
            if self.tentativas_restantes == 0:
                return f"Você perdeu! A palavra era: {self.palavra}"
            return f"Palpite incorreto. Tentativas restantes: {self.tentativas_restantes}"

def main():
    # Defina a palavra a ser adivinhada aqui
    palavra = "python"  
    game = WordGuessGame(palavra)

    # simplificação para os comandos mais comuns
    Pyro4.Daemon.serveSimple(
        {
            game: "jogo_da_forca",
        },
        ns = True # nameserver
    )

if __name__ == "__main__":
    main()
