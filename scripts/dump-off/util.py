#! /usr/bin/env python3

import os
import sys

'''
Read continuous header array by array of target
  fp: file descriptor, set seek to start point to read
  target: array of hash of target data to read
format of 'target': array of hash as
  type: type of value, also taken as byte length
  name: tag name of value, used as hash ID of return
  desc: description for print
  fixed: if fixed value or deprecated, set this as its value
  comp: composited value, not to be displayed as single
        parsing function should provide format string array with 'name' as id
return: hash of value with 'name' as ID
'''
def ReadHeaderArray(fp, target):
  ret = {}
  for tgt in target:
    if tgt['type'] == 'uint8':
      ret[tgt['name']] = int.from_bytes(fp.read(1), 'big')
    elif tgt['type'] == 'int8':
      ret[tgt['name']] = int.from_bytes(fp.read(1), 'big', signed=True)
    elif tgt['type'] == 'uint16':
      ret[tgt['name']] = int.from_bytes(fp.read(2), 'big')
    elif tgt['type'] == 'int16':
      ret[tgt['name']] = int.from_bytes(fp.read(2), 'big', signed=True)
    elif tgt['type'] == 'uint24':
      ret[tgt['name']] = int.from_bytes(fp.read(3), 'big')
    elif tgt['type'] == 'uint32':
      ret[tgt['name']] = int.from_bytes(fp.read(4), 'big')
    elif tgt['type'] == 'int32':
      ret[tgt['name']] = int.from_bytes(fp.read(4), 'big', signed=True)
    elif tgt['type'] == 'Fixed':
      ret[tgt['name']] = int.from_bytes(fp.read(4), 'big')
    elif tgt['type'] == 'FWORD':
      ret[tgt['name']] = int.from_bytes(fp.read(2), 'big', signed=True)
    elif tgt['type'] == 'UFWORD':
      ret[tgt['name']] = int.from_bytes(fp.read(2), 'big')
    elif tgt['type'] == 'F2DOT14':
      ret[tgt['name']] = int.from_bytes(fp.read(2), 'big')
    elif tgt['type'] == 'LONGDATETIME':
      ret[tgt['name']] = int.from_bytes(fp.read(8), 'big', signed=True)
    elif tgt['type'] == 'Tag':
      ret[tgt['name']] = int.from_bytes(fp.read(4), 'big')
    elif tgt['type'] == 'Offset16':
      ret[tgt['name']] = int.from_bytes(fp.read(2), 'big')
    elif tgt['type'] == 'Offset24':
      ret[tgt['name']] = int.from_bytes(fp.read(3), 'big')
    elif tgt['type'] == 'Offset32':
      ret[tgt['name']] = int.from_bytes(fp.read(4), 'big')
    elif tgt['type'] == 'Version16Dot16':
      tmp = int.from_bytes(fp.read(4), 'big')
      ret[tgt['name']] = (tmp >> 16) + (float((tmp & 0xF000) >> 12) / 10.0)
  return ret

def ParseHeaderArray(fname, offset, table):
  fp = open(fname, 'rb')
  fp.seek(offset, os.SEEK_SET)
  tdat = ReadHeaderArray(fp, table)
  fp.close()
  return tdat

def PrintHeaderArray(tdat, table, format):
  for tgt in table:
    if ('fixed' not in tgt) and ('comp' not in tgt):
      print('{}: {}'.format(tgt['desc'], tdat[tgt['name']]))
  for tgt in format:
    print(tgt.format(tdat))

def PPHeaderArray(fname, offset, table, format):
  PrintHeaderArray(
    ParseHeaderArray(fname, offset, table), table, format)


