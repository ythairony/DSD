public class CalcInvestimentos {
    // [ 1 ] - Quero ganhar X por mês
    // 	* Informa quanto quer ganhar
    // 	* Informa em quanto tempo
    // 	retorna valor que deve ser investido por mês 

    // TUDO DA DANDO CONTA TRONXA 

    public static double QueroGanharX(double valor, int anos) {
        // taxa mes de 0,9%
        double taxaMes = 0.009;

        double montanteEstimando = valor / taxaMes;

        // taxa de juros anual (1 + tx mes elevado a 12 - 1)
        double taxaAnual = ((double)Math.Pow((1 + taxaMes), 12) - 1);

        // taxa real é a taxa anual divido por 12, pois a taxa real sempre será maior que a taxa mensal
        double taxaReal = taxaAnual / 12;

        // Formulinha contrária da QueroInvestir https://www.youtube.com/watch?v=9zY0xeZ0q1g 
        double investimentoMensal = montanteEstimando / (((double)Math.Pow((1 + taxaReal), (anos * 12)) - 1) / taxaReal) * Math.Pow((1 + taxaReal), 1);

        // Valor total investido pelo pessoa
        double totalInvestido = investimentoMensal * (anos * 12);
        // montanteEstimado é o valor acumulado no final

        return investimentoMensal;
    }



    // Quero investir
	// * Informa quanto tem disponível para investir por mês
	// * Informa quando tempo vai investir
	// retorna renda que terá mensalmente ao término do prazo, o valor total investido e o valor que foi acumulado
    public static double QueroInvestir(double valor, int anos) {
        // taxa mes de 0,9%
        double taxaMes = 0.009;
        double taxaAnual = ((double)Math.Pow((1 + taxaMes), 12) - 1);
        double taxaReal = taxaAnual / 12;

        // Formulinha https://www.youtube.com/watch?v=9zY0xeZ0q1g
        double montanteFinal = valor * (((double)Math.Pow((1 + taxaReal), (anos * 12)) - 1) / taxaReal) * Math.Pow((1 + taxaReal), 1);

        // retornar valor total investido
        double totalInvestido = valor * (anos * 12);
        // retornar o valor que renderá no final do período 
        double rendaPassiva = montanteFinal * taxaMes;


        // retorna o montante acumulado no final
        return montanteFinal;
    }
}