var express = require('express');
var request = require("request");
var circJSON = require("circular-json");
var bodyParser = require('body-parser');
var multer = require('multer'); 
var app = express();
app.use(bodyParser.raw({type:'application/ocsp-request'}));



app.get('/', function (req, res) {
  res.send('GET Request is not supported for this OCSP');
});

app.post('/', function(req, res) {
    var tempreq = request({ url: 'http://'+req.hostname+':8888', method: 'POST', headers: {'Content-Type':'application/ocsp-request','Content-Length':req.get("Content-Length")} , body: req.body }, function(err, remoteResponse, remoteBody) {
        if (err) { console.log(err);
return res.status(415).end('Error'); }
        //console.log("Remote-Body: "+remoteBody);
	//console.log("Remote-Header: "+remoteResponse);
	res.writeHead(remoteResponse); // copy all headers from remoteResponse
        res.end(remoteBody);
    });
console.log(tempreq);
});

var server = app.listen(3000, function () {

  var host = server.address().address;
  var port = server.address().port;

  console.log('Example app listening at http://%s:%s', host, port);

});
