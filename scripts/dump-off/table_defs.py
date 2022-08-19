#! /usr/bin/env python3

# 'head' table
TABLE_HEAD = [
  {'type': 'uint16', 'name': 'majorVersion', 'desc': 'major version'},
  {'type': 'uint16', 'name': 'minorVersion', 'desc': 'minor version'},
  {'type': 'Fixed', 'name': 'fontRevision', 'desc': 'revision by manufacturer'},
  {'type': 'uint32', 'name': 'checksumAdjustment', 'desc': 'checksum adjustment', 'disp': 'x8'},
  {'type': 'uint32', 'name': 'magicNumber', 'desc': 'magic number', 'fixed': 0x5F0F3CF5},
  {'type': 'uint16', 'name': 'flags', 'desc': 'bit flags (0-15 bits)', 'disp': 'b16'},
  {'type': 'uint16', 'name': 'unitsPerEm', 'desc': 'units per EM'},
  {'type': 'LONGDATETIME', 'name': 'created', 'desc': 'created at'},
  {'type': 'LONGDATETIME', 'name': 'modified', 'desc': 'modified at'},
  {'type': 'int16', 'name': 'xMin', 'desc': 'Min X of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'yMin', 'desc': 'Min Y of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'xMax', 'desc': 'Max X of bounding box', 'comp': 1},
  {'type': 'int16', 'name': 'yMax', 'desc': 'Max Y of bounding box', 'comp': 1},
  {'type': 'uint16', 'name': 'macStyle', 'desc': 'bit flags of font style', 'disp': 'b16'},
  {'type': 'uint16', 'name': 'lowestRecPPEM', 'desc': 'Smallest readable size in pixels'},
  {'type': 'int16', 'name': 'fontDirectionHint', 'desc': '', 'fixed': 2},
  {'type': 'int16', 'name': 'indexToLocFormat', 'desc': 'offset format'},
  {'type': 'int16', 'name': 'glyphDataFormat', 'desc': 'glyph format'},
]
TABLE_HEAD_FORMAT = [
  'Bounding box: x({0[xMin]}, {0[xMax]}), y({0[yMin]}, {0[yMax]})'
]

TABLE_HEAD_BIT_FLAGS = [
  'Baseline at y=0',
  'Left sidebearing point x=0',
  'Instructions may depend on point size',
  'Force ppem to int val (clear = fractional ppem size)',
  'Instructions may alter advance width',
  'unused in OpenType',
  'unused in OpenType',
  'unused in OpenType',
  'unused in OpenType',
  'unused in OpenType',
  'unused in OpenType',
  'Font data as lossless',
  'Font converted',
  'Font optimized for ClearType',
  'Last Resort font',
  'reserved',
]
TABLE_HEAD_BIT_MACSTYLE = [
  'Bold',
  'Italic',
  'Underline',
  'Outline',
  'Shadow',
  'Condensed',
  'Extended',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
]

# 'hhea' table
TABLE_HHEA = [
  {'type': 'uint16', 'name': 'majorVersion', 'desc': 'major version'},
  {'type': 'uint16', 'name': 'minorVersion', 'desc': 'minor version'},
  {'type': 'FWORD', 'name': 'ascender', 'desc': 'Typographic ascent'},
  {'type': 'FWORD', 'name': 'descender', 'desc': 'Typographic descent'},
  {'type': 'FWORD', 'name': 'lineGap', 'desc': 'Typographic line gap'},
  {'type': 'UFWORD', 'name': 'advanceWidthMax', 'desc': 'Max advance width'},
  {'type': 'FWORD', 'name': 'minLeftSideBearing', 'desc': 'min left sidebearing'},
  {'type': 'FWORD', 'name': 'minRightSideBearing', 'desc': 'min right sidebearing'},
  {'type': 'FWORD', 'name': 'xMaxExtent', 'desc': 'x Max extent'},
  {'type': 'int16', 'name': 'caretSlopeRise', 'desc': 'slope of cursor', 'comp': 1},
  {'type': 'int16', 'name': 'caretSlopeRun', 'desc': 'slope of cursor', 'comp': 1},
  {'type': 'int16', 'name': 'caretOffset', 'desc': 'slant amount', 'comp': 1},
  {'type': 'int16', 'name': 'reserved0', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved1', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved2', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved3', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'metricDataFormat', 'desc': 'metric data format'},
  {'type': 'uint16', 'name': 'numberOfHMetrics', 'desc': 'number of hMetric entries in hmtx'},
]
TABLE_HHEA_FORMAT = [
  'caret: slope ({0[caretSlopeRise]}/ {0[caretSlopeRun]}), slant offset {0[caretOffset]}'
]

# 'vhea' table
TABLE_VHEA = [
  {'type': 'Version16Dot16', 'name': 'version', 'desc': 'Version'},
  {'type': 'int16', 'name': 'ascent', 'desc': 'From center to previous descent'},
  {'type': 'int16', 'name': 'descent', 'desc': 'From center to next ascent'},
  {'type': 'int16', 'name': 'lineGap', 'desc': 'reserved', 'fixed': 0},
  {'type': 'int16', 'name': 'advanceHeightMax', 'desc': 'maximum advance height'},
  {'type': 'int16', 'name': 'minTopSideBearing', 'desc': 'min top sidebearing'},
  {'type': 'int16', 'name': 'minBottomSideBearing', 'desc': 'min bottom sidebearing'},
  {'type': 'int16', 'name': 'yMaxExtent', 'desc': 'y max extent'},
  {'type': 'int16', 'name': 'caretSlopeRise', 'desc': 'slope of caret', 'comp': 1},
  {'type': 'int16', 'name': 'caretSlopeRun', 'desc': 'slope of caret', 'comp': 1},
  {'type': 'int16', 'name': 'caretOffset', 'desc': 'slant amount', 'comp': 1},
  {'type': 'int16', 'name': 'reserved0', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved1', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved2', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'reserved3', 'desc': '', 'fixed': 0},
  {'type': 'int16', 'name': 'metricDataFormat', 'desc': 'metric data format', 'fixed': 0},
  {'type': 'uint16', 'name': 'numOfLongVerMetrics', 'desc': 'number of VMetric entries in vmtx'},
]
TABLE_VHEA_FORMAT = [
  'caret: slope ({0[caretSlopeRise]}/ {0[caretSlopeRun]}), slant offset {0[caretOffset]}'
]

# 'maxp' table
TABLE_MAXP = [
  {'type': 'Version16Dot16', 'name': 'version', 'desc': 'Version'},
  {'type': 'uint16', 'name': 'numGlyphs', 'desc': 'number of glyphs'},
]
TABLE_MAXP_1_0 = [
  {'type': 'uint16', 'name': 'maxPoints', 'desc': 'max points in non-composite'},
  {'type': 'uint16', 'name': 'maxContours', 'desc': 'max contours in non-composite'},
  {'type': 'uint16', 'name': 'maxCompositePoints', 'desc': 'max points in composite'},
  {'type': 'uint16', 'name': 'maxCompositeContours', 'desc': 'max contours in composite'},
  {'type': 'uint16', 'name': 'maxZones', 'desc': '1 for no twilight zone, 2 for using'},
  {'type': 'uint16', 'name': 'maxTwilightPoints', 'desc': 'max points in twilight zone'},
  {'type': 'uint16', 'name': 'maxStorage', 'desc': 'storage area locations'},
  {'type': 'uint16', 'name': 'maxFunctionDefs', 'desc': 'number of FDEF'},
  {'type': 'uint16', 'name': 'maxInstructionDefs', 'desc': 'number of IDEF'},
  {'type': 'uint16', 'name': 'maxStackElements', 'desc': 'max stack depth in program'},
  {'type': 'uint16', 'name': 'maxSizeOfInstructions', 'desc': 'max byte for glyph instructions'},
  {'type': 'uint16', 'name': 'maxComponentElements', 'desc': 'max components at top level'},
  {'type': 'uint16', 'name': 'maxComponentDepth', 'desc': 'max levelof recursion'},
]

# 'OS/2' table
TABLE_OS2 = [
  {'type': 'uint16', 'name': 'version', 'desc': 'version'},
  {'type': 'int16', 'name': 'xAvgCharWidth', 'desc': 'Average weighted escapement'},
  {'type': 'uint16', 'name': 'usWeightClass', 'desc': 'Weight class'},
  {'type': 'uint16', 'name': 'usWidthClass', 'desc': 'Width class'},
  {'type': 'uint16', 'name': 'fsType', 'desc': 'Type flags', 'disp': 'b16'},
  {'type': 'int16', 'name': 'ySubscriptXSize', 'desc': 'subscript horizontal font size'},
  {'type': 'int16', 'name': 'ySubscriptYSize', 'desc': 'subscript vertical font size'},
  {'type': 'int16', 'name': 'ySubscriptXOffset', 'desc': 'subscript X offset'},
  {'type': 'int16', 'name': 'ySubscriptYOffset', 'desc': 'subscript Y offset'},
  {'type': 'int16', 'name': 'ySuperscriptXSize', 'desc': 'superscript horizontal font size'},
  {'type': 'int16', 'name': 'ySuperscriptYSize', 'desc': 'superscript vertical font size'},
  {'type': 'int16', 'name': 'ySuperscriptXOffset', 'desc': 'superscript X offset'},
  {'type': 'int16', 'name': 'ySuperscriptYOffset', 'desc': 'superscript Y offset'},
  {'type': 'int16', 'name': 'yStrikeoutSize', 'desc': 'strikeout size'},
  {'type': 'int16', 'name': 'yStrikeoutPosition', 'desc': 'strikeout position'},
  {'type': 'int16', 'name': 'sFamilyClass', 'desc': 'font-family class and subclass'},
  {'type': 'uint8', 'name': 'panose_bFamilyType', 'desc': 'PANOSE family type'},
  {'type': 'uint8', 'name': 'panose_bSerifStyle', 'desc': 'PANOSE serif style'},
  {'type': 'uint8', 'name': 'panose_bWeight', 'desc': 'PANOSE weight'},
  {'type': 'uint8', 'name': 'panose_bProportion', 'desc': 'PANOSE proportion'},
  {'type': 'uint8', 'name': 'panose_bContrast', 'desc': 'PANOSE contrast'},
  {'type': 'uint8', 'name': 'panose_bStrokeVariation', 'desc': 'PANOSE stroke variation'},
  {'type': 'uint8', 'name': 'panose_bArmStyle', 'desc': 'PANOSE arm style'},
  {'type': 'uint8', 'name': 'panose_bLetterform', 'desc': 'PANOSE letter form'},
  {'type': 'uint8', 'name': 'panose_bMidline', 'desc': 'PANOSE midline'},
  {'type': 'uint8', 'name': 'panose_bXHeight', 'desc': 'PANOSE XHeight'},
  {'type': 'uint32', 'name': 'ulUnicodeRange1', 'desc': 'unicode character range 1', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'ulUnicodeRange2', 'desc': 'unicode character range 2', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'ulUnicodeRange3', 'desc': 'unicode character range 3', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'ulUnicodeRange4', 'desc': 'unicode character range 4', 'disp': 'b32'},
  {'type': 'Tag', 'name': 'achVendID', 'desc': 'font verndor identification', 'disp': 's4'},
  {'type': 'uint16', 'name': 'fsSelection', 'desc': 'font selection flags', 'disp': 'b16'},
  {'type': 'uint16', 'name': 'usFirstCharIndex', 'desc': 'minimum unicode index'},
  {'type': 'uint16', 'name': 'usLastCharIndex', 'desc': 'maximum unicode index'},
  {'type': 'int16', 'name': 'sTypoAscender', 'desc': 'typographic ascender'},
  {'type': 'int16', 'name': 'sTypoDescender', 'desc': 'typographic descender'},
  {'type': 'int16', 'name': 'sTypoLineGap', 'desc': 'typographic line gap'},
  {'type': 'uint16', 'name': 'usWinAscent', 'desc': 'windows ascender'},
  {'type': 'uint16', 'name': 'usWinDescent', 'desc': 'windows descender'},
]
TABLE_OS2_1 = [
  {'type': 'uint32', 'name': 'ulCodePageRange1', 'desc': 'code page character range 1', 'disp': 'b32'},
  {'type': 'uint32', 'name': 'ulCodePageRange2', 'desc': 'code page character range 2', 'disp': 'b32'},
]
TABLE_OS2_4 = [
  {'type': 'int16', 'name': 'sxHeight', 'desc': 'so called x-Height'},
  {'type': 'int16', 'name': 'sCapHeight', 'desc': 'so called cap height'},
  {'type': 'uint16', 'name': 'usDefaultChar', 'desc': 'codepoint for default glyph'},
  {'type': 'uint16', 'name': 'usBreakChar', 'desc': 'codepoint for default break char'},
  {'type': 'uint16', 'name': 'usMaxContent', 'desc': 'max length of composition'},
]
TABLE_OS2_5 = [
  {'type': 'uint16', 'name': 'usLowerOpticalPointSize', 'desc': 'lower size of design'},
  {'type': 'uint16', 'name': 'usUpperOpticalPointSize', 'desc': 'upper size of design'},
]

TABLE_OS2_BIT_FSTYPE = [
  'permissions (no flag)',
  'permissions, restricted license embedding',
  'permissions, preview and print embedding',
  'permissions, editable embedding',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'No subsetting',
  'Bitmap embedding only',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
  'reserved',
]
TABLE_OS2_BIT_UNICODERANGE1 = [
  'Basic Latin',
  'Latin-1 Supplement',
  'Latin Extended-A',
  'Latin Extended-B',
  'IPA Extensions',
  'Spacing Modifier Letters',
  'Combining Diacritical Marks',
  'Greek and Coptic',
  'Coptic',
  'Cyrillic',
  'Armenian',
  'Hebrew',
  'Vai',
  'Arabic',
  'NKo',
  'Devanagari',
  'Bengali',
  'Gurmukhi',
  'Gujarati',
  'Oriya',
  'Tamil',
  'Telugu',
  'Kannada',
  'Malayalam',
  'Thai',
  'Lao',
  'Georgian',
  'Balinese',
  'Hangul Jamo',
  'Latin Extended Additional',
  'Greek Extended',
  'General Punctuation',
]



