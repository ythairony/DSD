const soap = require("soap")
const http = require("http")

const WSDL_PATH = "/QAjudaFinancas.wsdl"
const WSDL_DEFINITION = require("fs").readFileSync(WSDL_PATH, "utf8")

const servico = {
    QAjuda_servico: {
        porta: {
             
        }
    }
}

const servidor = http.createServer(function(req, res) {
    res.end("404: Not found " + req.url)
})

servidor.listen(8000)
SOAP.listen(servidor, "/QAjuda", servico, WSDL_DEFINITION) // temporário...

console.log("QAjuda Finanças rodando...")