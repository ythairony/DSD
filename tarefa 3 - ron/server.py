import Pyro4, random

@Pyro4.expose
class JogoDaForca:
    def __init__(self):
        self.palavras_possiveis = ['alessandro', 'demostenes', 'jorgiano', 'gracon', 'silvia']
        self.palavra = self.palavras_possiveis[random.randrange(0, len(self.palavras_possiveis))]
        self.palavra_montada = ['_'] * len(self.palavra)
        self.tentativas_restantes = 5

    def sorteia_palavra(self):
        numero = random.randrange(0, len(self.palavras_possiveis))
        self.palavra = self.palavras_possiveis[numero]

    def fim(self, vitoria):
        palavra_antiga = self.palavra
        self.sorteia_palavra()
        self.palavra_montada = ['_'] * len(self.palavra) # reseta as letras adivinhadas
        self.tentativas_restantes = 5 # reseta as tentativas restantes
        
        if vitoria:
            return "Parabéns! Você adivinhou a palavra!"
        else:
            return f"Você perdeu! A palavra era: {palavra_antiga}"

    def adivinhar(self, palpite):
        palpite = palpite.lower()
        
        if palpite == self.palavra:
            return self.fim(True)

        # caso o palpite esteja na palavra e seja menor que 2
        if (palpite in self.palavra) and (len(palpite)<2):
            for i in range(len(self.palavra)):
                # verifica se alguma letra da palavra é o palpite
                if self.palavra[i] == palpite:
                    self.palavra_montada[i] = palpite
            # notifica o acerto da palavra ou da letra
            if (''.join(self.palavra_montada) == self.palavra):
                self.palavra_montada = ['_'] * len(self.palavra) # reseta as letras adivinhadas
                return self.fim(True)
            else: return "Você acertou a letra: " + ''.join(self.palavra_montada)
        # caso o palpite nem esteja na palavra e sem seja a palavra
        else:
            self.tentativas_restantes -= 1
            if self.tentativas_restantes == 0:
                return self.fim(False)
            return f"Palpite incorreto. Tentativas restantes: {self.tentativas_restantes}"



def main():
    # Defina a palavra a ser adivinhada aqui  
    jogo = JogoDaForca()

    # simplificação para os comandos mais comuns
    Pyro4.Daemon.serveSimple(
        {
            jogo: "jogo_da_forca",
        },
        ns = True # nameserver
    )

if __name__ == "__main__":
    main()
