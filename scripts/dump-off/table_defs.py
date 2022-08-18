#! /usr/bin/env python3

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
  {'type': 'int16', 'name': 'x_min', 'desc': 'Min X of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'y_min', 'desc': 'Min Y of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'x_max', 'desc': 'Max X of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'y_max', 'desc': 'Max Y of bounding box', 'comp': 1},
  {'type': 'uint16', 'name': 'macstyle', 'desc': 'bit flags of font style'},
  {'type': 'uint16', 'name': 'ppem', 'desc': 'Smallest readable size in pixels'},
  {'type': 'int16', 'name': 'directionhint', 'desc': '', 'fixed': 2},
  {'type': 'int16', 'name': 'off_form', 'desc': 'offset format'},
  {'type': 'int16', 'name': 'glyph', 'desc': 'glyph format'},
]
TABLE_HEAD_FORMAT = [
  'Bounding box: x({0[x_min]}, {0[x_max]}), y({0[y_min]}, {0[y_max]})'
]

