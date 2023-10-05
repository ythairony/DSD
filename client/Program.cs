using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        int udpPort = 54321; // Porta para conexão UDP

        UdpClient udpClient = new UdpClient();
        udpClient.Connect(IPAddress.Loopback, udpPort);

        Console.Write("Informe seu nome de usuário: ");
        string username = Console.ReadLine();

        // Envia o nome de usuário via TCP
        using (TcpClient tcpClient = new TcpClient())
        {
            tcpClient.Connect(IPAddress.Loopback, 12345);
            NetworkStream tcpStream = tcpClient.GetStream();
            byte[] usernameBytes = Encoding.ASCII.GetBytes(username);
            tcpStream.Write(usernameBytes, 0, usernameBytes.Length);
        }

        byte[] udpBuffer;
        IPEndPoint udpEndPoint = new IPEndPoint(IPAddress.Loopback, udpPort);

        bool jogoContinua = true;

        while (jogoContinua)
        {
            Console.Write("Faça um palpite (letra ou palavra completa): ");
            string guess = Console.ReadLine().ToLower();
            udpBuffer = Encoding.ASCII.GetBytes(guess);

            udpClient.Send(udpBuffer, udpBuffer.Length);

            // Recebe o resultado do servidor via UDP
            udpBuffer = udpClient.Receive(ref udpEndPoint);
            string gameStatus = Encoding.ASCII.GetString(udpBuffer, 0, udpBuffer.Length);
            Console.WriteLine(gameStatus);

            if (gameStatus.Contains("Parabéns! Você adivinhou a palavra!") || gameStatus.Contains("Você perdeu!"))
            {
                Console.WriteLine("Deseja jogar novamente? (S/N)");
                string resposta = Console.ReadLine().ToLower();
                if (resposta != "s")
                {
                    jogoContinua = false;
                }
                else
                {
                    // Reinicia o jogo ou qualquer outra ação que você deseje fazer
                    // (por exemplo, gerar uma nova palavra para adivinhar)
                }
            }
        }

        Console.WriteLine("Pressione qualquer tecla para sair...");
        Console.ReadKey();
    }
}


















