#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  let counter = 0;
  for (; counter < x; counter++) {
    func();
  }
};
