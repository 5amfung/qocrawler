/*
 * A simple http server for testing.
 */

var express = require('express');
var app = express();

app.configure(function() {
  app.use(function(req, res, next) {
    console.log('ip: %s', req.ip);
    console.log(req.headers);
    next();
  });

  app.use('/', express.static(__dirname));
});

app.listen(8123);

