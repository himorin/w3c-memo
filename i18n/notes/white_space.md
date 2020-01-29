# HTMLにおける空白の扱いについて

## 関連項目

* [CSS Text Level 3](https://www.w3.org/TR/css-text-3/)
* [CSS Text Level 4](https://www.w3.org/TR/css-text-4/)
  * [Word Boundary](https://www.w3.org/TR/css-text-4/#word-boundaries) - zwsp (U+200B), wbr
  * [text-space-collapse etc.](https://www.w3.org/TR/css-text-4/#white-space-collapsing)
  * [text-spacing](https://www.w3.org/TR/css-text-4/#text-spacing-property)
* [CSS Text Decoration Module Level 3](https://www.w3.org/TR/css-text-decor-3/)

### Unicodeの仕様

* [UAX #11](https://www.unicode.org/reports/tr11/tr11-36.html): East Asian Width (Fullwidth/F, Halfwidth/H, Wide/W, Narrow/Na, Ambiguous/A, Neutral) の定義
* [UAX #29](http://www.unicode.org/reports/tr29/) : Grapheme cluster (Vowelや合字などのひとまとまりとして表示される組)、単語、文章の区切りを判別するためのUnicode属性の規定
* [UAX #44](https://www.unicode.org/reports/tr44/tr44-24.html) : Unicode character database (UCD)の定義で文字に付随する属性(たとえば[General_Category](https://www.unicode.org/reports/tr44/tr44-24.html#GC_Values_Table))を規定

## HTMLにおける文字のカテゴリと文字参照

Unicode code pointからのリンクは[Unicode utilities, character properties](https://unicode.org/cldr/utility/character.jsp)の該当文字のページ。

### 文字カテゴリ

Unicodeへの参照以外にも、いくつかのカテゴリが定義されており置換(読み替え)で利用される。

* [ASCII tab or newline](https://infra.spec.whatwg.org/#ascii-tab-or-newline) : [U+0009](https://unicode.org/cldr/utility/character.jsp?a=0009), [U+000A](https://unicode.org/cldr/utility/character.jsp?a=000A), [U+000D](https://unicode.org/cldr/utility/character.jsp?a=000D)
* [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace) :  [U+0009](https://unicode.org/cldr/utility/character.jsp?a=0009), [U+000A](https://unicode.org/cldr/utility/character.jsp?a=000A), [U+000C](https://unicode.org/cldr/utility/character.jsp?a=000C), [U+000D](https://unicode.org/cldr/utility/character.jsp?a=000D), [U+0020](https://unicode.org/cldr/utility/character.jsp?a=0020)

### 文字参照

空白関係で利用される文字参照のリスト、展開先のコードポイントとCSSプロパティーによる置換などをコメントで含めて。全リストは[Named character references](https://html.spec.whatwg.org/multipage/named-characters.html#entity-nbsp)にある。文字参照名に貼ってあるリンクはこのリストのページ内の該当業へのリンク。

* 1byte系
  * [NewLine](https://html.spec.whatwg.org/multipage/named-characters.html#entity-NewLine) ([U+000A](https://unicode.org/cldr/utility/character.jsp?a=000A))
  * [nbsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-nbsp) ([U+00A0](https://unicode.org/cldr/utility/character.jsp?a=00A0))
    * [NonBreakingSpace](https://html.spec.whatwg.org/multipage/named-characters.html#entity-NonBreakingSpace)
* U+20XX系
  * [ensp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-ensp) ([U+2002](https://unicode.org/cldr/utility/character.jsp?a=2002))
  * [emsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-emsp) ([U+2003](https://unicode.org/cldr/utility/character.jsp?a=2003))
  * [emsp13](https://html.spec.whatwg.org/multipage/named-characters.html#entity-emsp13) ([U+2004](https://unicode.org/cldr/utility/character.jsp?a=2004))
  * [emsp14](https://html.spec.whatwg.org/multipage/named-characters.html#entity-emsp14) ([U+2005](https://unicode.org/cldr/utility/character.jsp?a=2005))
  * [nvap](https://html.spec.whatwg.org/multipage/named-characters.html#entity-nvap) ([U+2007](https://unicode.org/cldr/utility/character.jsp?a=2007))
  * [puncap](https://html.spec.whatwg.org/multipage/named-characters.html#entity-puncap) ([U+2008](https://unicode.org/cldr/utility/character.jsp?a=2008))
  * [thinsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-thinsp) ([U+2009](https://unicode.org/cldr/utility/character.jsp?a=2009))
  * [hairsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-hairsp) ([U+200A](https://unicode.org/cldr/utility/character.jsp?a=200A))
  * [zwsp](https://html.spec.whatwg.org/multipage/named-characters.html#entity-ZeroWidthSpace) ([U+200B](https://unicode.org/cldr/utility/character.jsp?a=200B))
  * [zwnj](https://html.spec.whatwg.org/multipage/named-characters.html#entity-zwnj) ([U+200C](https://unicode.org/cldr/utility/character.jsp?a=200C))
  * [zwj](https://html.spec.whatwg.org/multipage/named-characters.html#entity-zwj) ([U+200D](https://unicode.org/cldr/utility/character.jsp?a=200D))
  * [MediumSpace](https://html.spec.whatwg.org/multipage/named-characters.html#entity-MediumSpace) ([U+205F](https://unicode.org/cldr/utility/character.jsp?a=205F)
  * [NoBreak](https://html.spec.whatwg.org/multipage/named-characters.html#entity-NoBreak) ([U+2060](https://unicode.org/cldr/utility/character.jsp?a=2060))
  * [it](https://html.spec.whatwg.org/multipage/named-characters.html#entity-it) ([U+2062](https://unicode.org/cldr/utility/character.jsp?a=2062))
    * [InvisibleTimes](https://html.spec.whatwg.org/multipage/named-characters.html#entity-InvisibleTimes)
  * [ic](https://html.spec.whatwg.org/multipage/named-characters.html#entity-ic) ([U+2063](https://unicode.org/cldr/utility/character.jsp?a=2063))
    * [InvisibleComma](https://html.spec.whatwg.org/multipage/named-characters.html#entity-InvisibleComma)

### 置換

* [改行の正規化 (normalize newlines)](https://infra.spec.whatwg.org/#normalize-newlines) : U+000D U+000AをU+000Aに置換した後、すべてのU+000DをU+000Aに置換
* [空白の畳み込み (strip and collapse ASCII whitespace)](https://infra.spec.whatwg.org/#strip-and-collapse-ascii-whitespace) : 連続したASCII whitespaceのブロックのすべてを一つのU+0020に置き換え、文字列前後のASCII whitespaceを除去

## CSS仕様

### CSS Text (Level 3)

CSSの空白処理で影響する対象は、各仕様で明記がない限り[document white space characters](https://www.w3.org/TR/css-text-3/#white-space-rules) (css-text-3 4.1)となる U+0020, U+0009, U+000A の文字。UCD [General_Category=Zs](https://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AGeneral_Category%3DZs%3A%5D&g=&i=)のU+0020, U+00A0以外の15文字は`other space separators`とされる。
またこのセクションの定義により、U+000Aや言語ごとにunicodeで定義された改行文字は`segment break`となり、プロパティーの設定によっては表示に反映される。
U+0009, U+000A, `segment break`の表現に当てはまらない[Control characters, General_Category=Cc](https://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AGeneral_Category%3DCc%3A%5D&g=&i=)の文字は、フォント上で不可視の場合でも何らかの形で可視表示せねばならず、`Other Symbols' (General_Category=So)として扱う。

推奨される(結果が同じであれば必須ではない)文字列処理の順序は[Appendix A](https://www.w3.org/TR/css-text-3/#order)にあり、以下の順になる。

* [空白文字の処理 I](https://www.w3.org/TR/css-text-3/#white-space-phase-1) css-text-3 section 4.1.1
* [文字変換 (text-transform)](https://www.w3.org/TR/css-text-3/#transforming) : 大文字小文字・全角などの処理
* [縦書きでの縦中横](https://www.w3.org/TR/css-writing-modes-3/#text-combine-horizontal)
* [文字の向き](https://www.w3.org/TR/css-writing-modes-3/#text-orientation) : 縦書きでの横寝かせなど
* [表示上の改行処理](https://www.w3.org/TR/css-text-3/#wrapping) : css-text-3 section 5
  * 改行挿入処理の中で以下は各表示行ごとに考慮する
    * [行頭インデント](https://www.w3.org/TR/css-text-3/#text-indent-property) : text-indent
    * [行ごとの表示方向](https://www.w3.org/TR/css-writing-modes-3/#text-direction) : rtl/ltr
    * [空白文字の処理 II](https://www.w3.org/TR/css-text-3/#white-space-phase-2) css-text-3 section 4.1.3
    * [フォント・グリフの選択](https://www.w3.org/TR/css-fonts-3/)
    * [letter-spacing](https://www.w3.org/TR/css-text-3/#propdef-letter-spacing), [word-spacing](https://www.w3.org/TR/css-text-3/#propdef-word-spacing)
    * [約物禁則処理](https://www.w3.org/TR/css-text-3/#hanging-punctuation-property)
* [行そろえ](https://www.w3.org/TR/css-text-3/#justification) : 行末そろえや、そろえた際の空きの入れ方
* [text-align適用](https://www.w3.org/TR/css-text-3/#text-align-property)

#### [white-space](https://drafts.csswg.org/css-text-3/#white-space-property) 空白の畳み込みを行うかの制御

ざっくりいうと、preエレメント的な扱いの拡張の設定と、畳み込み規則の詳細定義

* `normal`: infra specの畳み込みに準拠、soft wrap opportunitiesも適用
* `pre`: 空白の畳み込みを一切行わず、`segment break`は強制改行位置として扱い、soft wrapは適用しない (htmlのpreエレメントの扱い)
* `norwap`: 空白の畳み込みを行うが、soft wrapは適用しない
* `pre-wrap`: 空白の畳み込みは一切行わないが、soft wrapは適用する
* `break-spaces`: 以下の2点以外は`pre-wrap`と同じ。行末を含め空白や`other space separators`による空白のサイズを維持する、それらの空白の間を含めすべての空白文字の直後に`soft wrap`を許可する (その分行末に余計なサイズが付く)
* `pre-line`: 空白の畳み込みもsoft wrapも行うが、`segment break`を強制改行位置として扱う (強制改行以外は`normal`と同じ)

これらの処理で保持された(畳み込まれなかった)空白は`preserved white space`と呼ぶ。

#### [空白文字処理 section 4.1](https://drafts.csswg.org/css-text-3/#white-space-rules)

* Phase I: 畳み込みと置換 (このPhase I処理は表示用改行処理やbidiの考慮の適用前に行う)
  * `white-space`が`normal`, `nowrap`, `pre-line`の場合、空白の畳み込みを行う
    * 改行文字直前直後の`space`, `tab`の並びは削除する
    * 以下の`segment break`の変換規則により、畳み込み可能な`segment break`を変換する
    * 畳み込み可能な`tab`はU+0020 (`space`)に置換する
    * 連続する畳み込み可能な`space`の2つ目以降をゼロ幅に置換する (`soft wrap`可能な不可視文字)
  * `white-space`が`pre`, `pre-wrap`, `break-spaces`の場合、すべての`space`をU+00A0と扱う
    * `soft wrap`の位置について、`pre-wrap`の場合は空白の連続の最後のみに、`break-spaces`の場合はすべての空白の直後に許される
  * bidiの処理の前なので畳み込みはバイト列順の並びで処理される (表示の際の順序ではない)
* Phase II: トリミングと表示位置 (表示の際に文字列から表示用データへの変換で行われる処理)
  * 行頭の全ての空白の並びを除去する
  * `tab-size`が0に設定されていれば保持されたタブは表示されない、それ以外の場合は通常のタブの表示の処理で空白をあける
  * 行末の全ての空白の並びを除去する (bidiの場合は方向制御前の行末にあるものも除去)
  * bidi処理後に`space`や`other space separators`が行末にある場合は以下の処理を行う (ぶら下げ処理を行われた空白は文字選択時に選択可能になる)
    * `white-space`が`normal`, `norwap`, `pre-line`の場合、ぶら下げ処理を行う (領域外に出られる)
    * `white-space`が`pre-wrap`の場合、`forced line break`が続いていない場合に限りぶら下げ処理を行い、続く場合は`conditional hang` (文字揃えを行う前に収まらない場合のみぶら下げる)を行う
    * `white-space`が`break-spaces`の場合、行末でのぶら下げ・畳み込みは禁止され、行送りされる
* `segment break`変換処理
  * `white-space`が`pre`, `pre-wrap`, `break-spaces`, `pre-line`の場合、`segment break`は畳みこまれず、すべて`preserved line feed`として扱う
  * それ以外の場合、`segment break`は畳み込み可能になる。2つ目以降は除去され、残ったものはU+0020に置換されるか前後の状況により除去される
    * 前後に`zero width space character` (U+200B)がある場合は除去し、U+200Bのみ残す
    * 前後両方の文字の`East Asian Width`が`Fullwidth`, `Wide`, `Halfwidth`で`Ambiguous`でない場合、かつ、ハングルでなければ`segment break`は除去する
    * `segment break`に適用される`lang`が中国語、日本語、Yiの場合、かつ、前後のどちらかが約物か記号([Unicode General Category P*かS*](https://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AGeneral_Category%3DPd%3A%5D%0D%0A%5B%3AGeneral_Category%3DPs%3A%5D%0D%0A%5B%3AGeneral_Category%3DPe%3A%5D%0D%0A%5B%3AGeneral_Category%3DPc%3A%5D%0D%0A%5B%3AGeneral_Category%3DPo%3A%5D%0D%0A%5B%3AGeneral_Category%3DSm%3A%5D%0D%0A%5B%3AGeneral_Category%3DSc%3A%5D%0D%0A%5B%3AGeneral_Category%3DSk%3A%5D%0D%0A%5B%3AGeneral_Category%3DSo%3A%5D%0D%0A%5B%3AGeneral_Category%3DPi%3A%5D%0D%0A%5B%3AGeneral_Category%3DPf%3A%5D&g=&i=))で`East Asian Width`が`Ambiguous`であり、もう一方の`East Asian Width`が`Fullwidth`, `Wide`, `Halfwidth`でハングルでない場合、`segment break`は除去する
    * これまでに当てはまらない場合、U+0020に置換する
  * なお、[Unicode Emoji](https://unicode.org/cldr/utility/list-unicodeset.jsp?a=%5B%3AEmoji%3A%5D&g=&i=)で、`East Asian Width`が`Wide`か`Neutral`の文字は`Ambiguous`として扱う

#### [改行と単語区切り section 5](https://drafts.csswg.org/css-text-3/#line-breaking)



