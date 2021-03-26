
/**
 * Module dependencies.
 */

var express = require('express');
var http = require('http');
var path = require('path');
var handlebars = require('express3-handlebars');
var cookieParser = require('cookie-parser');


var index = require('./routes/index');
var main = require('./routes/main');
var countdown = require('./routes/countdown');
var taskSetting = require('./routes/taskSetting');
var notiSetting = require('./routes/notiSetting');
var login = require('./routes/login');
var individual = require('./routes/individual');
var ticket = require('./routes/ticket');
var friends = require('./routes/friends');
var middleware = require('./middleware/middleware');
var achievements = require('./routes/achievements');
var history = require('./routes/history');
var todo = require('./routes/todo');
var addtask = require('./routes/addtask');
const { Collection } = require('mongoose');
// Example route
// var user = require('./routes/user');

var app = express();

// all environments
app.set('port', process.env.PORT || 3000);
app.set('views', path.join(__dirname, 'views'));
app.engine('handlebars', handlebars());
app.set('view engine', 'handlebars');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use(express.methodOverride());
app.use(express.cookieParser('IxD secret key'));
app.use(express.session());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));
app.use(cookieParser());

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

app.get('/', index.view);
// Example route
// app.get('/users', user.list);
app.post('/main',middleware.verify, main.view);
app.get('/main', main.view);
app.get('/countdown', countdown.view);
app.post('/countdown', countdown.post);
app.get('/tasksetting', taskSetting.view);
app.get('/notisetting', notiSetting.view);
app.get('/login',login.view);
app.get('/individual', individual.view);
app.post('/addTodo', todo.addTodo);
app.post('/deleteTodo', todo.deleteTodo);
app.get('/tasksetting/ticket',ticket.view);
app.post('/addTask', addtask.addTask);
app.get('/friends', friends.view);
app.get('/achievements', achievements.view);
app.get('/history', history.view);

http.createServer(app).listen(app.get('port'), function(){
  console.log('Express server listening on port ' + app.get('port'));
});
