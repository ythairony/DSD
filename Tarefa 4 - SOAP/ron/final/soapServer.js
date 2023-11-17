const soap = require('soap');
const express = require('express');
const app = express();

const calculatorService = {
  CalculatorService: {
    CalculatorPort: {
      performOperation: function (args) {
        let result;

        switch (args.operation) {
          case '1': // quero ganhar x por mes (quanto, em quanto tempo)
            valor = parseFloat(args.arg1);
            anos = parseint(args.arg2);

            // taxa mes de 0,9%
            taxaMes = parseFloat(0.009);
            montanteEstimando = parseFloat(valor/taxaMes);
            // taxa de juros anual (1 + tx mes elevado a 12 - 1)
            taxaAnual = ((1+taxaMes)*12) -1;
            taxaReal = parseFloat(taxaAnual/12);
            // Formulinha contrária da QueroInvestir https://www.youtube.com/watch?v=9zY0xeZ0q1g 
            investimentoMensal = (montanteEstimando / (((1+taxaReal)**(anos*12))-1) / taxaReal) * ((1+taxaReal)**1);

            totalInvestido = investimentoMensal*(anos*12);

            result = `pra ganhar ${valor} por mês você vai precisar investir ${investimentoMental}`;

            break;


          case '2': // quero investir (quanto tem disponivel ao mes, quanto tempo)
            valor = parseFloat(args.arg1);
            anos = parseint(args.arg2);
            taxaMes = parseFloat(0.009);
            taxaAnual = ((1+taxaMes)*12) -1;
            taxaReal = parseFloat(taxaAnual/12);

            montanteFinal = (valor * (((1+taxaReal)**(anos*12))-1) / taxaReal) * ((1+taxaReal)**1);

            totalInvestido = valor* (anos*12);

            rendaPassiva = montanteFinal * taxaMes;

            result = `o seu montante final será ${montanteFinal}`

            break;


          case '3': // quanto gastar com moradia
            salario = parseFloat(args.arg1);
            result = `o valor que você pode gastar com moradia é no máximo ${sal/3}`;
            break;


          case '4': // plano de investimento
            salario = parseFloat(args.arg1);
            valorAluguel = parseint(args.arg2);
            valorBonus = parseint(args.arg3);

            valorParaInvestir = parseFloat((salario-valorAluguel)*0.1)*12;
            // Somar com 50% dos bonus anuais
            valorParaInvestir = valorParaInvestir + (valorBonus * 0.5);
            // Somar com 70% do 13º
            valorParaInvestir = valorParaInvestir + (sal * 0.7);

            valorParaFerias = (sal / 3) + (sal * 0.3);

            result = `O valor a ser gasto com suas férias é de ${valorParaFerias}\nValor investido durante o ano será ${valorParaInvestir}\nSeu valor investido renderá ${(valorParaInvestir*0.009)} todos os meses no ano seguinte.`;
        }

        return { result: result };
      },
    },
  },
};

const server = app.listen(8000, function () {
  const wsdlPath = '/calculator?wsdl';
  const xml = require('fs').readFileSync('./calculatorService.wsdl', 'utf8');
  soap.listen(server, wsdlPath, calculatorService, xml);
  console.log('SOAP server running at http://localhost:8000/calculator?wsdl');
});