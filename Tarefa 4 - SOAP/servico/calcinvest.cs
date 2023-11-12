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


    // [ 3 ] - Quando devo gastar com moradia
	// * Informa o valor do salário
	// retorna o valor sugerido de preço que deve pagar de aluguel/financiamento

    public static string ValorMoradia(double sal) {
        return $"Seu valor com aluguel ou parcela de financiamento deverá ser no máximo {(sal/3).ToString("C")}.";
    }


    // [ 4 ] - Monte seu plano de investimento
	// * Informe o salário
	// * Informe valor do aluguel/parcela de onde mora
	// * Informe valor caso receba bonus da empresa (comissões, PLR) de forma anual

	// retorna valor à investir = [
	// 	{ do seu salário: 10% do salário - custo com moradia },
	// 	{ do seu bonus: 50% do bônus },
	// 	{ do seu 13º: 70% do 13º }]
	// retorna o valor a usar com férias = 1/3 do salário (1/3 de férias) + 30% do 13º
	// retorna o valor que seus investimentos vão render para o ano seguinte por mês

    public static string PlanoDeInvestimento(double sal, double valorAluguel, double valorBonus) {
        double valorParaInvestir = ((sal - valorAluguel) * 0.1) * 12;
        // Somar com 50% dos bonus anuais
        valorParaInvestir = valorParaInvestir + (valorBonus * 0.5);
        // Somar com 70% do 13º
        valorParaInvestir = valorParaInvestir + (sal * 0.7);

        double valorParaFerias = (sal / 3) + (sal * 0.3);

        return $"O valor a ser gasto com suas férias é de {valorParaFerias.ToString("C")}\nValor investido durante o ano será {valorParaInvestir.ToString("C")}\nSeu valor investido renderá {(valorParaInvestir*0.009).ToString("C")} todos os meses no ano seguinte.";
    }
}