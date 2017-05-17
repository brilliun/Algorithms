var algorithm = require('./' + process.argv[2]);
var debug_mode = process.argv.length > 3 ? (process.argv[3] === '-dbg') : false;

function prepare_testcases() {
  var testcases = [];

  testcases.push([]);
  testcases.push([1]);
  testcases.push([1, 2]);
  testcases.push([2, 1]);
  testcases.push([1, 1]);
  testcases.push([1, 2, 3]);
  testcases.push([3, 2, 1]);
  testcases.push([2, 2, 2]);
  testcases.push([1, 3, 1]);
  testcases.push([3, 1, 3]);

  var size = 10;
  for (var i = 0; i < 10; i++) testcases.push(_generateRandomArray(size, size));

  size = 15;
  for (var i = 0; i < 10; i++) testcases.push(_generateRandomArray(size, size));

  size = 16;
  for (var i = 0; i < 10; i++) testcases.push(_generateRandomArray(size, size));

  return testcases;
}

function run_tests(testcases) {
  var options = {
    debug_mode: debug_mode
  };
  var total = testcases.length;
  var prefix;
  var error_count = 0;
  var original;

  console.log('Running ' + total + ' test cases...');
  testcases.forEach(function(testcase, i) {
    original = testcase.slice();
    result = algorithm.run(testcase.slice(), options);
    should_be = testcase.sort(function(a, b) {
      return a - b;
    });

    prefix = '(' + (i+1) + '/' + total + ')';
    if (_arrayEqual(result, should_be)) {
      console.log(prefix + ' Passed');
    } else {
      error_count++;
      console.error(prefix + 'Failed');
      console.error('Origin: ' + original.toString());
      console.error('Result: ' + result.toString());
      console.error('Should: ' + should_be.toString());
    }

    if (debug_mode) {
      debugger;    
    }

  });

  if (error_count > 0) {
    console.error(error_count + ' Failures.');
  } else {
    console.log('All tests passed.');
  }

}

run_tests(prepare_testcases());




function _generateRandomArray(pSize, pMax) {
  var tResult = new Array(pSize);

  for (var i = 0; i < pSize; i++) {
    tResult[i] = Math.floor(pMax * Math.random());
  }

  return tResult;
}

function _arrayEqual(pA, pB) {
  if (pA.length !== pB.length) {
    return false;
  }

  for (var i = 0; i < pA.length; i++) {
    if (pA[i] !== pB[i]) {
      return false;
    }
  }

  return true;
}

function arrayEqual(pA, pB) {
  if (_arrayEqual(pA, pB)) {
    console.log('Passed');
  } else {
    console.error('Failed!');
    console.error(pA);
    console.error(pB);
  }

}
