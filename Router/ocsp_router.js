var hoxy = require('hoxy');

var proxy = new hoxy.Proxy().listen(8888);

proxy.intercept('request', function(req, resp){
  console.log('request made to: ' + req.fullUrl());
});
