#!/usr/bin/node
exports.esrever = function (list) {
  let lenth = list.length - 1;
  let i = 0;
  while ((lenth - i) > 0) {
    const temp = list[lenth];
    list[lenth] = list[i];
    list[i] = temp;
    i++;
    lenth--;
  }
  return list;
};
