using System;

class Program {
    static void Main(string[] args) {
        string palavra = "PALAVRA";
        string resposta = new string('_', palavra.Length);
        int contadorErros = 0;

        while (true) {
            Console.Write("Digite uma letra: ");
            char letra = char.Parse(Console.ReadLine().ToUpper());

            bool letraEncontrada = false;

            for (int i = 0; i < palavra.Length; i++) {
                if (letra == palavra[i]) {
                    resposta = resposta.Remove(i, 1).Insert(i, letra.ToString());
                    letraEncontrada = true;
                }
            }

            Console.WriteLine();
            Console.WriteLine(resposta);
            Console.WriteLine();

            if (!resposta.Contains("_")) {
                Console.WriteLine("Parabéns, você acertou a palavra!");
                break;
            }

            if (!letraEncontrada) {
                Console.WriteLine();
                Console.WriteLine("Letra errada, tente novamente.");
                Console.WriteLine($"Você errou {++contadorErros} de 3 possíveis.");
                Console.WriteLine();
            }

            if (contadorErros == 3) {
                break;
            }
        }
    }
}
