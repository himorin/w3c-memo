# 試験第2弾

## サンプルファイル

### Web Fontsターゲットリスト

* [Noto Sans JP](https://fonts.google.com/noto/specimen/Noto+Sans+JP)
* [M Plus 1P](https://fonts.google.com/specimen/M+PLUS+1p)
* [LINE Seed JP](https://fonts.google.com/specimen/LINE+Seed+JP)
* [BIZ UDPGothic](https://fonts.google.com/specimen/BIZ+UDPGothic)

### ファイルと生成したPDF

* PDF生成はChromeとFirefoxでそれぞれ内蔵のPDFへ保存を利用することとした
* ベースファイル
  * all: [比較対象文字両方を含むもの](sample-base-all.html) (こちらのファイルはグリフの差を比較する部分を追加した)
  * limit: [CJK統合漢字の領域内だけにしたもの](saple-base-limit.html)


| フォント | HTML all | HTML limit | Chrome all | Chrome limit | Firefox all | Firefox limit |
|---|---|---|---|---|---|---|
| Noto Sans JP | [all](sample-noto-all.html) | [limit](sample-noto-limit.html) | [pdf](chrome-noto-all.pdf) [extract](chrome-noto-all.txt) | [pdf](chrome-noto-limit.pdf) [extract](chrome-noto-limit.txt) | [pdf](firefox-noto-all.pdf) [extract](firefox-noto-all.txt) | [pdf](firefox-noto-limit.pdf) [extract](firefox-noto-limit.txt) |
| M Plus 1P | [all](sample-mplus-all.html) | [limit](sample-mplus-limit.html) | [pdf](chrome-mplus-all.pdf) [extract](chrome-mplus-all.txt) | [pdf](chrome-mplus-limit.pdf) [extract](chrome-mplus-limit.txt) | [pdf](firefox-mplus-all.pdf) [extract](firefox-mplus-all.txt) | [pdf](firefox-mplus-limit.pdf) [extract](firefox-mplus-limit.txt) |
| LINE Seed JP | [all](sample-line-all.html) | [limit](sample-line-limit.html) | [pdf](chrome-line-all.pdf) [extract](chrome-line-all.txt) | [pdf](chrome-line-limit.pdf) [extract](chrome-line-limit.txt) | [pdf](firefox-line-all.pdf) [extract](firefox-line-all.txt) | [pdf](firefox-line-limit.pdf) [extract](firefox-line-limit.txt) |
| BIZ UDPGothic | [all](sample-bizud-all.html) | [limit](sample-bizud-limit.html) | [pdf](chrome-bizud-all.pdf) [extract](chrome-bizud-all.txt) | [pdf](chrome-bizud-limit.pdf) [extract](chrome-bizud-limit.txt) | [pdf](firefox-bizud-all.pdf) [extract](firefox-bizud-all.txt) | [pdf](firefox-bizud-limit.pdf) [extract](firefox-bizud-limit.txt) |

#### pdffontsの出力

* Web Fontsでのスライシングのために複数フォントに分かれているものは集約している
  * allとlmitで変化はほとんどなし(スライス分の数が違う程度)
* ChromeでNoto Sans JP、FirefoxでMeiryoのそれぞれが(双方ともブラウザデフォルトの設定)も併用されていた
* FirefoxでNoto Sans JPを利用したPDFファイルは情報がなかった

| フォント | ブラウザ | name                                | type             | encoding        | emb | sub | uni | object | ID |
|---|---|---|---|---|---|---|---|---|---|
| BIZ UDP | Chrome | AAAAAA+BIZUDPGothic-Regular        |  CID TrueType     | Identity-H     |  yes | yes | yes  |    4 | 0 |
| BIZ UDP | Chrome (2) | OAAAAA+Noto-Sans-JP             |     Type 3       |     Custom      |     yes | yes | yes  |   19 | 0 |
| LINE Seed JP | Chrome | AAAAAA+LINESeedJP-Regular      |      CID TrueType  |    Identity-H   |    yes | yes | yes  |    4 | 0 |
| LINE Seed JP | Chrome (2) |KBAAAA+Noto-Sans-JP          |        Type 3      |      Custom     |      yes | yes | yes  |   41 |  0 |
| M Plus 1P | Chrome | AAAAAA+MPLUS1p-Regular            |   CID TrueType    |  Identity-H      | yes | yes | yes   |   4 | 0 |
| M Plus 1P | Chrome (2) | KBAAAA+Noto-Sans-JP           |       Type 3        |    Custom       |    yes | yes | yes  |   41 | 0 |
| Noto Sans JP | Chrome | AAAAAA+Noto-Sans-JP-Thin       |      Type 3        |    Custom        |   yes | yes | yes  |    4 | 0 |
| BIZ UDP | Firefox | RAXXRY+BIZUDPGothic-Regular        |  TrueType         |  WinAnsi         | yes | yes | yes     |  7 | 0 |
| BIZ UDP | Firefox (2) | ZPLGZP+BIZUDPGothic-Regular     |     CID TrueType  |    Identity-H      | yes | yes | yes     |  8 | 0 |
| BIZ UDP | Firefox (3) | ZWWJFQ+Meiryo                    |    CID TrueType   |   Identity-H      | yes | yes | yes     | 22 | 0 |
| LINE Seed JP | Firefox | HLFUBE+LINESeedJP-Regular       |     TrueType        |  WinAnsi         | yes | yes | yes     |  7 | 0 |
| LINE Seed JP | Firefox (2) | BHCLHL+LINESeedJP-Regular    |        CID TrueType |     Identity-H      | yes | yes | yes     |  8 | 0 |
| LINE Seed JP | Firefox (3) | SFEESR+Meiryo                 |       CID TrueType  |    Identity-H      | yes | yes | yes     | 44 | 0 |
| M Plus 1P | Firefox | YCVUMT+MPLUS1p-Regular             |  TrueType         | WinAnsi         | yes | yes | yes     |  7 | 0 |
| M Plus 1P | Firefox (2) | YHAOMV+MPLUS1p-Regular          |     CID TrueType  |    Identity-H      | yes | yes | yes     |  8 | 0 |
| M Plus 1P | Firefox (3) | QNFJIJ+Meiryo                    |    CID TrueType   |   Identity-H      | yes | yes | yes     | 44 | 0 |


### 結果

* FirefoxのNoto Sans JPは文字抽出ができなかった
* 比較用2文字のグリフが異なったのは、ChromeのBIZ UDPGothicとNoto Sans JP、FirefoxのNoto Sans JPの3つ