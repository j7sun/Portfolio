var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();
app.use(cookieParser());

const data = require('../data.json');

exports.view = function(req, res){
    res.render('main', data);
};

