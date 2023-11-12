using System;


public class Program 
{ 
    public static void Main() {

        Console.WriteLine(CalcInvestimentos.QueroInvestir(1397, 5));
        Console.WriteLine(CalcInvestimentos.QueroGanharX(1000, 5));

        Console.WriteLine(CalcInvestimentos.ValorMoradia(20000));
        Console.WriteLine(CalcInvestimentos.PlanoDeInvestimento(1200, 200, 10000));

    }
}