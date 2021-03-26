const data = require('../todo.json');

exports.addTodo = (req,res) => {
    const newTodo = req.body.todo;
    console.log(data.todo);
    data['todo'].push(newTodo);
}

exports.deleteTodo = (req, res) => {
    const toRemove = req.body.todo;
    console.log(toRemove);
    data['todo'] = data['todo'].filter(item => item !== toRemove);
}
