var algorithm = require('..;, /' + process.argv[2]);
var debug_mode = process.argv.length > 3 ? (process.argv[3] === '-dbg') : false;

function prepare_testcases() {