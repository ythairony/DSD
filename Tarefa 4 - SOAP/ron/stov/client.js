var soap = require('soap');
var url = 'http://localhost/wsdl?wsdl';
var args = {name: 'value'};
soap.createClient(url, function(err, client) {
  client.MyFunction(args, function(err, result) {
      console.log(result);
  });
});