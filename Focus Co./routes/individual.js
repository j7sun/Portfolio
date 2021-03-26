const data = require('../todo.json');

exports.view = function(req, res){
    res.render('individual', data);
};