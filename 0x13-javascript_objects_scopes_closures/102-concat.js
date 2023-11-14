#!/usr/bin/node
const file_ = require('fs');

const Arg0 = file_.readFileSync(process.argv[2]).toString();
const Arg1 = file_.readFileSync(process.argv[3]).toString();
file_.writeFileSync(process.argv[4], Arg0 + Arg1);
