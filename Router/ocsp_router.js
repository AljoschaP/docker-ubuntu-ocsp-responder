var http = require('http'),
    httpProxy = require('http-proxy');
var chokidar = require('chokidar');
var sys = require('sys');
var exec = require('child_process').exec;
var fs = require('fs');
var npid = require('npid');

try {
    var pid = npid.create('/var/run/ocsp-router.pid');
    pid.removeOnExit();
} catch (err) {
    console.log(err);
    process.exit(1);
}




//
// Create a proxy server with custom application logic
//
var proxy = httpProxy.createProxyServer({});

//
// Create your custom server and just call `proxy.web()` to proxy
// a web request to the target passed in the options
// also you can use `proxy.ws()` to proxy a websockets request
//
var server = http.createServer(function(req, res) {
  // You can define here your custom logic to handle the request
  // and then proxy the request.
        console.log(req.method);
if(req.method == "POST"){
proxy.web(req, res, { target: 'http://127.0.0.1:8888' });
}else{
proxy.web(req, res, { target: 'http://127.0.0.1:8080' });
}
});

console.log("listening on port 3000")
server.listen(3000);

http.createServer(function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.write('request successfully proxied to: ' + req.url + '\n' + JSON.stringify(req.headers, true, 2));
  res.end();
}).listen(8080);

chokidar.watch('/opt/pki/ca/index.txt', {ignored: /[\/\\]\./}).on('change', function(event, path) {
  fs.appendFile('/var/log/ocsp-router/ocsp-router.log',event+":"+path.ctime+"\n", function (err) {
});
console.log(event,path);
exec("/etc/init.d/ocsp stop");

});


exec("/etc/init.d/ocsp stop");

});



