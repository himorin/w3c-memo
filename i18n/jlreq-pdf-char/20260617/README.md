# 試験第3弾

QPDFが出力するjsonをパースするスクリプト([check_chars.py](../check_chars.py))ができたのでそちらでToUnicodeを参照する。

## データ

* Web Fontsは入っていない、ブラウザの設定はFirefoxはメイリオでChromeはNotoである
* 以下、`C&P`はPDFをPDF-XChangeで表示して文字ボックスをコピペしたもの
* Firefoxから出力のQPDF JSONの構造は未対応

| ソース | Chrome PDFを保存 | Firefox PDFを保存 |
|---|---|---|
| [sample.html](../20260609/sample.html) | [PDF](chrome-all-noto.pdf) [QPDF json](chrome-all-noto.json) [QPDF 解析](chrome-all-noto.out) [C&P](chrome-all-noto-cp.txt) [pdftotext](chrome-all-noto-pdftotext.txt) | [PDF](firefox-all-meiryo.pdf) [QPDF json](firefox-all-meiryo.json) QPDF 解析 [C&P](firefox-all-meiryo-cp.txt) [pdftotext](firefox-all-meiryo-pdftotext.txt) |
| [sample-ja.html](../20260609/sample-ja.html) | [PDF](chrome-limit-noto.pdf) [QPDF json](chrome-limit-noto.json) [QPDF 解析](chrome-limit-noto.out) [C&P](chrome-limit-noto-cp.txt) [pdftotext](chrome-limit-noto-pdftotext.txt) | [PDF](firefox-limit-meiryo.pdf) [QPDF json](firefox-limit-meiryo.json) QPDF 解析 [C&P](firefox-limit-meiryo-cp.txt) [pdftotext](firefox-limit-meiryo-pdftotext.txt) |

