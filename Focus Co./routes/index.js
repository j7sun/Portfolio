
/*
 * GET home page.
 */

exports.view = function(req, res){
  res.cookie('loggedIn', true);
  res.render('index');
};