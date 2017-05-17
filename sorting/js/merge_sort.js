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

  var dest = input.slice();

  _merge_sort(input, dest, 0, input.length - 1);

  return dest;
}


function _merge_sort(input, dest, start, end) {
  if (debug_mode) {
    var id = global_id++;
    console.log('[' + id + ']-------Start _merge_sort: from: ' + start + ' to: ' + end + ' ---------');
    console.log('input: ' + input.toString());
    console.log('dest:  ' + dest.toString());    
  }

  if (start >= end) {
    if (debug_mode) {
        console.log('[' + id + ']-------Direct Finished _merge_sort: from: ' + start + ' to: ' + end + ' ---------');
    }
    return;
  }

  var mid = Math.floor(start + (end - start) / 2);
  _merge_sort(dest, input, start, mid);
  _merge_sort(dest, input, mid + 1, end);

  _merge(input, dest, start, mid + 1, end);

  if (debug_mode) {
    console.log('[' + id + ']-------Finished _merge_sort: from: ' + start + ' to: ' + end + ' ---------');
    console.log('input: ' + input.toString());
    console.log('dest:  ' + dest.toString());    
  }
}

function _merge(input, dest, start_l, start_r, end) {
  if (debug_mode) {
    var id = global_id++;
    console.log('[' + id + ']-------Start _merge: left: ' + start_l + ' right: ' + start_r + ' end: ' + end + ' ---------');
    console.log('input: ' + input.toString());
    console.log('dest:  ' + dest.toString());    
  }

  var l = start_l, r = start_r;
  var i = l;

  while (l < start_r || r <= end) {
    if (l >= start_r) {
      dest[i++] = input[r++];
    } else if (r > end) {
      dest[i++] = input[l++];
    } else if (input[l] <= input[r]) {
      dest[i++] = input[l++];
    } else {
      dest[i++] = input[r++];
    }
  }

  if (debug_mode) {
    console.log('[' + id + ']-------Finished _merge: left: ' + start_l + ' right: ' + start_r + ' end: ' + end + ' ---------');
    console.log('input: ' + input.toString());
    console.log('dest:  ' + dest.toString());    
  }

}