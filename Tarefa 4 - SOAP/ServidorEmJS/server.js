const soap = require("soap");
const http = require("http");

const servico = {
    QAjuda_servico: {
        porta: {
            QueroGanharX: function (args, callback) {
                try {
                    const valor = args.valor;
                    const anos = args.anos;

                    const taxaMes = 0.009;
                    const montanteEstimando = valor / taxaMes;
                    const taxaAnual = Math.pow(1 + taxaMes, 12) - 1;
                    const taxaReal = taxaAnual / 12;

                    const investimentoMensal =
                        (montanteEstimando / ((Math.pow(1 + taxaReal, anos * 12) - 1) / taxaReal)) *
                        Math.pow(1 + taxaReal, 1);

                    callback(null, { investimentoMensal });
                } catch (error) {
                    console.error(error);
                    callback({ Fault: { Code: { Value: 'soap:Receiver' }, Reason: { Text: 'Internal Server Error' } } });
                }

            },
            QueroInvestir: function (args, callback) {
                const valor = args.valor;
                const anos = args.anos;

                const taxaMes = 0.009;
                const taxaAnual = Math.pow(1 + taxaMes, 12) - 1;
                const taxaReal = taxaAnual / 12;

                const montanteFinal =
                    valor *
                    ((Math.pow(1 + taxaReal, anos * 12) - 1) / taxaReal) *
                    Math.pow(1 + taxaReal, 1);

                callback(null, { montanteFinal });
            },
            ValorMoradia: function (args, callback) {
                const sal = args.sal;
                const mensagem = `Seu valor com aluguel ou parcela de financiamento deverá ser no máximo ${(sal / 3).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}.`;
                callback(null, { mensagem });
            },
            PlanoDeInvestimento: function (args, callback) {
                const sal = args.sal;
                const valorAluguel = args.valorAluguel;
                const valorBonus = args.valorBonus;
            
                let valorParaInvestir = (sal - valorAluguel) * 0.1 * 12;
                valorParaInvestir += valorBonus * 0.5;
                valorParaInvestir += sal * 0.7;
            
                const valorParaFerias = (sal / 3) + sal * 0.3;
            
                const plano = {
                    valorParaFerias: valorParaFerias.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }),
                    valorInvestidoAno: valorParaInvestir.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }),
                    rendimentoMensal: (valorParaInvestir * 0.009).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
                };
            
                callback(null, { plano });
            }
        }
    }
};

const xml = `
<definitions
    name="QAjuda_servico"
    targetNamespace="http://example.com/QAjuda_servico"
    xmlns="http://schemas.xmlsoap.org/wsdl/"
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:tns="http://example.com/QAjuda_servico"
>
    <types>
        <!-- Defina seus tipos de dados aqui -->
    </types>

    <message name="QueroGanharXInput">
        <part name="valor" type="xsd:double" />
        <part name="anos" type="xsd:int" />
    </message>

    <message name="QueroGanharXOutput">
        <part name="investimentoMensal" type="xsd:double" />
    </message>

    <!-- Adicione outras mensagens e operações aqui -->

    <portType name="QAjudaPortType">
        <operation name="QueroGanharX">
            <input message="tns:QueroGanharXInput" />
            <output message="tns:QueroGanharXOutput" />
        </operation>
        <!-- Adicione outras operações aqui -->
    </portType>

    <binding name="QAjudaBinding" type="tns:QAjudaPortType">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http" />
        <operation name="QueroGanharX">
            <soap:operation soapAction="http://example.com/QueroGanharX" />
            <input>
                <soap:body use="literal" />
            </input>
            <output>
                <soap:body use="literal" />
            </output>
        </operation>
        <!-- Adicione outras operações aqui -->
    </binding>

    <service name="QAjudaService">
        <port name="QAjudaPort" binding="tns:QAjudaBinding">
            <soap:address location="http://localhost:8000/QAjuda" />
        </port>
    </service>
</definitions>

`;

const servidor = http.createServer(function (req, res) {
    res.end("404: Not found " + req.url);
});

servidor.listen(8000);

// Crie o servidor SOAP sem usar um arquivo WSDL
const server = soap.listen(servidor, '/QAjuda', servico, xml);

console.log('Servidor SOAP rodando em http://localhost:8000/QAjuda');
