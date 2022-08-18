#! /usr/bin/env python3

import os
import sys
import util

TABLE_HEAD = [
  {'type': 'uint16', 'name': 'ver_maj', 'desc': 'major version'},
  {'type': 'uint16', 'name': 'ver_min', 'desc': 'minor version'},
  {'type': 'Fixed', 'name': 'rev', 'desc': 'revision by manufacturer'},
  {'type': 'uint32', 'name': 'checksum', 'desc': 'checksum adjustment'},
  {'type': 'uint32', 'name': 'magic', 'desc': 'magic number', 'fixed': 0x5F0F3CF5},
  {'type': 'uint16', 'name': 'flags', 'desc': 'bit flags (0-15 bits)'},
  {'type': 'uint16', 'name': 'unit', 'desc': 'units per EM'},
  {'type': 'LONGDATETIME', 'name': 't_create', 'desc': 'created at'},
  {'type': 'LONGDATETIME', 'name': 't_modify', 'desc': 'modified at'},
  {'type': 'int16', 'name': 'x_min', 'desc': 'Min X of bounding box'},
  {'type': 'int16', 'name': 'y_min', 'desc': 'Min Y of bounding box'},
  {'type': 'int16', 'name': 'x_max', 'desc': 'Max X of bounding box'},
  {'type': 'int16', 'name': 'y_max', 'desc': 'Max Y of bounding box'},
  {'type': 'uint16', 'name': 'macstyle', 'desc': 'bit flags of font style'},
  {'type': 'uint16', 'name': 'ppem', 'desc': 'Smallest readable size in pixels'},
  {'type': 'int16', 'name': 'directionhint', 'desc': '', 'fixed': 2},
  {'type': 'int16', 'name': 'off_form', 'desc': 'offset format'},
  {'type': 'int16', 'name': 'glyph', 'desc': 'glyph format'},
]

'''
Parse 'head' table, returns hash (see TABLE_HEAD array)
'''
def ParseHead(fname, offset):
  fp = open(fname, 'rb')
  fp.seek(offset, os.SEEK_SET)
  tdat = util.ReadHeaderArray(fp, TABLE_HEAD)
  fp.close()
  return tdat

def PrintHead(tdat):
  print('head table information')
  print('majorVersion: {}'.format(tdat['ver_maj']))
  print('minorVersion: {}'.format(tdat['ver_min']))
  print('fontRevision: {}'.format(tdat['rev']))
  print('flags: {:016b}'.format(tdat['flags']))
  print('unitsPerEm: {}'.format(tdat['unit']))
  print('created: {}'.format(tdat['t_create']))
  print('modified: {}'.format(tdat['t_modify']))
  print('Bounding box: x({}, {}), y({}, {})'.format(tdat['x_min'], tdat['x_max'], tdat['y_min'], tdat['y_max']))
  print('style: {:07b}'.format(tdat['macstyle']))
  print('smallest pixel: {}'.format(tdat['ppem']))
  print('offset format: {}'.format(tdat['off_form']))
  print('glyph format: {}'.format(tdat['glyph']))

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


