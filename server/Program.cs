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
        int attemptsLeft = 5;

        // Loop principal do jogo
        while (attemptsLeft > 0)
        {
          Console.WriteLine($"Palavra: {guessedWord}, Tentativas Restantes: {attemptsLeft}");
          Console.Write("Faça um palpite (letra ou palavra completa): ");

          // Recebe o palpite do cliente via UDP
          IPEndPoint udpEndPoint = new IPEndPoint(IPAddress.Any, udpPort);
          byte[] udpBuffer = udpListener.Receive(ref udpEndPoint);
          string guess = Encoding.ASCII.GetString(udpBuffer, 0, udpBuffer.Length);

          if (guess == wordToGuess)
          {
              guessedWord = wordToGuess;
              Console.WriteLine("Parabéns! Você adivinhou a palavra!");
              // Agora você pode reiniciar o jogo ou tomar outra ação, se desejar
              attemptsLeft = 0; // Encerra o loop
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
              udpBuffer = Encoding.ASCII.GetBytes("Acertou a letra");
              udpListener.Send(udpBuffer, udpBuffer.Length, udpEndPoint);

          }
          else
          {
              attemptsLeft--;
              Console.WriteLine("Palpite incorreto. Tente novamente.");
              udpBuffer = Encoding.ASCII.GetBytes($"Palpite incorreto. Voce tem {attemptsLeft} tentativas.");
              udpListener.Send(udpBuffer, udpBuffer.Length, udpEndPoint);
              if (attemptsLeft==0) {
                udpBuffer = Encoding.ASCII.GetBytes($"Voce perdeu, a palavra era => {wordToGuess}");
                udpListener.Send(udpBuffer, udpBuffer.Length, udpEndPoint);
              }
          }

          // Envia o resultado do jogo de volta para o cliente
          // string gameStatus = attemptsLeft == 0 ? "Você perdeu! A palavra era: " + wordToGuess : "Você ganhou!";
          // udpBuffer = Encoding.ASCII.GetBytes(gameStatus);
          // udpListener.Send(udpBuffer, udpBuffer.Length, udpEndPoint);
        }

        // Informa o resultado ao usuário
        Console.WriteLine(attemptsLeft == 0 ? "Você perdeu! A palavra era: " + wordToGuess : "Você ganhou!");
        tcpClient.Close();
        udpListener.Close();

        Console.WriteLine("Pressione qualquer tecla para sair...");
        Console.ReadKey();
    }
}