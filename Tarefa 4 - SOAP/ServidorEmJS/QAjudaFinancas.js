// Lógica em JavaScript
const calcInvestimentos = {
    QueroGanharX: function (valor, anos) {
        const taxaMes = 0.009;
        const montanteEstimando = valor / taxaMes;
        const taxaAnual = Math.pow(1 + taxaMes, 12) - 1;
        const taxaReal = taxaAnual / 12;

        const investimentoMensal =
            (montanteEstimando / ((Math.pow(1 + taxaReal, anos * 12) - 1) / taxaReal)) *
            Math.pow(1 + taxaReal, 1);

        return investimentoMensal;
    },

    QueroInvestir: function (valor, anos) {
        const taxaMes = 0.009;
        const taxaAnual = Math.pow(1 + taxaMes, 12) - 1;
        const taxaReal = taxaAnual / 12;

        const montanteFinal =
            valor *
            ((Math.pow(1 + taxaReal, anos * 12) - 1) / taxaReal) *
            Math.pow(1 + taxaReal, 1);

        return montanteFinal;
    },

    ValorMoradia: function (sal) {
        return `Seu valor com aluguel ou parcela de financiamento deverá ser no máximo ${(sal / 3).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}.`;
    },

    PlanoDeInvestimento: function (sal, valorAluguel, valorBonus) {
        let valorParaInvestir = (sal - valorAluguel) * 0.1 * 12;
        valorParaInvestir += valorBonus * 0.5;
        valorParaInvestir += sal * 0.7;

        const valorParaFerias = (sal / 3) + sal * 0.3;

        return `O valor a ser gasto com suas férias é de ${valorParaFerias.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}\nValor investido durante o ano será ${valorParaInvestir.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}\nSeu valor investido renderá ${(valorParaInvestir * 0.009).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })} todos os meses no ano seguinte.`;
    }
};

// Exemplo de chamada dos métodos
const resultadoQueroGanharX = calcInvestimentos.QueroGanharX(1000, 5);
const resultadoQueroInvestir = calcInvestimentos.QueroInvestir(500, 10);
const resultadoValorMoradia = calcInvestimentos.ValorMoradia(3000);
const resultadoPlanoInvestimento = calcInvestimentos.PlanoDeInvestimento(5000, 1000, 2000);

console.log("Quero Ganhar X:", resultadoQueroGanharX);
console.log("Quero Investir:", resultadoQueroInvestir);
console.log("Valor Moradia:", resultadoValorMoradia);
console.log("Plano de Investimento:", resultadoPlanoInvestimento);
