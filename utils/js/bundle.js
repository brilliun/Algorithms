(function(global) {
  if (typeof document !== 'undefined') {
    var mModules = {
      assert: {
        deepStrictEqual: function() {
          return;
        }
      }
    };

    global.require = function(pModule) {
      return mModules[pModule];
    };
  }
}(window));
