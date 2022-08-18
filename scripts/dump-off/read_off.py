#! /usr/bin/env python3

import os
import sys
import util

'''
Parse 'cmap' table, returns hash
  version: Table version number (0)
  num: number of encoding tables
  records: array of encoding records (hash below)
    platform: platform ID
    encoding: platform specific encoding ID
    offset: byte offset from beginning of 'cmap'
    format: subtable format
    length: byte length of subtable
    language: (partly included) language field
'''
def ParseCmap(fname, offset):
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
  for rec in er:
    off = offset + rec['offset']
    fp.seek(off, os.SEEK_SET)
    rec['format'] = int.from_bytes(fp.read(2), 'big')
    if rec['format'] in [0, 2, 4, 6]:
      rec['length'] = int.from_bytes(fp.read(2), 'big')
      rec['language'] = int.from_bytes(fp.read(2), 'big')
    elif rec['format'] in [8, 10, 12, 13]:
      tmp = fp.read(2)
      rec['length'] = int.from_bytes(fp.read(4), 'big')
      rec['language'] = int.from_bytes(fp.read(4), 'big')
    elif rec['format'] in [14]:
      rec['length'] = int.from_bytes(fp.read(4), 'big')
  tdat['records'] = er
  return tdat

def PrintCmapOverview(fdat):
  print('cmap table information')
  print('  version: {}'.format(fdat['version']))
  print('  number: {}'.format(fdat['num']))
  print('encoding records array:')
  print('  number PlatID EncID   Offset format length')
  for id in range(len(fdat['records'])):
    rec = fdat['records'][id]
    print('  {:>6}  {:>5} {:>5} {:>8} {:>6} {:>6}'.format(id, rec['platform'], rec['encoding'], rec['offset'], rec['format'], rec['length']))


