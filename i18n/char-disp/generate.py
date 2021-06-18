#! /usr/bin/env python3

import sys

LINE_LEN = 16

def genCharArray(fname):
    try:
        fp = open(fname, 'r', encoding='UTF-8')
    except IOError as e:
        raise Exception("File '{}' open error {}".format(fname, e))
    flines = fp.read().splitlines()
    fdat = []
    for fline in flines:
        fdat += list(fline)
    return fdat

def printSupport(fp, ccodes):
    for ic in ccodes:
        fp.write("<td class='desc'>\n")
        fp.write("<a href='https://util.unicode.org/UnicodeJsps/character.jsp?a={}' title='U+{}'>U+{}</a>\n".format(ic, ic, ic))
        fp.write("</td>\n")

def outputHTML(fname):
    try:
        fp = open(fname + '.html', 'x', encoding='UTF-8')
    except IOError as e:
        raise Exception("Cannot create file '{}.html': {}".format(fname, e))
    chars = genCharArray(fname)
    fp.write('''
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>MOCKUP - Character list</title>
  <style>
    .vhtgt { height: 2em; width: 2em; }
    table { border-collapse: collapse; }
    .sgnchar { font-size: 2em; border: 1px solid black; }
  </style>
  <script>
  function switchMode(tgt) {
    let elems = document.getElementsByClassName("vhtgt");
    for (var i = 0; i < elems.length; i++) {
      elems[i].style["writing-mode"] = tgt;
    }
  }
  </script>
</head>
<body>
<table border="1">
<tr>
            ''')
    cnum = -1
    ccodes = []
    for cchr in chars:
        if cchr == ' ':
            continue
        cnum += 1
        if cnum == LINE_LEN:
            cnum = 0
            fp.write('</tr><tr>')
            printSupport(fp, ccodes)
            fp.write('</tr><tr>')
            ccodes = []
        code = format(ord(cchr), 'x')
        ccodes.append(code)
        fp.write("<td class='vhtgt'><span class='vhtgt sgnchar' id='char-{}'>&#x{};</span></td>".format(code, code))
    fp.write('</tr><tr>')
    printSupport(fp, ccodes)
    fp.write('''
</tr>
</table>
<p>
<label><input checked type="radio" name="wm" onclick="switchMode(\'horizontal-tb\');">Horizontal</label>
<br>
<label><input type="radio" name="wm" onclick="switchMode(\'vertical-rl\');">Vertical</label>
<br>
</p>
</body>
</html>
            ''')
    fp.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Usage: <script> <target file>")
    outputHTML(sys.argv[1])


