#! /usr/bin/env python3

import os
import sys

'''
Parse 'cmap' table, returns hash
  version: Table version number (0)
  num: number of encoding tables
  records: array of encoding records (hash below)
    platform: platform ID
    encoding: platform specific encoding ID
    offset: byte offset from beginning of 'cmap'
'''
def ParseTablecmap(fname, offset):
  tdat = {}
  fp = open(fname, 'rb')
  fp.seek(offset, os.SEEK_SET)
  tdat['version'] = int.from_bytes(fp.read(2), 'big')
  tdat['num'] = int.from_bytes(fp.read(2), 'big')
  er = []
  for id in range(tdat['num']):
    rec = {}
    rec['platform'] = int.from_bytes(fp.read(2), 'big')
    rec['encoding'] = int.from_bytes(fp.read(2), 'big')
    rec['offset'] = int.from_bytes(fp.read(4), 'big')
    er.append(rec)
  tdat['records'] = er
  return tdat


