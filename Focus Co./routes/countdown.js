const data = require('../task.json');


exports.view = function(req, res){
    res.render('countdown');
};

exports.post = function (req, res) {
    data['task']['ticket_val'] = req.body.ticket_val;
    data['task']['ticket_num'] = req.body.ticket_num;
    res.render('countdown',data);
}