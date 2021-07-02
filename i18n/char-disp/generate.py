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
    table { border-collapse: collapse; }
    tr.disp { height: 4em; }
    .sgnchar { font-size: 2rem; line-height: 2rem; margin: 0.5rem; border: 1px solid black; display: inline-block; }
  </style>
  <script>
  function switchMode(tgt) {
    let elems = document.getElementsByClassName("vhtgt");
    for (var i = 0; i < elems.length; i++) {
      elems[i].style["writing-mode"] = tgt;
    }
  }
  function switchFont() {
    let tgt = document.getElementById('fontname').value;
    let elems = document.getElementsByClassName("vhtgt");
    for (var i = 0; i < elems.length; i++) {
      elems[i].style["font-family"] = tgt;
    }
  }
  </script>
</head>
<body>
<p>
<label><input checked type="radio" name="wm" onclick="switchMode(\'horizontal-tb\');">Horizontal</label>
<br>
<label><input type="radio" name="wm" onclick="switchMode(\'vertical-rl\');">Vertical</label>
<br>
<p>Font: <input type="text" name="fontname" id="fontname" list="fontlist" onchange="switchFont()"> (Double click to select)</p>
<datalist id="fontlist">
  <option value="游ゴシック">
  <option value="游明朝">
  <option value="ヒラギノ">
  <option value="メイリオ">
  <option value="Times New Roman">
  <option value="Arial">
  <option value="serif">
  <option value="sans-serif">
  <option value="monospace">
  <option value="rounded">
  <option value="system-ui">
</datalist>
</p>
<table border="1">
<tr class="disp">
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
            fp.write('</tr><tr class="disp">')
            ccodes = []
        code = format(ord(cchr), 'x')
        ccodes.append(code)
        fp.write("<td class='vhtgt'><span class='vhtgt sgnchar' id='char-{}'>&#x{};</span></td>".format(code, code))
    fp.write('</tr><tr>')
    printSupport(fp, ccodes)
    fp.write('''
</tr>
</table>
</body>
</html>
            ''')
    fp.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Usage: <script> <target file>")
    outputHTML(sys.argv[1])


