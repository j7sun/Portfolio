const data = require('../task.json');

exports.addTask = (req, res) => {
    const task = req.body;
    data['task']['hour'] = task.hour;
    data['task']['min'] = task.min;
    data['task']['tasks'] = task.list;
}