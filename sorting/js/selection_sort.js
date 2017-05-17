module.exports = {
  run: run_sort
};

function run_sort(input) {
  var candidate, index;
  var i, j;

  for (i = 0; i < input.length - 1; i++) {
    candidate = Infinity;
    for (j = i; j < input.length; j++){
      if (input[j] < candidate) {
        candidate = input[j];    
        index = j;
      }
    }

    _swap(input, i, index);
  }

  return input;
}


function _swap(input, a, b) {
  if (a === b) return;

  var temp = input[a];
  input[a] = input[b];
  input[b] = temp;
}