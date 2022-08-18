#! /usr/bin/env python3

# 'head' table
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

# 'hhea' table
TABLE_HHEA = [
  {'type': 'uint16', 'name': 'ver_maj', 'desc': 'major version'},
  {'type': 'uint16', 'name': 'ver_min', 'desc': 'minor version'},
  {'type': 'FWORD', 'name': 'ascender', 'desc': 'Typographic ascent'},
  {'type': 'FWORD', 'name': 'descender', 'desc': 'Typographic descent'},
  {'type': 'FWORD', 'name': 'linegap', 'desc': 'Typographic line gap'},
  {'type': 'UFWORD', 'name': 'max_adv', 'desc': 'Max advance width'},
  {'type': 'FWORD', 'name': 'minLSB', 'desc': 'min left sidebearing'},
  {'type': 'FWORD', 'name': 'minRSB', 'desc': 'min right sidebearing'},
  {'type': 'FWORD', 'name': 'xmaxext', 'desc': 'x Max extent'},
  {'type': 'int16', 'name': 'caret_rise', 'desc': 'slope of cursor', 'comp': 1},
  {'type': 'int16', 'name': 'caret_run', 'desc': 'slope of cursor', 'comp': 1},
  {'type': 'int16', 'name': 'caret_off', 'desc': 'slant amount', 'comp': 1},
  {'type': 'int16', 'name': 'reserved0', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved1', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved2', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved3', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'format', 'desc': 'metric data format'},
  {'type': 'uint16', 'name': 'num_hmtx', 'desc': 'number of hMetric entries in hmtx'},
]
TABLE_HHEA_FORMAT = [
  'caret: slope ({0[caret_rise]}/ {0[caret_run]}), slant offset {0[caret_off]}'
]

# 'vhea' table
TABLE_VHEA = [
  {'type': 'Version16Dot16', 'name': 'ver', 'desc': 'Version'},
  {'type': 'int16', 'name': 'ascent', 'desc': 'From center to previous descent'},
  {'type': 'int16', 'name': 'descent', 'desc': 'From center to next ascent'},
  {'type': 'int16', 'name': 'linegap', 'desc': 'reserved', 'fixed': 0},
  {'type': 'int16', 'name': 'max_adv', 'desc': 'maximum advance height'},
  {'type': 'int16', 'name': 'minTSB', 'desc': 'min top sidebearing'},
  {'type': 'int16', 'name': 'minBSB', 'desc': 'min bottom sidebearing'},
  {'type': 'int16', 'name': 'ymaxext', 'desc': 'y max extent'},
  {'type': 'int16', 'name': 'caret_rise', 'desc': 'slope of caret', 'comp': 1},
  {'type': 'int16', 'name': 'caret_run', 'desc': 'slope of caret', 'comp': 1},
  {'type': 'int16', 'name': 'caret_off', 'desc': 'slant amount', 'comp': 1},
  {'type': 'int16', 'name': 'reserved0', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved1', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved2', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved3', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'format', 'desc': 'metric data format', 'fixed': 0},
  {'type': 'uint16', 'name': 'num_vmtx', 'desc': 'number of VMetric entries in vmtx'},
]
TABLE_VHEA_FORMAT = [
  'caret: slope ({0[caret_rise]}/ {0[caret_run]}), slant offset {0[caret_off]}'
]

