# テスト第1弾

* 全体的な状態を調べるために、Windows上でFirefoxとChromeを利用し、インストールしていたPDFプリンタドライバを利用して生成したPDFについて調査する
* サンプルhtmlの文字列
  * ベーシックな文字としてひらがな・カタカナ
  * 要検証の対象として、康煕部⾸とCJK部首補助の2領域
* コマンドラインで`pdftotext`と`pdffonts`でPDFファイルの解析結果を取得、またPDFビューアーで文字列をコピペしたらどうなるかを調べる
  * ブラウザ内蔵のPDFビューアーは利用しない (ChromeでｈFoxitのPDFiumベース、FirefoxではPDF.jsベース)

## サンプルhtmlと作成されたPDF

### 康煕部⾸と通常の文字両方含む文書

* [サンプルhtml](sample.html)をブラウザ(Windows上)で表示し、印刷から各種ツール経由でPDFにする
* PDFをリーダーで開いてコピペで文字を抽出したもの、pdftotextでテキストデータにしたものを作成

| browser | Adobe PDF | Microsoft print | PrimoPDF | PDFへ保存 |
|---------|-----------|-----------------|----------|----------|
| chrome | [PDF](20260609-chrome-adobepdf.pdf) / [text](20260609-chrome-adobepdf.txt) | [PDF](20260609-chrome-msprint.pdf) / [text](20260609-chrome-msprint.txt) | [PDF](20260609-chrome-primo.pdf) / [text](20260609-chrome-primo.txt) | [PDF](20260609-chrome-savetopdf.pdf) / [text](20260609-chrome-savetopdf.txt) |
| firefox | [PDF](20260609-firefox-adobepdf.pdf) / [text](20260609-firefox-adobepdf.txt) | [PDF](20260609-firefox-msprint.pdf) / [text](20260609-firefox-msprint.txt) | [PDF](20260609-firefox-primo.pdf) / [text](20260609-firefox-primo.txt) | [PDF](20260609-firefox-savetopdf.pdf) / [text](20260609-firefox-savetopdf.txt) |

### 通常の文字だけの文章

* [サンプル2](sample-ja.html)を利用する、基本的にCJK統合漢字の範囲内の文字のみ

| browser | Adobe PDF | Microsoft print | PrimoPDF | PDFへ保存 |
|---------|-----------|-----------------|----------|----------|
| chrome | [PDF](20260609b-chrome-adobepdf.pdf) / [text](20260609-chromeb-adobepdf.txt) | [PDF](20260609b-chrome-msprint.pdf) / [text](20260609b-chrome-msprint.txt) | [PDF](20260609b-chrome-primo.pdf) / [text](20260609b-chrome-primo.txt) | [PDF](20260609b-chrome-savetopdf.pdf) / [text](20260609b-chrome-savetopdf.txt) |
| firefox | [PDF](20260609b-firefox-adobepdf.pdf) / [text](20260609b-firefox-adobepdf.txt) | [PDF](20260609b-firefox-msprint.pdf) / [text](20260609b-firefox-msprint.txt) | [PDF](20260609b-firefox-primo.pdf) / [text](20260609b-firefox-primo.txt) | [PDF](20260609b-firefox-savetopdf.pdf) / [text](20260609b-firefox-savetopdf.txt) |

## 結果


### サンプル1

#### 埋め込みフォント一覧

* chrome msprintはpdffontsで見れるフォントがなかった

| browser | print | name                               |  type            |  encoding      |   emb | sub | uni | object | ID |
|---------|-------|------------------------------------|------------------|----------------|-------|-----|-----|--------|----|
| chrome | adobe | T1                                  | Type 3           | Custom         |  yes | no | no  |    65 | 0 |
| chrome | primo | `[none]`                              | Type 3         |   Custom      |     yes | no | no    |  18  | 0 |
| chrome | savetopdf | AAAAAA+Noto-Sans-JP-Bold   (など多数)        |   Type 3         |   Custom      |     yes | yes | yes |     4 | 0 |
| firefox | adobe | AKEFEL+YuMincho-Regular            |  CID TrueType   |   Identity-H   |    yes | yes | yes  |   35 | 0 |
| firefox | msprint | CIDFont+F3                         |  CID TrueType    |  Identity-H    |   yes | no | yes  |   27 | 0 |
| firefox | primo | UJQUKG+游明朝-WinCharSetFFFF-H    |   CID TrueType    |  Identity-H    |   yes | yes | yes  |   17 | 0 |
| firefox | savetopdf 1 | TVXKTP+YuMincho-Regular          |    TrueType        |  WinAnsi       |   yes | yes | yes  |   11 | 0 |
| firefox | savetopdf 2 | FDFDID+YuMincho-Regular           |   CID TrueType     | Identity-H     |  yes | yes | yes   |  12 | 0 |


* chromeのPDFへ保存以外はタイトルなどのヘッダ・フッタ部分のデータのみしか保存されていない
* chromeのPDFへ保存ではすべての文字が正常に復元されていた


#### 康煕部⾸に似た漢字のコピペ

* chrome savetopdf : ⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⺐⼫屮⼭⼮⼯⼰⼱⼲⺓⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⻑⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉黒⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕
* firefox adobe : ⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⺐⼫⼬⼭⼮⼯⼰⼱⼲⺓⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⻑⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⻤⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕
* firefox msprint : ⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘卩⼚⼛⼜⼝⼞⼟⼠夂⼢⼣⼤⼥⼦⼧寸⼩⺐⼫⼬⼭巛⼯⼰⼱⼲⺓⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇曰⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧癶⽩⽪皿目⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶糸缶⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒角⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⻑門⾩⾪⾫⾬⾭非⾯⾰⾱⾲⾳⾴風⾶⾷⾸⾹⾺骨⾼⾽⾾⾿⿀⻤⿂⿃鹵⿅⿆⿇⿈⿉⿊⿋黽⿍⿎⿏⿐⿑⿒龍⿔⿕
* firefox primo : ⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘卩⼚⼛⼜⼝⼞⼟⼠夂⼢⼣⼤⼥⼦⼧寸⼩⺐⼫⼬⼭巛⼯⼰⼱⼲⺓⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇曰⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧癶⽩⽪皿目⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶糸缶⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒角⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⻑門⾩⾪⾫⾬⾭非⾯⾰⾱⾲⾳⾴風⾶⾷⾸⾹⾺骨⾼⾽⾾⾿⿀⻤⿂⿃鹵⿅⿆⿇⿈⿉⿊⿋黽⿍⿎⿏⿐⿑⿒龍⿔⿕
* firefox savetopdf : ⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘卩⼚⼛⼜⼝⼞⼟⼠夂⼢⼣⼤⼥⼦⼧寸⼩⺐⼫⼬⼭巛⼯⼰⼱⼲⺓⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇曰⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧癶⽩⽪皿目⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶糸缶⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒角⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⻑門⾩⾪⾫⾬⾭非⾯⾰⾱⾲⾳⾴風⾶⾷⾸⾹⾺骨⾼⾽⾾⾿⿀⻤⿂⿃鹵⿅⿆⿇⿈⿉⿊⿋黽⿍⿎⿏⿐⿑⿒龍⿔⿕

### サンプル2 (20260609b)

#### 埋め込みフォント一覧

| browser | print | name                               |  type            |  encoding      |   emb | sub | uni | object | ID |
|---------|-------|------------------------------------|------------------|----------------|-------|-----|-----|--------|----|
| chrome | savetopdf | BAAAAA+Noto-Sans-JP               |   Type 3      |      Custom       |    yes | yes | yes |     12 | 0 |
| firefox | adobe | BNIEBO+Meiryo                      |  CID TrueType    |  Identity-H    |   yes | yes | yes |     29 |  0 |
| firefox | msprint | CIDFont+F1                        |   CID TrueType   |   Identity-H    |   yes | no | yes |    11 | 0 |
| firefox | primo | IMTNSZ+游明朝-WinCharSetFFFF-H   |  CID TrueType    |  Identity-H     |  yes | yes | yes  |   13 | 0 |
| firefox | savetopdf 1 | PFALMZ+Meiryo               |         CID TrueType   |   Identity-H   |    yes | yes | yes |     9 | 0 |
| firefox | savetopdf 2 | GWXHTG+Meiryo               |         TrueType        |  WinAnsi       |   yes | yes | yes |    10 | 0 |

* Chromeからの印刷ではPDFへ保存のみテキスト抽出ができており、すべての文字が正常に復元されていた
* Firefoxからの印刷ではAdobe PDFのみすべての文字が康煕部⾸に変換されたが、それ以外の3ツールの出力は完全に同一になっており、一部の文字だけ正常に復元されている


## 考察

* 両方のサンプルについて通常の文字の領域についてもかなりの文字が康煕部⾸の文字コードで出力された
* ToUnicode CMapの抽出・復元の問題というよりは、フォント依存の処理の問題に見える
* ブラウザ上で表示している段階で、Firefox (Meiryo)ではU+2FCAとU+9ED2が同じ字形 (要検証ながら同じCIDのグリフ？)だが、Chrome (NotoSans)では異なる字形になっている
