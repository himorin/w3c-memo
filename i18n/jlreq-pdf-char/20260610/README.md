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


### pdftotextの出力

* FirefoxのNoto Sans JPは文字抽出ができなかった
* 比較用2文字のグリフが異なったのは、ChromeのBIZ UDPGothicとNoto Sans JP、FirefoxのNoto Sans JPの3つ
* Chrome
  * all, limitとも、すべての康煕部首に似た文字はCJK Ideographのコードポイントになっていた、逆も同様
  * Noto Sans JP以外ではpdftotextの出力結果で文字の並び順がずれていたりという事象が発生している（抜けがあるかどうかの詳細までは未検証）
* Firefox
  * 文字の並び順などはすべて問題なかった（一部改行位置が異なったことがあるがプロポーショナルなどの問題もある可能性）
  * CJK Ideographの領域で康煕部首になっていた文字 (all, limitの双方で差異はなし)
    * M Plus: ⼹ (U+2F39)、⾭ (U+2FAD)、⿈ (U+2FC8)
    * LINE: ⼹ (U+2F39)、⽧ (U+2F67)、⽱ (U+2F71)、⾡ (U+2FA1)、⿈ (U+2FC8)
    * Biz UDP: ⼹ (U+2F39)
  * BIZ UDP (all)では康煕部首の領域の文字がほかのものになっていた例が出た
    * CJK Ideographになっていた文字: 卩 (U+5369)、夂 (U+5902)、寸 (U+5BF8)、巛 (U+5DDB)、曰 (U+66F0)、癶 (U+7676)、皿 (U+76BF)、目 (U+76EE)、糸 (U+7CF8)、缶 (U+7F36)、角 (U+89D2)、門 (U+9580)、非 (U+975E)、風 (U+98A8)、骨 (U+9AA8)、鹵 (U+9E75)、黽 (U+9EFD)、龍 (U+9F8D)
    * CJK Radicalになっていた文字: ⺐ (U+2E90)、⺓ (U+2E93)、⻑ (U+2ED1)、⻤ (U+2EE4)


## 考察

* Chromeで読み込むフォントが違っても結果が同じになったのはToUnicode CMapsを生成する際の元データが同じことが原因ではないかとも推察される
  * ブラウザのデフォルトフォントのデータを利用している可能性？: 他のPDF印刷ドライバを試す、デフォルトフォントを変更して試す、など
* FirefoxのBIZ UDPで逆向きの置換が出た点について、PDFから文字をコピペして調査しても同様の結果が得られたのでpdftotext依存の問題ではない
  * Firefoxの結果を見る限りは、ToUnicode CMaps経由で漢字が康煕部首に置換されてしまうのは、フォントが持つ情報起因であることが推察される


# 試験第2弾 - 追加

Chromeでブラウザのデフォルトフォントを切り替えて結果がどうなるかを試してみる。
PDFファイルの作成はallの4フォント向けファイルを利用、PDFファイルを生成する際にはChromeの設定からフォントの標準・Serif・Sans Serifの3つを変更し再起動してからPDFを生成する。

## 結果

| 既定フォント | Chrome NotoSans | Chrome M Plus | Chrome LINE | Chrome BIZ UDP |
|---|---|---|---|---|
| A-OTF UD Reimin Pr6N | [PDF](font-chrome-aotf-noto.pdf) [extract](font-chrome-aotf-noto.txt) | [pdf](font-chrome-aotf-mplus.pdf) [extract](font-chrome-aotf-mplus.txt) | [pdf](font-chrome-aotf-line.pdf) [extract](font-chrome-aotf-line.txt) | [pdf](font-chrome-aotf-bizud.pdf) [extract](font-chrome-aotf-bizud.txt) |
| Ahem | [PDF](font-chrome-ahem-noto.pdf) [extract](font-chrome-ahem-noto.txt) | [pdf](font-chrome-ahem-mplus.pdf) [extract](font-chrome-ahem-mplus.txt) | [pdf](font-chrome-ahem-line.pdf) [extract](font-chrome-ahem-line.txt) | [pdf](font-chrome-ahem-bizud.pdf) [extract](font-chrome-ahem-bizud.txt) |
| BIZ UDPGothic | [PDF](font-chrome-bizud-noto.pdf) [extract](font-chrome-bizud-noto.txt) | [pdf](font-chrome-bizud-mplus.pdf) [extract](font-chrome-bizud-mplus.txt) | [pdf](font-chrome-bizud-line.pdf) [extract](font-chrome-bizud-line.txt) | [pdf](font-chrome-bizud-bizud.pdf) [extract](font-chrome-bizud-bizud.txt) |
| FOT UDMincho Pr6N | [PDF](font-chrome-fot-noto.pdf) [extract](font-chrome-fot-noto.txt) | [pdf](font-chrome-fot-mplus.pdf) [extract](font-chrome-fot-mplus.txt) | [pdf](font-chrome-fot-line.pdf) [extract](font-chrome-fot-line.txt) | [pdf](font-chrome-fot-bizud.pdf) [extract](font-chrome-fot-bizud.txt) |
| MS Gochic | [PDF](font-chrome-msg-noto.pdf) [extract](font-chrome-msg-noto.txt) | [pdf](font-chrome-msg-mplus.pdf) [extract](font-chrome-msg-mplus.txt) | [pdf](font-chrome-msg-line.pdf) [extract](font-chrome-msg-line.txt) | [pdf](font-chrome-msg-bizud.pdf) [extract](font-chrome-msg-bizud.txt) |
| Meiryo | [PDF](font-chrome-meiryo-noto.pdf) [extract](font-chrome-meiryo-noto.txt) | [pdf](font-chrome-meiryo-mplus.pdf) [extract](font-chrome-meiryo-mplus.txt) | [pdf](font-chrome-meiryo-line.pdf) [extract](font-chrome-meiryo-line.txt) | [pdf](font-chrome-meiryo-bizud.pdf) [extract](font-chrome-meiryo-bizud.txt) |
| Yu Gochic | [PDF](font-chrome-yug-noto.pdf) [extract](font-chrome-yug-noto.txt) | [pdf](font-chrome-yug-mplus.pdf) [extract](font-chrome-yug-mplus.txt) | [pdf](font-chrome-yug-line.pdf) [extract](font-chrome-yug-line.txt) | [pdf](font-chrome-yug-bizud.pdf) [extract](font-chrome-yug-bizud.txt) |

* "Chrome NotoSans", "M Plus", "LINE"の行、NotoSansのWeb Fontを指定したhtmlから生成されたPDFは、pdftotextの結果は完全一致、康煕部首についてすべて問題なかった
* "Chrome BIZ UDP"の行に対し、A-OTF, Ahem, BIZ UDMinchoにおいて、康煕部首の彐 (U+5F50)のみCJK Ideographに置き換わっていた（それ以外はすべて問題なし）

## 考察

* 設定の、"デザイン" -> "フォントをカスタマイズ"の画面において、Ahemを指定した時、サンプルテキストはひらがな・カタカナ・漢字が正常に表示されているので何らかのフォールバックがありそう
* BIZ UDPでFirefoxでCJK Ideographが康煕部首になっていた文字と同じセット（単一文字ながら）に影響が起こっていたので、何らかの既定フォントの影響はある？

## 追加

* WebFontを入れないで既定のフォントを変更するのをやっていないので追加する
* ファイル
  * A-OTF UD Reimin Pr6N: [PDF](font-chrome-aotf-def.pdf) [extract](font-chrome-aotf-def.txt)
  * Ahem:  [PDF](font-chrome-ahem-def.pdf) [extract](font-chrome-ahem-def.txt)
  * BIZ UDPGothic:  [PDF](font-chrome-bizud-def.pdf) [extract](font-chrome-bizud-def.txt)
  * FOT UDMincho Pr6N:  [PDF](font-chrome-fot-def.pdf) [extract](font-chrome-fot-def.txt)
  * MS Gochic:  [PDF](font-chrome-msg-def.pdf) [extract](font-chrome-msg-def.txt)
  * Meiryo:  [PDF](font-chrome-meiryo-def.pdf) [extract](font-chrome-meiryo-def.txt)
  * Yu Gochic:  [PDF](font-chrome-yug-def.pdf) [extract](font-chrome-yug-def.txt)
* Ahemを指定した際、表示にはNoto Sans JPがRenderingでリストされていた
