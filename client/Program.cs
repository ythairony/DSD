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

        while (true)
        {
            Console.Write("Faça um palpite (letra ou palavra completa): ");
            string guess = Console.ReadLine().ToLower();
            udpBuffer = Encoding.ASCII.GetBytes(guess);

            udpClient.Send(udpBuffer, udpBuffer.Length);

            // Recebe a resposta do servidor
            IPEndPoint serverEndPoint = new IPEndPoint(IPAddress.Any, udpPort);
            udpBuffer = udpClient.Receive(ref serverEndPoint);

            string gameStatus = Encoding.ASCII.GetString(udpBuffer, 0, udpBuffer.Length);
            Console.WriteLine(gameStatus);
        }
    }
}
