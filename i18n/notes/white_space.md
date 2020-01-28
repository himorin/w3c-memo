# HTMLにおける空白の扱いについて

## 関連項目

* [CSS Text Level 4](https://www.w3.org/TR/css-text-4/)
  * [Word Boundary](https://www.w3.org/TR/css-text-4/#word-boundaries) - zwsp (U+200B), wbr
  * [text-space-collapse etc.](https://www.w3.org/TR/css-text-4/#white-space-collapsing)
  * [text-spacing](https://www.w3.org/TR/css-text-4/#text-spacing-property)

## HTMLにおける文字のカテゴリと文字参照

### 文字カテゴリ

Unicodeへの参照以外にも、いくつかのカテゴリが定義されており置換(読み替え)で利用される。

* [ASCII tab or newline](https://infra.spec.whatwg.org/#ascii-tab-or-newline) : U+0009, U+000A, U+000D
* [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace) : U+0009, U+000A, U+000C, U+000D, U+0020

### 文字参照

空白関係で利用される文字参照のリスト、展開先のコードポイントとCSSプロパティーによる置換などをコメントで含めて。全リストは[Named character references](https://html.spec.whatwg.org/multipage/named-characters.html#entity-nbsp)にある。

* 1byte系
  * [nbsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-nbsp) (U+00A0)
  * [NonBreakingSpace](https://html.spec.whatwg.org/multipage/named-characters.html#entity-NonBreakingSpace) (U+00A0)
  * [NewLine](https://html.spec.whatwg.org/multipage/named-characters.html#entity-NewLine) (U+000A)
* U+20XX系
  * [ensp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-ensp) (U+2002)
  * [emsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-emsp) (U+2003)
  * [emsp13](https://html.spec.whatwg.org/multipage/named-characters.html#entity-emsp13) (U+2004)
  * [emsp14](https://html.spec.whatwg.org/multipage/named-characters.html#entity-emsp14) (U+2005)
  * [nvap](https://html.spec.whatwg.org/multipage/named-characters.html#entity-nvap) (U+2007)
  * [puncap](https://html.spec.whatwg.org/multipage/named-characters.html#entity-puncap) (U+2008)
  * [thinsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-thinsp) (U+2009)
  * [hairsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-hairsp) (U+200A)
  * [zwsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-ZeroWidthSpace) (U+200B)
  * [zwnj](https://html.spec.whatwg.org/multipage/named-characters.html#entity-zwnj) (U+200C)
  * [zwj](https://html.spec.whatwg.org/multipage/named-characters.html#entity-zwj) (U+200D)
  * [MediumSpace](https://html.spec.whatwg.org/multipage/named-characters.html#entity-MediumSpace) (U+205F)
  * [NoBreak](https://html.spec.whatwg.org/multipage/named-characters.html#entity-NoBreak) (U+2060)
  * [it](https://html.spec.whatwg.org/multipage/named-characters.html#entity-it) (U+2062)
    * [InvisibleTimes](https://html.spec.whatwg.org/multipage/named-characters.html#entity-InvisibleTimes)
  * [ic](https://html.spec.whatwg.org/multipage/named-characters.html#entity-ic) (U+2063)
    * [InvisibleComma](https://html.spec.whatwg.org/multipage/named-characters.html#entity-InvisibleComma)

### 置換

* [改行の正規化 (normalize newlines)](https://infra.spec.whatwg.org/#normalize-newlines) : U+000D U+000AをU+000Aに置換した後、すべてのU+000DをU+000Aに置換
* [空白の畳み込み (strip and collapse ASCII whitespace)](https://infra.spec.whatwg.org/#strip-and-collapse-ascii-whitespace) : 連続したASCII whitespaceのブロックのすべてを一つのU+0020に置き換え、文字列前後のASCII whitespaceを除去
