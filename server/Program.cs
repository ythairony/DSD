using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int tcpPort = 12345; // Porta para conexão TCP
        int udpPort = 54321; // Porta para conexão UDP

        TcpListener tcpListener = new TcpListener(IPAddress.Any, tcpPort);
        UdpClient udpListener = new UdpClient(udpPort);

        Console.WriteLine("Servidor do Jogo da Forca iniciado...");

        // Aceita a conexão TCP para confirmar o nome do usuário
        tcpListener.Start();
        TcpClient tcpClient = tcpListener.AcceptTcpClient();
        NetworkStream tcpStream = tcpClient.GetStream();
        byte[] tcpBuffer = new byte[1024];
        int bytesRead = tcpStream.Read(tcpBuffer, 0, tcpBuffer.Length);
        string username = Encoding.ASCII.GetString(tcpBuffer, 0, bytesRead);
        Console.WriteLine($"Usuário {username} conectou via TCP.");

        // Inicializa o jogo e a palavra a ser adivinhada
        string wordToGuess = "banana";
        string guessedWord = new string('_', wordToGuess.Length);
        int attemptsLeft = 6;

        // Loop principal do jogo
        while (attemptsLeft > 0)
        {
            Console.WriteLine($"Palavra: {guessedWord}, Tentativas Restantes: {attemptsLeft}");
            Console.Write("Faça um palpite (letra ou palavra completa): ");
            string guess = Console.ReadLine().ToLower();

            if (guess == wordToGuess)
            {
                guessedWord = wordToGuess;
                Console.WriteLine("Parabéns! Você adivinhou a palavra!");
                break;
            }
            else if (guess.Length == 1 && wordToGuess.Contains(guess))
            {
                // Atualiza a palavra adivinhada com a letra correta
                StringBuilder newGuessedWord = new StringBuilder(guessedWord);
                for (int i = 0; i < wordToGuess.Length; i++)
                {
                    if (wordToGuess[i] == guess[0])
                    {
                        newGuessedWord[i] = guess[0];
                    }
                }
                guessedWord = newGuessedWord.ToString();
            }
            else
            {
                Console.WriteLine("Palpite incorreto. Tente novamente.");
                attemptsLeft--;
            }
        }

        // Informa o resultado ao usuário
        Console.WriteLine(attemptsLeft == 0 ? "Você perdeu! A palavra era: " + wordToGuess : "Você ganhou!");
        tcpClient.Close();
        udpListener.Close();

        Console.WriteLine("Pressione qualquer tecla para sair...");
        Console.ReadKey();
    }
}
