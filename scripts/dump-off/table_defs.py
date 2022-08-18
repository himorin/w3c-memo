#! /usr/bin/env python3

# 'head' table
TABLE_HEAD = [
  {'type': 'uint16', 'name': 'ver_maj', 'desc': 'major version'},
  {'type': 'uint16', 'name': 'ver_min', 'desc': 'minor version'},
  {'type': 'Fixed', 'name': 'rev', 'desc': 'revision by manufacturer'},
  {'type': 'uint32', 'name': 'checksum', 'desc': 'checksum adjustment', 'disp': 'x8'},
  {'type': 'uint32', 'name': 'magic', 'desc': 'magic number', 'fixed': 0x5F0F3CF5},
  {'type': 'uint16', 'name': 'flags', 'desc': 'bit flags (0-15 bits)', 'disp': 'b16'},
  {'type': 'uint16', 'name': 'unit', 'desc': 'units per EM'},
  {'type': 'LONGDATETIME', 'name': 't_create', 'desc': 'created at'},
  {'type': 'LONGDATETIME', 'name': 't_modify', 'desc': 'modified at'},
  {'type': 'int16', 'name': 'x_min', 'desc': 'Min X of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'y_min', 'desc': 'Min Y of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'x_max', 'desc': 'Max X of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'y_max', 'desc': 'Max Y of bounding box', 'comp': 1},
  {'type': 'uint16', 'name': 'macstyle', 'desc': 'bit flags of font style', 'disp': 'b16'},
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

# 'maxp' table
TABLE_MAXP = [
  {'type': 'Version16Dot16', 'name': 'ver', 'desc': 'Version'},
  {'type': 'uint16', 'name': 'num_glyphs', 'desc': 'number of glyphs'},
]
TABLE_MAXP_1_0 = [
  {'type': 'uint16', 'name': 'points', 'desc': 'max points in non-composite'},
  {'type': 'uint16', 'name': 'contours', 'desc': 'max contours in non-composite'},
  {'type': 'uint16', 'name': 'comp_point', 'desc': 'max points in composite'},
  {'type': 'uint16', 'name': 'comp_cont', 'desc': 'max contours in composite'},
  {'type': 'uint16', 'name': 'zone', 'desc': '1 for no twilight zone, 2 for using'},
  {'type': 'uint16', 'name': 'twilight', 'desc': 'max points in twilight zone'},
  {'type': 'uint16', 'name': 'storage', 'desc': 'storage area locations'},
  {'type': 'uint16', 'name': 'fdefs', 'desc': 'number of FDEF'},
  {'type': 'uint16', 'name': 'idefs', 'desc': 'number of IDEF'},
  {'type': 'uint16', 'name': 'stak', 'desc': 'max stack depth in program'},
  {'type': 'uint16', 'name': 's_inst', 'desc': 'max byte for glyph instructions'},
  {'type': 'uint16', 'name': 'comp_elem', 'desc': 'max components at top level'},
  {'type': 'uint16', 'name': 'comp_dep', 'desc': 'max levelof recursion'},
]

# 'OS/2' table
TABLE_OS2 = [
  {'type': 'uint16', 'name': 'ver', 'desc': 'version'},
  {'type': 'int16', 'name': 'xAvgCharWidth', 'desc': 'Average weighted escapement'},
  {'type': 'uint16', 'name': 'usWeightClass', 'desc': 'Weight class'},
  {'type': 'uint16', 'name': 'usWidthClass', 'desc': 'Width class'},
  {'type': 'uint16', 'name': 'fsType', 'desc': 'Type flags', 'disp': 'b16'},
  {'type': 'int16', 'name': 'sub_x', 'desc': 'subscript horizontal font size'},
  {'type': 'int16', 'name': 'sub_y', 'desc': 'subscript vertical font size'},
  {'type': 'int16', 'name': 'sub_xoff', 'desc': 'subscript X offset'},
  {'type': 'int16', 'name': 'sub_yoff', 'desc': 'subscript Y offset'},
  {'type': 'int16', 'name': 'sup_x', 'desc': 'superscript horizontal font size'},
  {'type': 'int16', 'name': 'sup_y', 'desc': 'superscript vertical font size'},
  {'type': 'int16', 'name': 'sup_xoff', 'desc': 'superscript X offset'},
  {'type': 'int16', 'name': 'sup_yoff', 'desc': 'superscript Y offset'},
  {'type': 'int16', 'name': 'strike_size', 'desc': 'strikeout size'},
  {'type': 'int16', 'name': 'strike_pos', 'desc': 'strikeout position'},
  {'type': 'int16', 'name': 'family_class', 'desc': 'font-family class and subclass'},
  {'type': 'uint8', 'name': 'p_family', 'desc': 'PANOSE family type'},
  {'type': 'uint8', 'name': 'p_serif', 'desc': 'PANOSE serif style'},
  {'type': 'uint8', 'name': 'p_weight', 'desc': 'PANOSE weight'},
  {'type': 'uint8', 'name': 'p_prop', 'desc': 'PANOSE proportion'},
  {'type': 'uint8', 'name': 'p_contrast', 'desc': 'PANOSE contrast'},
  {'type': 'uint8', 'name': 'p_stroke', 'desc': 'PANOSE stroke variation'},
  {'type': 'uint8', 'name': 'p_arm', 'desc': 'PANOSE arm style'},
  {'type': 'uint8', 'name': 'p_letter', 'desc': 'PANOSE letter form'},
  {'type': 'uint8', 'name': 'p_mid', 'desc': 'PANOSE midline'},
  {'type': 'uint8', 'name': 'p_xheight', 'desc': 'PANOSE XHeight'},
  {'type': 'uint32', 'name': 'uran1', 'desc': 'unicode character range 1', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'uran2', 'desc': 'unicode character range 2', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'uran3', 'desc': 'unicode character range 3', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'uren4', 'desc': 'unicode character range 4', 'disp': 'b32'},
  {'type': 'Tag', 'name': 'vend_id', 'desc': 'font verndor identification', 'disp': 's4'},
  {'type': 'uint16', 'name': 'fs_sel', 'desc': 'font selection flags', 'disp': 'b16'},
  {'type': 'uint16', 'name': 'char_first', 'desc': 'minimum unicode index'},
  {'type': 'uint16', 'name': 'char_last', 'desc': 'maximum unicode index'},
  {'type': 'int16', 'name': 'typo_ascend', 'desc': 'typographic ascender'},
  {'type': 'int16', 'name': 'typo_descend', 'desc': 'typographic descender'},
  {'type': 'int16', 'name': 'typo_linegap', 'desc': 'typographic line gap'},
  {'type': 'uint16', 'name': 'win_ascent', 'desc': 'windows ascender'},
  {'type': 'uint16', 'name': 'win_descent', 'desc': 'windows descender'},
]
TABLE_OS2_1 = [
  {'type': 'uint32', 'name': 'code_ran1', 'desc': 'code page character range 1', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'code_ran2', 'desc': 'code page character range 2', 'disp': 'b32'},
]
TABLE_OS2_4 = [
  {'type': 'int16', 'name': 'x_height', 'desc': 'so called x-Height'},
  {'type': 'int16', 'name': 'cap_height', 'desc': 'so called cap height'},
  {'type': 'uint16', 'name': 'char_def', 'desc': 'codepoint for default glyph'},
  {'type': 'uint16', 'name': 'char_break', 'desc': 'codepoint for default break char'},
  {'type': 'uint16', 'name': 'max_content', 'desc': 'max length of composition'},
]
TABLE_OS2_5 = [
  {'type': 'uint16', 'name': 'lower_psize', 'desc': 'lower size of design'},
  {'type': 'uint16', 'name': 'upper_psize', 'desc': 'upper size of design'},
]

