#!/usr/bin/node
const ndict = require('./101-data').dict;

const list_ = Object.entries(ndict);
const v = Object.values(ndict);
const vu = [...new Set(v)];
const dict_ = {};
for (const i in vu) {
  const nlist = [];
  for (const j in list_) {
    if (list_[k][1] === vu[i]) {
      nlist.unshift(list_[k][0]);
    }
  }
  dict[vu[i]] = nlist;
}
console.log(dict_);
