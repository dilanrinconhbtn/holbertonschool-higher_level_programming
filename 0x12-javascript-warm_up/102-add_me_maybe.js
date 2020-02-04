#!/usr/bin/node
exports.addMeMaybe = function (x, func) {
    x = x + 1;
    func(x);
  };