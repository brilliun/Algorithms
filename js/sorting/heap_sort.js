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

  if (input.length <= 1) return input;

  var heap = new Heap(input);
  var max;

  while(!heap.isEmpty()) {
    max = heap.delMax();
    input[heap.size()] = max;
  }

  return input;
}



function Heap(input) {
  this._data = input;
  this._size = 0;
  this._initialize();

  if (debug_mode) {
    console.log('After initialization:')
    console.log(this._data.toString());
  }
}

var tProto = Heap.prototype;

tProto.size = function() {
  return this._size; 
};

tProto.isEmpty = function() {
  return this.size() === 0;
};

tProto.insert = function(value) {
  var k = this.size();
  this._setAt(k, value);
  this._size++;
  this._swim(k);
};

tProto.delMax = function() {
  if (this.size() === 0) return null;

  var result = this._getAt(0);
  var newRoot;

  if (this.size() > 1) {  
    this._setAt(0, this._getAt(this.size() - 1));
    this._size--;
    this._sink(0);
  } else {
    this._size--;    
  }

  return result;
};

tProto._initialize = function() {
  var k = 0;
  var size = this._data.length;

  while (k < size) {
    this.insert(this._data[k++]);
  }
};

tProto._swim = function(k) {
  if (k <= 0 || k >= this.size()) return;

  var target = this._getAt(k);
  var parent;

  while (this._hasParent(k)) {
    parent = this._parentOf(k);

    if (parent < target) {
      this._setAt(k, parent);
      k = this._parentIndex(k);
    } else {
      break;
    }
  }

  this._setAt(k, target);
};

tProto._sink = function(k) {
  var leftK;
  var rightK;
  var largerChildIndex;
  var target = this._getAt(k);

  if (target === null) return;

  do {
    largerChildIndex = this._largerChildIndex(k);

    if (largerChildIndex === -1) break;

    if (this._getAt(largerChildIndex) > target) {
      this._setAt(k, this._getAt(largerChildIndex));
      k = largerChildIndex;
    } else {
      break;
    }
  } while (true)

  this._setAt(k, target);

  return;
};

tProto._hasParent = function(k) {
  return k > 0;
};

tProto._parentOf = function(k) {
  return this._getAt(this._parentIndex(k));
};

tProto._parentIndex = function(k) {
  return Math.floor((k + 1) / 2) - 1;
};

tProto._largerChildIndex = function(k) {
  var leftK = this._leftIndex(k);
  var rightK = this._rightIndex(k);
  var largerK;

  if (this._getAt(leftK) === null && this._getAt(rightK) === null) return -1;
  if (this._getAt(leftK) === null) {
    largerK = rightK;
  } else if (this._getAt(rightK) === null) {
    largerK = leftK;
  } else {
    largerK = this._getAt(leftK) >= this._getAt(rightK) ? leftK : rightK;
  }

  return largerK
};

tProto._leftIndex = function(k) {
  return (k + 1) * 2 - 1;
};

tProto._rightIndex = function(k) {
  return (k + 1) * 2;
};

tProto._getAt = function(p) {
  if (p < 0 || p >= this._size) return null;
  return this._data[p];
};

tProto._setAt = function(p, value) {
  if (p >= this._data.length || p < 0) return;
  this._data[p] = value;
}