module.exports = {
  run: run_sort
};

function run_sort(input) {
  var step = Math.floor(input.length / 2);

  _iteration(input, step);

  return input;
}

function _iteration(input, step) {
  if (step == 0) return;

  for (var i = 0; i < step; i++) {
    _single_iter(input, step, i);
  }

  _iteration(input, Math.floor(step / 2));
  
}

function _single_iter(input, step, start) {
  var i, j;
  var curr, compare;

  for (i = step + start; i < input.length; i += step) {
    curr = input[i];

    for (j = i - step; j >= start; j -= step) {
      compare = input[j];

      if (curr < compare) {
        input[j + step] = compare;
      } else {
        input[j + step] = curr;
        break;
      }
    }

    if (j < start) {
      input[start] = curr;
    }

  }

}