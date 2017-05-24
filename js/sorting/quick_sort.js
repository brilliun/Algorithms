module.exports = {
  run: run_sort
};

var global_id;
var debug_mode = false;


function run_sort(input, options) {
  if (options.debug_mode) {
    global_id = 0;
    debug_mode = true;    
  }

  _sort(input, 0, input.length - 1);

  return input;
}

function _sort(input, start, end) {
  if (debug_mode) {
    var id = global_id++;
    console.log('[' + id + ']-------Start _sort: from: ' + start + ' to: ' + end + ' ---------');
    console.log('input: ' + input.toString());
  }

  if (end <= start) {
    if (debug_mode) {
      console.log('[' + id + ']-------Direct Finished _sort: from: ' + start + ' to: ' + end + ' ---------');
    }
    return;
  }

  var pivot = _partition(input, start, end);

  _sort(input, start, pivot - 1);
  _sort(input, pivot + 1, end);

  if (debug_mode) {
    console.log('[' + id + ']-------Finished _sort: from: ' + start + ' to: ' + end + ' ---------');
    console.log('input: ' + input.toString());
  }
}

function _partition(input, start, end) {
  if (debug_mode) {
    var id = global_id++;
    console.log('[' + id + ']-------Start _partition: start: ' + start  + ' end: ' + end + ' ---------');
    console.log('input: ' + input.toString());
  }
  var mid = input[start];
  var l = start + 1, r = end;

  while (true) {
    while (l <= end && input[l] <= mid) l++;
    while (r > start && input[r] > mid) r--;
    if (l >= r) break;
    _swap(input, l, r);
    l++;
    r--;
  }

  _swap(input, start, r);

  if (debug_mode) {
    console.log('[' + id + ']-------Finished _partition: start: ' + start  + ' end: ' + end + ' ---------');
    console.log('input: ' + input.toString());
  }

  return r;
}

function _swap(input, a, b) {
  var temp = input[a];
  input[a] = input[b];
  input[b] = temp;
}