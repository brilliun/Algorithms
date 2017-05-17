module.exports = {
  run: run_sort
};

function run_sort(input) {
  var i, j;
  var curr, compare;

  for (i = 1; i < input.length; i++) {
    curr = input[i];

    for (j = i - 1; j >= 0; j--) {
      compare = input[j];

      if (curr < compare) {
        input[j + 1] = compare;
      } else {
        input[j + 1] = curr;
        break;
      }
    }

    if (j < 0) {
      input[0] = curr;
    }
  }

  return input;
}

