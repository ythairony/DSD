const soap = require('soap');

const url = 'http://localhost:8000/calculator?wsdl';

soap.createClient(url, function (err, client) {
  if (err) {
    console.error('Error creating SOAP client:', err);
    return;
  }

  // Test the performOperation function with different operations
  const operationArgs = { num1: 5, num2: 3, operation: 'add' };
  client.performOperation(operationArgs, function (err, result) {
    if (err) {
      console.error('Error calling performOperation:', err);
    } else {
      console.log('Operation Result:', result.result);
    }
  });

  // Test other operations similarly
});