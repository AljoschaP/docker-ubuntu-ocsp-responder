var fs = require('fs');
var express = require('express');
var cors = require('cors');
var https = require('https');
var http = require('http');
var bodyParser = require('body-parser');
var key = fs.readFileSync('/opt/pki/va/va.key.pem');
var cert = fs.readFileSync('/opt/pki/va/va.cert.pem');
var caCert = fs.readFileSync('/opt/pki/ca/ca-chain.cert.pem');

var https_options = {
    key: key,
    cert: cert,
	ca: caCert
};
var PORT = 80;
var HOST = '0.0.0.0';
var app = express();
app.use(cors());
app.use(bodyParser.json()); // for parsing application/json

//server = https.createServer(https_options, app).listen(PORT, HOST);
server = http.createServer(app).listen(PORT,HOST);
console.log('HTTPS Server listening on %s:%s', HOST, PORT);


// routes
app.get('/', function(req, res) {
    res.send('Get is not supported');
});
app.post('/postIndex', function(req, res) {
    	console.log(req);
	fs.writeFile('/opt/pki/ca/index.txt',req.body.data, function (err) {
  if (err) return console.log(err);
  console.log(req.body.data+' > index.txt');
});
	res.send('Index received');
});
