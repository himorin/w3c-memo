#! /usr/bin/env python3

import read_off
import table_defs
import util
import sys
import os

TAG_TTC = 0x74746366
TAG_TTF = 0x00010000
TAG_PSF = 0x4F54544F

def PrintCommands():
  print(
"""\
Commands
  (blank)   : display font file overview, with table index @TTF, font index @TTC

For TTF
  cmap      : summary of 'cmap' table (Character to Glyph index mapping)
  head      : dump 'head' table (font header table)
  hhea      : header table for horizontal layout
  vhea      : header table for vertical layout


For TTC (font collection)

""")

def ParseHead(fname):
  fp = open(fname, 'rb')
  fhead = {}
  fhead['tag'] = int.from_bytes(fp.read(4), 'big')
  if fhead['tag'] == TAG_TTC:
    fhead['tag_name'] = 'TTC';
    fhead['ver_maj'] = int.from_bytes(fp.read(2), 'big')
    fhead['ver_min'] = int.from_bytes(fp.read(2), 'big')
    fhead['num_fonts'] = int.from_bytes(fp.read(4), 'big')
    ParseTTCTableDirectory(fhead, fp)
  elif (fhead['tag'] == TAG_TTF) or (fhead['tag'] == TAG_PSF):
    fhead['tag_name'] = 'TTF';
    fhead['num_tables'] = int.from_bytes(fp.read(2), 'big')
    fhead['search_range'] = int.from_bytes(fp.read(2), 'big')
    fhead['entry_selector'] = int.from_bytes(fp.read(2), 'big')
    fhead['range_shift'] = int.from_bytes(fp.read(2), 'big')
    ParseTTFTableRecord(fhead, fp)
  else:
    raise Exception('Supplied file does not have font TAG')
  fp.close()
  fhead['fname'] = fname
  return fhead

def ParseTTFTableRecord(fhead, fp):
  ftables = {}
  for id in range(fhead['num_tables']):
    hname = fp.read(4).decode()
    hcheck = int.from_bytes(fp.read(4), 'big')
    hoffset = int.from_bytes(fp.read(4), 'big')
    hlen = int.from_bytes(fp.read(4), 'big')
    ftables[hname] = { 'offset': hoffset, 'len': hlen, 'checksum': hcheck }
  fhead['table_index'] = ftables

def ParseTTCTableDirectory(fhead, fp):
  fhead['font_offsets'] = []
  for id in range(fhead['num_fonts']):
    foffset = int.from_bytes(fp.read(4), 'big')
    fhead['font_offsets'].append(foffset)

def PrintHead(fhead):
  print('Font format: {}'.format(fhead['tag_name']))
  if fhead['tag_name'] == 'TTC':
    print('Number of fonts: {}'.format(fhead['num_fonts']))
    for id in range(len(fhead['font_offsets'])):
      print(' Table {:>3}: {:>8}'.format(id, fhead['font_offsets'][id]))
  else:
    print('Number of tables in head: {}'.format(fhead['num_tables']))
    print("Table Records:")
    print("NAME Offset     Length    checksum")
    for name, val in fhead['table_index'].items():
      print("{} {:>8}   {:>7}   {:08x}".format(name, val['offset'], val['len'], val['checksum']))

def PrintTTC(fhead, argv):
  return

def PrintTTF(fhead, argv):
  if argv[2] == 'cmap':
    fdat = read_off.ParseCmap(fhead['fname'], fhead['table_index']['cmap']['offset'])
    read_off.PrintCmapOverview(fdat)
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

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Usage: {} <fone file name> <options>".format(sys.argv[0]))
    print("       {} help".format(sys.argv[0]))
    exit()
  if sys.argv[1] == 'help':
    PrintCommands()
    exit()
  if not os.path.isfile(sys.argv[1]):
    print("File not found: {}".format(sys.argv[1]))
    exit()
  fhead = ParseHead(sys.argv[1])
  if len(sys.argv) == 2:
    PrintHead(fhead)
    exit()
  if fhead['tag_name'] == 'TTC':
    PrintTTC(fhead, sys.argv)
  else:
    PrintTTF(fhead, sys.argv)


