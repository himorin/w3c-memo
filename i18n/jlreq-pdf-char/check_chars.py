#! /usr/bin/env python3

# use json file created by QPDF, like "qpdf --json --json-stream-data=inline PDF > JSON"

import sys
import json
import base64

def LoadJSON(pdf_json):
  try:
    fjson = open(pdf_json, 'r')
  except IOError as e:
    raise Exception("File '%s' open error: %s" % (pdf_json, e))
  try:
    site_config = json.load(fjson)
  except:
    raise Exception("json format parse error for '%s'" % (pdf_json))
  return site_config

def LoadOverview(c_dat):
  c_ov = {}
  c_trailer = c_dat["trailer"]
  c_ov['Info'] = c_trailer["value"]["/Info"]
  c_ov['Root'] = c_trailer["value"]["/Root"]
  c_obj = c_dat["obj:" + c_ov['Info']]["value"]
  for c_key in c_obj:
    if c_key.startswith("/"):
      c_ov['Root' + c_key[1:]] = c_obj[c_key]
  c_obj = c_dat["obj:" + c_ov['Root']]["value"]
  c_ov['Root-Pages'] = c_obj['/Pages']
  c_ov['Root-StructTreeRoot'] = c_obj['/StructTreeRoot']
  c_ov['Root-Pages-obj'] = c_dat["obj:" + c_ov['Root-Pages']]["value"]["/Kids"]
  return c_ov

def GetFontsForPage(c_dat, c_obj):
  return c_dat['obj:' + c_obj]['value']['/Resources']['/Font']

def GetFontOverview(c_dat, c_obj):
  c_font = c_dat['obj:' + c_obj]['value']
  c_ov = {}
  c_ov['Subtype'] = c_font['/Subtype']
  if '/ToUnicode' in c_font:
    c_ov['ToUnicode'] = c_font['/ToUnicode']
  if '/BaseFont' in c_font:
    c_ov['BaseFont'] = c_font['/BaseFont']
    c_ov['DescendantFonts'] = c_font['/DescendantFonts']
    c_ov['name'] = 'BaseFont ' + c_font['/BaseFont']
  else:
    c_ov['CIDToGIDMap'] = c_font['/CIDToGIDMap']
    c_ov['FontDescriptor'] = c_font['/FontDescriptor']
    c_ov['FirstChar'] = c_font['/FirstChar']
    c_ov['LastChar'] = c_font['/LastChar']
    c_ov['name'] = "CIDFont (%s - %s)" % (c_font['/FirstChar'], c_font['/LastChar'])
  if isinstance(c_font['/Encoding'], dict):
    c_ov['Encoding'] = c_font['/Encoding']['/Type']
    if '/Differences' in c_font['/Encoding']:
      c_ov['Encoding'] += "-Differences"
  else:
    c_ov['Encoding'] = c_font['/Encoding']
  return c_ov

def DecodeB64(b64str):
  return base64.b64decode(b64str).decode('utf-8')

def ListCharmaps(c_dat):
  c_cmaps = []
  c_save = 0
  for c_line in c_dat.splitlines():
    if ((c_save > 0) and (c_line != "endbfchar") and (c_line != "endbfrange")):
      c_cmaps.append(c_line)
      c_save -= 1
      continue
    if ((c_line == "endbfchar") or (c_line == "endbfrange")):
      c_save = 0
      continue
    c_linesep = c_line.split()
    if ((len(c_linesep) == 2) and (c_linesep[1] == "beginbfchar")):
      c_save = int(c_linesep[0])
    if ((len(c_linesep) == 2) and (c_linesep[1] == "beginbfrange")):
      c_save = int(c_linesep[0])
  return c_cmaps

if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise Exception("Invalid parameter: command <json_file>\n  Use json from \"qpdf --json --json-stream-data=inline PDF > JSON\"")
  c_dat = LoadJSON(sys.argv[1])
  c_pdf = c_dat['qpdf'][1]
  c_ov = LoadOverview(c_pdf)
  # print overview
  for c_key in c_ov:
    if (c_key != "Root-Pages-obj"):
      print("%s: %s" % (c_key, c_ov[c_key]))
  # print pages
  c_cnt = 0
  for c_pobj in c_ov['Root-Pages-obj']:
    c_cnt += 1
    c_fonts = GetFontsForPage(c_pdf, c_pobj)
    print("Page %s obj: %s" % (c_cnt, c_pobj))
    for c_fkey in c_fonts:
      c_fdat = GetFontOverview(c_pdf, c_fonts[c_fkey])
      print("  Font %s: %s (%s, %s)" % (c_fkey, c_fonts[c_fkey], c_fdat['Subtype'], c_fdat['name']))
      print("    Encoding: %s" % c_fdat['Encoding'])
      if 'ToUnicode' in c_fdat:
        print("    ToUnicode: %s" % c_fdat['ToUnicode'])
        c_tu = DecodeB64(c_pdf['obj:' + c_fdat['ToUnicode']]['stream']['data'])
        c_cmaps = ListCharmaps(c_tu)
        for c_cmap in c_cmaps:
          print("      - %s" % c_cmap)


