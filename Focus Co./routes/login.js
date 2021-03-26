var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();
app.use(cookieParser());


exports.view = function (req, res) {
    var status = {
        'loggedIn': req.cookies['loggedIn']
    };
    console.log(status.loggedIn);
    res.render('login', status);
};
