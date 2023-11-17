const soap = require('soap');
const readline = require('readline');
const { stringify } = require('querystring');

const url = 'http://127.0.0.1:8000/?wsdl';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function queroGanharX(client) {
  rl.question('Digite quanto deseja ganhar: ', (valor) => {
    rl.question('Digite o número de anos: ', (anos) => {
      client.QueroGanharX({ valor: parseFloat(valor), anos: parseInt(anos) }, (err, result) => {
        if (err) {
          console.error('Erro:', err);
          return;
        }
        console.log('Resultado QueroGanharX:', result.investimentoMensal);
        menu(client);
      });
    });
  });
}

function queroInvestir(client) {
  rl.question('Digite o valor disponível para investir por mês: ', (valor) => {
    rl.question('Digite o número de anos: ', (anos) => {
      client.QueroInvestir({ valor: parseFloat(valor), anos: parseInt(anos) }, (err, result) => {
        if (err) {
          console.error('Erro:', err);
          return;
        }
        console.log('Resultado QueroInvestir:', result.montanteFinal);
        menu(client);
      });
    });
  });
}

function valorMoradia(client) {
  rl.question('Digite o valor do salário: ', (sal) => {
    client.ValorMoradia({ sal: parseFloat(sal) }, (err, result) => {
      if (err) {
        console.error('Erro:', err);
        return;
      }
      console.log('Resultado ValorMoradia:', result.mensagem);
      menu(client);
    });
  });
}

function planoDeInvestimento(client) {
  rl.question('Digite o valor do salário: ', (sal) => {
    rl.question('Digite o valor do aluguel: ', (valorAluguel) => {
      rl.question('Digite o valor do bônus: ', (valorBonus) => {
        client.PlanoDeInvestimento({ sal: parseFloat(sal), valorAluguel: parseFloat(valorAluguel), valorBonus: parseFloat(valorBonus) }, (err, result) => {
          if (err) {
            console.error('Erro:', err);
            return;
          }
          const plano = result.plano;
          console.log(`Valor para férias: ${plano.valorParaFerias}`);
          console.log(`Valor investido durante o ano: ${plano.valorInvestidoAno}`);
          console.log(`Rendimento mensal: ${plano.rendimentoMensal}`);
          menu(client);
        });
      });
    });
  });
}

function menu(client) {
  console.log('\nMENU:');
  console.log('[ 1 ] Quero Ganhar X por mês');
  console.log('[ 2 ] Quero Investir X por mês');
  console.log('[ 3 ] Quanto devo gastar com moradia');
  console.log('[ 4 ] Plano de investimento');
  console.log('[ 0 ] Sair');
  rl.question('> ', (op) => {
    switch (op) {
      case '1':
        queroGanharX(client);
        break;
      case '2':
        queroInvestir(client);
        break;
      case '3':
        valorMoradia(client);
        break;
      case '4':
        planoDeInvestimento(client);
        break;
      case '0':
        rl.close();
        break;
      default:
        console.log('[ --Opcao inválida!-- ]');
        menu(client);
        break;
    }
  });
}

soap.createClient(url, (err, client) => {
  if (err) {
    console.error(err);
    return;
  }

  console.log('### QAjuda Investimentos');
  menu(client);
});
