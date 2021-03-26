var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();
app.use(cookieParser());
const data = require("../data.json");

exports.verify = function (req, res, next) {

    if (req.body.username == null || req.body.password == null || !data[req.body.username] ) {
        res.cookie('loggedIn', false);
        res.render('login');
    } else {
        const username = req.body.username;
        const password = req.body.password;
        var pass = data[username].password;

        if (password === pass) {
            console.log("You have successfully logged in.");
            res.cookie('loggedIn', true);
            return next();
        } else {
            res.cookie('loggedIn', false);
            res.render('login');
        }
    }


}
