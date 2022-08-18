#! /usr/bin/env python3

import table_defs
import util

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

def PrintTTF(fhead, argv):
  if argv[2] == 'cmap':
    fdat = ParseCmap(fhead['fname'], fhead['table_index']['cmap']['offset'])
    PrintCmapOverview(fdat)
  elif argv[2] == 'head':
    print('head table information')
    util.PPHeaderArray(
      fhead['fname'], fhead['table_index']['head']['offset'], 
      table_defs.TABLE_HEAD, table_defs.TABLE_HEAD_FORMAT)
  elif argv[2] == 'hhea':
    print('hhea table information')
    util.PPHeaderArray(
      fhead['fname'], fhead['table_index']['hhea']['offset'], 
      table_defs.TABLE_HHEA, table_defs.TABLE_HHEA_FORMAT)
  elif argv[2] == 'vhea':
    print('vhea table information')
    util.PPHeaderArray(
      fhead['fname'], fhead['table_index']['hhea']['offset'], 
      table_defs.TABLE_VHEA, table_defs.TABLE_VHEA_FORMAT)
  elif argv[2] == 'maxp':
    print('maxp table information')
    fdat = util.ParseHeaderArray(
      fhead['fname'], fhead['table_index']['maxp']['offset'],
      table_defs.TABLE_MAXP)
    util.PrintHeaderArray(fdat, table_defs.TABLE_MAXP, [])
    if fdat['ver'] == 1.0:
      util.PPHeaderArray(
        fhead['fname'], fhead['table_index']['maxp']['offset'] + 6, 
        table_defs.TABLE_MAXP_1_0, [])
  elif argv[2] == 'OS2':
    print('OS/2 table information')
    fdat = util.ParseHeaderArray(
      fhead['fname'], fhead['table_index']['OS/2']['offset'],
      table_defs.TABLE_OS2)
    util.PrintHeaderArray(fdat, table_defs.TABLE_OS2, [])
    if fdat['ver'] > 0:
      util.PPHeaderArray(
        fhead['fname'], fhead['table_index']['OS/2']['offset'] + 78, 
        table_defs.TABLE_OS2_1, [])
    if fdat['ver'] > 1:
      util.PPHeaderArray(
        fhead['fname'], fhead['table_index']['OS/2']['offset'] + 86, 
        table_defs.TABLE_OS2_4, [])
    if fdat['ver'] > 4:
      util.PPHeaderArray(
        fhead['fname'], fhead['table_index']['OS/2']['offset'] + 96, 
        table_defs.TABLE_OS2_5, [])


