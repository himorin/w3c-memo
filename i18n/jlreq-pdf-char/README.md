# PDFでの康煕部⾸周りのテスト

## 康煕部⾸と通常の文字両方含む文書

* [サンプルhtml](sample.html)をブラウザ(Windows上)で表示し、印刷から各種ツール経由でPDFにする
* PDFをリーダーで開いてコピペで文字を抽出したもの、pdftotextでテキストデータにしたものを作成
* [結果](20260609-results.md): 通常の文字の領域についてもかなりの文字が康煕部⾸の文字コードで出力された

| browser | Adobe PDF | Microsoft print | PrimoPDF | PDFへ保存 |
|---------|-----------|-----------------|----------|----------|
| chrome | [PDF](20260609-chrome-adobepdf.pdf) / [text](20260609-chrome-adobepdf.txt) | [PDF](20260609-chrome-msprint.pdf) / [text](20260609-chrome-msprint.txt) | [PDF](20260609-chrome-primo.pdf) / [text](20260609-chrome-primo.txt) | [PDF](20260609-chrome-savetopdf.pdf) / [text](20260609-chrome-savetopdf.txt) |
| firefox | [PDF](20260609-firefox-adobepdf.pdf) / [text](20260609-firefox-adobepdf.txt) | [PDF](20260609-firefox-msprint.pdf) / [text](20260609-firefox-msprint.txt) | [PDF](20260609-firefox-primo.pdf) / [text](20260609-firefox-primo.txt) | [PDF](20260609-firefox-savetopdf.pdf) / [text](20260609-firefox-savetopdf.txt) |

## 通常の文字だけの文章

* [サンプル2](sample-ja.html)を利用する、基本的にCJK統合漢字の範囲内の文字のみ

