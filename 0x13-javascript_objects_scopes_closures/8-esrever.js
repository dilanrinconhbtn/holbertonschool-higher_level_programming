#!/usr/bin/node
exports.esrever = function (list) {
  let n_list = [];
  for (let index = list.length - 1; index >= 0; index--) {
    n_list.push(list[index]);
  }
  return n_list;
};
