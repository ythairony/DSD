const soap = require('soap');
const http = require('http');



// Define the service implementation
const service = {
  WeatherService: {
    WeatherPort: {
      GetWeather: function(args, callback) {
        // Perform the logic to get the weather based on the location
        const location = args.location;
        const temperature = '25°C';
        const description = 'Sunny';

        // Return the response
        const result = {
          temperature: temperature,
          description: description
        };
        callback(null, result);
      }
    }
  }
};

// Create the SOAP server
// const xml = require('fs').readFileSync('./weatherService.wsdl', 'utf8');
// const server = soap.listen({ path: '/weather', xml: xml }, function() {
//   console.log('SOAP server running at http://localhost:8000/weather?wsdl');
// });

const xml = require('fs').readFileSync('./weatherService.wsdl', 'utf8');

var server = http.createServer(function(request,response) {
  response.end('404: Not Found: ' + request.url);
});

server.listen(8000);
soap.listen(server, '/weather?wsdl', service, xml, function(){
console.log('server initialized');
});

// Attach the service implementation to the SOAP server
//server.addService(xml, service, { suppressStack: true });