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
* [UAX #14](https://www.unicode.org/reports/tr14/tr14-43.html): 改行位置・可能性に関する定義
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
  * [MediumSpace](https://html.spec.whatwg.org/multipage/named-characters.html#entity-MediumSpace) ([U+205F](https://unicode.org/cldr/utility/character.jsp?a=205F))
  * [NoBreak](https://html.spec.whatwg.org/multipage/named-characters.html#entity-NoBreak) ([U+2060](https://unicode.org/cldr/utility/character.jsp?a=2060))
  * [it](https://html.spec.whatwg.org/multipage/named-characters.html#entity-it) ([U+2062](https://unicode.org/cldr/utility/character.jsp?a=2062))
    * [InvisibleTimes](https://html.spec.whatwg.org/multipage/named-characters.html#entity-InvisibleTimes)
  * [ic](https://html.spec.whatwg.org/multipage/named-characters.html#entity-ic) ([U+2063](https://unicode.org/cldr/utility/character.jsp?a=2063))
    * [InvisibleComma](https://html.spec.whatwg.org/multipage/named-characters.html#entity-InvisibleComma)

### 置換

* [改行の正規化 (normalize newlines)](https://infra.spec.whatwg.org/#normalize-newlines) : U+000D U+000AをU+000Aに置換した後、すべてのU+000DをU+000Aに置換
* [空白の畳み込み (strip and collapse ASCII whitespace)](https://infra.spec.whatwg.org/#strip-and-collapse-ascii-whitespace) : 連続したASCII whitespaceのブロックのすべてを一つのU+0020に置き換え、文字列前後のASCII whitespaceを除去

## CSS仕様

以下、この文書記述時点での最新ドラフト準拠。

* css-text-3, css-text-4: 2020/02

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

検討点

* `forced line break`: `preserved newline character`などの明示的改行指示や、ブロックの先頭・最後
* `soft wrap break`: 表示幅に合わせて表示上で改行する場所、`soft wrap opportunity`である許可された場所でのみ可能
  * ハイフネーション可能位置や空白で示される言語が多い
  * Thai, Lao, Khmerでは単語区切りがなく、改行可能位置の明確な定義はない。U+200Bで示すのは可能。
  * Javanese, Balineseも同様に単語区切りでなく、`orthographic syllable boundary`での改行になる
  * 中国語、日本語、Yi、に加えて韓国語の一部では、特定のペア以外のどこでも改行可能
* これらを制御するために以下の属性がある
  * `line-break`: 改行規則の厳密さの選択
  * `word-break`: 改行不可な単語として扱う文字種の定義
  * `hyphens`: ハイフンを利用する言語でのハイフン規則の制御
  * `overflow-wrap`: 改行不可な文字列以外のどこでも改行可能で、不可なものは行送りする

概要

* `preserved forced break`で改行する、UAX #14のBK, NLも考慮する
* プロパティーでの指定がない限り、UAX #14のWJ, ZW, GL, ZWJを考慮する
* 単語区切りでない約物で改行可能な言語ではそれを優先する。CSSではブロック幅・言語・`line-break`の値などによる改行可能優先度は定義しないが、`word-break: break-all`では単語区切りの優先扱いは想定されておらず、`line-break: anywhere`の場合は優先扱いは禁止される。
* out-of-flowエレメントやインラインエレメントの境界は`forced line break`や`soft wrap opportunity`としては扱わない
* 置換された文字やインライン要素の改行可能性はUAX #14の定義に従うが、後方互換性から、それらとU+00A0の間には`soft wrap opportunity`を置く
* U+0020などの改行時に消える文字による`soft wrap opportunity`はその文字を含む要素の属性による。連続する2文字間については最下位の共通要素の`white-space`属性により、`line-break`, `word-break`, `overflow-wrap`属性に関してはLevel 3では未定義
* ボックス内の先頭の前・最後の後にある`soft wrap opportunity`はボックスの端と中身の間でなく、直前・直後(margin edge)で行う
* Ruby周りはcss-ruby参照
* 文字列解析が要求される言語で不可能な場合、全ての表示の塊(UAX #44)の間に`soft wrap opportunity`を置く

定義されている属性

* [word-break](https://drafts.csswg.org/css-text-3/#word-break-property)
  * 特にUAX #14でNU, AL, AI, IDの文字や表示の塊の間での`soft wrap opportunity`の制御であり、`white space`や約物によるものには影響しない
  * `normal`: 前出の言語による一般規則に従う
  * `break-all` 基本的にはどこでも改行可能にする。UAX #14 NU, AL, SAをIDとして扱う。約物には影響しない
  * `kepp-all`: 単語中での改行を禁止する。辞書ベースの改行位置以外の、NU, AL, AI, IDや表示の塊の間の`soft wrap opportunity`は無視される。
  * 改行を強制した前後においてもshapingは維持する
* [line-break](https://drafts.csswg.org/css-text-3/#line-break-property)
  * `auto`: UAによる判断、行長などに依存して選択される
  * それ以外には`loose`, `normal`, `strict`, `anywhere`が選べる
  * `anywhere`ではUAX #14のGL, WJ, ZWJなどを含めた禁止規則が無視され、ハイフネーションも行わない。また`white-space`による行末の空白処理も変更される。
  * 文字種ごとの扱いについて (ここは変更が検討されている)
    * 拗音・長音(UAX #14 CJ)の前での改行は、`strict`で禁止、`normal`, `loose`で許可
    * ‐ U+2010, – U+2013, 〜 U+301C, ゠ U+30A0の前での改行は、中国語・日本語の場合について`normal`, `loose`で許可され、それ以外では禁止
    * 繰り返し記号(々とか)の前やUAX #14 IN (2/3点ダーシ)などの分割不可文字の並びの間での改行は`loose`の場合のみ許可
    * 中央寄せ約物(中黒など)の直前、UAX #14 POかつ`East Asian Width`が`Ambiguous`, `Fullwidth`, `Wide`の後置文字の前、UAX #14 PRかつ`East Asian Width`が`Ambiguous`, `Fullwidth`, `Wide`の前置文字の後での改行は、中国語・日本語で`loose`の場合のみ許可
* [hyphens](https://drafts.csswg.org/css-text-3/#hyphenation)
  * U+002D (HYPHEN-MINUS), U+2010 (HYPHEN)で指定される場所でない、U+00ADや`shy`のハイフネーション可能点の制御
  * `none` (行わない), `manual` (事前定義のみ), `auto` (単語解析で挿入可能)がある
  * ハイフネーションを行ってもshapingは分割前の状態を維持する
* [overflow-wrap, word-wrap](https://drafts.csswg.org/css-text-3/#overflow-wrap-property)
  * オーバーフローがおこる際に禁止された点で改行可能かどうかを指定する
  * `normal`: 許可された点でのみ可能だが、`word-break: kepp-all`の場合は`normal`に読み替え可能
  * `anywhere`: どこでも改行挿入可能
  * `break-word`: `anywhere`と同等だが、`break-word`で追加される`soft wrap opportunity`は表示幅を計算する際には考慮しない
* 単語間改行でのshapingの扱いはつながったままの表示とする

#### [アライメント・単語揃え](https://drafts.csswg.org/css-text-3/#justification)

両端揃えなどの設定と、揃えにした場合の空白挿入の扱いについて

* `text-align`: `start`, `end`などの揃え方の指定 (`text-align-all`と`text-align-last`2つの短縮版)
  * `justify`の場合で空白が`collapsable`でない場合は、文字列を揃えに利用せず`justification opportunities`なしとみなす。もし文字列を揃える場合は、`tab`を空白処理基準に従って並べる。
  * オーバーフローする場合は`end`側を外に伸ばす
* `text-justify`: 空白挿入の方法
  * `auto`: (既定値) 速度と品質を考慮してUAが決定する、記述方式・言語によって処理を変えるべきであるとされている
  * `none`: `justification opportunities`なしとみなす (user stylesheetでの設定が主目的)
  * `inter-word`: `word separator`で空きを調整する (`word-spacing`の設定に依存)
  * `inter-character`: 全ての`typographic character units`間で空きを調整する (`letter-spacing`の設定に依存)
* `justification opportunity`: 調整可能な位置の定義で、`word separator`などの単一`typographic character unit`もしくはその並びで、`text-justify`の値により決定される
  * 空白の挿入は`letter-spacing`, `word-spacing`での空き量に加算される。
  * 異なる言語の文字が並ぶ場合など、内部処理上で複数レベルの優先度の定義は許され、文字種によらず優先度のみで空き量調整を行う。
  * 揃えの方法によらず、リガチャやその他のフォントの属性を利用可能(Lv3の制御範囲外)だが、必須のリガチャやshapingを解除することは許されない。
  * `justrification opportunity`が存在する場合、揃えは設定されていれば必ず適用される。
* 記号・約物の扱い(Unicode `S*`, `P*`)はその文字の属する言語、もしくは`Common`の場合は文章で主要な言語に従って行う。ただし、言語ごとに要求される処理は別途適用する。
* 空き量調整で揃えられない行は`text-align-last`によって処理する
* cursiveのjoinしている部分に空きを入れることは禁止され、伸ばして表記可能な部分に挿入(tatweelなど)するか、`justification opportunity`非存在として扱う。
* `auto`に対する要求は明示されていないが、最低要件は提示されている
  * 記述に利用される言語で特に禁則規定がない限り、単語区切り、`block script`の塊・`clustered script`の塊と他の塊の間、に`justification opportunity`が存在する
  * `block script`のすべての文字、`clustered script`のすべての文字は同等に扱う (異言語交じりの場合など)
* [i18n jusitification](https://www.w3.org/International/articles/typography/justification)の情報も参照

#### [空き量](https://drafts.csswg.org/css-text-3/#spacing)

単語間(`word-spacing`)、文字間(`letter-spacing`)の空き量の指定

* `word-spacing`: `normal`は`0`とし、値はフォント指定の単語間空き量に追加する値(両側に半分ずつ)となる
  * 単語区切り文字は[U+0020](https://unicode.org/cldr/utility/character.jsp?a=0020), [U+00A0](https://unicode.org/cldr/utility/character.jsp?a=00A0), [U+1361](https://unicode.org/cldr/utility/character.jsp?a=1361) (Ethiopic), [U+10100](https://unicode.org/cldr/utility/character.jsp?a=10100)/[U+10101](https://unicode.org/cldr/utility/character.jsp?a=10101) (Aegean), [U+1039F](https://unicode.org/cldr/utility/character.jsp?a=1039F) (Ugaritic), [U+1091F](https://unicode.org/cldr/utility/character.jsp?a=1091F) (Phoenician) など
  * 指定のない場合もしくは[U+200B](https://unicode.org/cldr/utility/character.jsp?a=200B)の場合は空き量を追加禁止
  * 一般約物(U+2000からU+206F)、サイズ指定空白(U+3000, U+2000からU+200A)は単語区切り文字とは扱わない
* `letter-spacing`: `typographic character units`間の追加空き量で、bidi処理後にカーニングや`word-spacing`に追加して挿入され、揃えの指定によっては増減が加えられる
  * 互換性上、計算結果が0の場合は`normal`が`getComputedStyle()`から戻る
  * 連続したインライン要素(画像やインラインブロック)は一つの`typographic character unit`として扱う
  * 行頭・行末には適用しない
  * レンダリング要素の扱い上、空き量は両側の`typographic character units`が属する最内の要素に属する
  * 不可視のゼロ幅制御文字の位置には挿入されない
  * 空き量が0でない場所では必須でないリガチャは適用しないが、`font-feature-settings`で上書きされうる
    * OpenTypeでrligは必須であるリガチャである
* 繋げ文字の場合、ある塊に割り当てられた全空き量と同じ量を伸ばすことが可能な位置に再割当することができる
  * 伸ばすことが可能な位置を扱えない場合は開けることは禁止
* shapingの解除条件
  * `typographic character units`を分割し、かつ以下の条件を満たすインラインボックスの端ではshapingは解除される
    * 0でないmargin, border, paddingが設定されている
    * `vertical-align`が`baseline`でない
    * 端がbidi分割場所
  * 形式に変化がない部分やグリフに影響しない変化のみの場所では解除禁止
  * それら以外で、フォントの制約がない場合は解除しない

#### [行端処理](https://drafts.csswg.org/css-text-3/#edge-effects)

* `text-indent`: 行頭空き指定、`each-line`や`hanging`がない限り先頭行のみで、絶対量指定かブロック要素全幅に対する割合
  * `each-line`: `forced line break`の直後全てに挿入する
  * `hanging`: 適用行頭の反転
* ぶら下げ処理の対象の文字
  * ぶら下げ処理が行われた文字は行の長さの計算に入らない。
  * ぶら下げ処理が行われなかった場合は行の長さの計算に入れ、揃え量計算でも考慮される。
  * 条件付きぶら下げ処理対象文字は、揃え処理前にのみぶら下げ処理対象となり、サイズ計算では`min-content`には入らないが`max-content`には入る
  * 複数文字が同時にぶら下がることは可能だが、最大文字数の制約を付けることは許される
* `hanging-punctuation`: 約物のぶら下げ処理を行うかどうか
  * `none`: 行わない
  * `first`, `last`: 要素の先頭・最終行で行う、Ps, Pf, Pi, U+0027, U+0022が対象
  * `force-end` (強制), `allow-end` (許可): 行末の`stop or comma`を対象に行う
    * `stop or comma`: U+002C, U+002E, U+060C, U+06D4, U+3001, U+3002, U+FF0C, U+FF0E, U+FE50, U+FE51, U+FE52, U+FF61, U+FF64
    * これ以外でも該当すると思われる文字を処理対象に含められる

### CSS Text Level 4 での追加

空白処理以外では

* [追い出し](https://www.w3.org/TR/css-text-4/#wrapping)
* [最終行の行長](https://www.w3.org/TR/css-text-4/#last-line-limits)
* [一括指定のための`white-space`](https://www.w3.org/TR/css-text-4/#white-space-property)
* [単語内分割 (hyphenation)](https://www.w3.org/TR/css-text-4/#hyphenation)

#### [Word boundaries](https://www.w3.org/TR/css-text-4/#word-boundaries)

分かち書きなどのために利用できる設定の導入で、wbrやU+200Bを挿入することで位置を定義する。

* `word-boundary-detection`: 単語間区切りの検出方法、検出された位置に`virtual word boundary`が挿入される
  * `manual`: `virtual word boundary`の挿入はしない、SAはAL属性も持つとして扱う (`line-break`が`anywhere`以外の場合に`soft wrap opportunity`が存在しなくなる)
  * `normal`: 東南アジア諸言語以外においては`virtual word boundary`の挿入はしない、SAはAL属性も持つとして扱うが`virtual word boundary`を解析して必要なら挿入しなければならない
  * `auto(lang)`: 指定の言語での仕様に沿った解析を行う
  * `virtual word boundary`の挿入は[空白文字処理 Phase 1 (Lv3 4.1.1)](https://www.w3.org/TR/css-text-3/#white-space-phase-1)の前、かつ、`word-boundary-expansion`の処理前に行う。
  * `virtual word boundary`挿入位置で複数のインラインボックス境界がある場合は、最外の境界に入れる。
  * 以下の部分には`virtual word boundary`を挿入禁止
    * 親要素に`manual`がある場合の先頭・最後
    * 単語区切り文字、空白文字、U+200Bの直前・直後
    * 単一`typographic character unit`内の文字間
    * CL, CP, IS, EXの文字が後ろに来る文字との間
    * OPの文字が前に来る文字との間
    * GL, WJ, ZWJの文字が隣に来る文字との間
  * 以下の部分には`vitual word boundary`を挿入すべきではない
    * PO, NSの文字が後ろに来る文字との間
    * PRの文字が前に来る文字との間
* `word-boundary-expansion`: 単語間文字の置き換えの指定
  * `none`: 行わない
  * `space`: U+200BをU+0020に置き換え
  * `ideographic-space`: U+200BをU+3000に置き換え
  * `forced line break`の直前直後のU+200Bは置き換え禁止
  * 挿入された`virtual word boundary`であるwbrはU+200Bとして扱う
  * 処理は[空白文字処理 Phase 1 (Lv3 4.1.1)](https://www.w3.org/TR/css-text-3/#white-space-phase-1)の前に行い、そのあとの処理はU+200Bでなく置き換えられた文字があるとして行う

#### [空白除去処理](https://www.w3.org/TR/css-text-4/#white-space-processing)

* `text-space-collapse`: 空白文字を畳みこむかどうかの選択
  * `collapse`: 既定の動作で、連続の空白文字を１文字に置き換える
  * `preserve`: 畳みこまない、`segment break`は`forced line break`になる
  * `preserve-breaks`: 畳みこむが、`segment break`は`forced line break`になる
  * `preserve-spaces`: 空白を畳み込まないが、タブや`segment break`を空白に置き換える
  * `discard`: 全て除去する
* `text-space-trim`: 先頭・最後での除去のオプション、既定は`none` (行わない)
  * `trim-inner`: ブロックコンテナにおいて先頭・最後を除去する
  * `discard-before`: 先頭の空白を要素の直前の空白に畳み込む
  * `discard-after`: 最後の空白を要素の直後の空白に畳み込む

#### [空き量調整](https://www.w3.org/TR/css-text-4/#spacing)

* `line-padding`: 先頭・末尾の追加padding量
* `text-spacing`: 文字種による空き量処理の設定
  * `auto`: 自動処理
  * `normal`: 現状では`space-start`, `allow-end`, `trim-adjacent`
  * `none`: 行わない
  * `ideograph-alpha`: `ideographs`, `non-ideographic lettes`間に1/4emを追加
  * `ideograph-numeric`: `ideographs`, `non-ideographic numerals`間に1/4emを追加
  * `punctuation`: 言語で定義された約物周りの分割禁止空白を入れる
  * `space-start`: `fullwidth opening punctuation`を行頭で全角として扱う
  * `trim-start`: `fullwidth opening punctuation`を行頭で半角として扱う
  * `space-first`: 改行の行分割直後のみ`space-start`とする
  * `allow-end`: `fullwidth closing punctuation`を追い出しの代わりに行末で半角として扱う
  * `space-end`: `fullwidth closing punctuation`を行末で全角として扱う
  * `trim-end`: `fullwidth closing punctuation`を行末で半角として扱う
  * `space-adjacent`: 行頭でない`fullwidth opening punctuation`と行末でない`fullwidth closing punctuation`を全角として扱う
  * `trim-adjacent`: 連続した約物の空き量を調整する
  * `no-compress`: 揃えの時にtext-spacingを圧縮しない
* `trim-adjacent`での処理
  * `fullwidth opening punctuation`が、`fullwidth opening punctuation`, `fullwidth middle dot punctuation`, U+3000に続く場合と、同じかより大きなサイズの`fullwidth closing punctuation`に続く場合に半角にする
  * `fullwidth closing punctuation`の後に、`fullwidth closing punctuation`, `fullwidth middle dot punctuation`, U+3000が続く場合と、同じ課より大きなサイズの`fullwidth opening punctuation`が続く場合に、半角にする
* 約物の半角調整はhalt, vhalを利用可能だがhwidや対応する半角文字を利用することは不可
  * プロポーショナルの場合、フォントに情報がない場合は処理不可
* 文字種の定義
  * `ideographs`: U+3041からU+30FFで`P*`でないもの、CJKストローク (U+31C0からU+31EF)、カタカナ発音 (U+31F0からU+31FF)、Han属性を持つ文字
  * `non-ideographic letters`: `ideograph`, EAW=F, 縦書き中の縦中横の文字、でない`L*`と`M*`の文字
  * `non-ideographic numerals`: EAW=F, 縦書き中の縦中横の文字、でない`Nd`の文字
  * `fullwidth opening punctuation`: `Ps`中、CJK (U+3000からU+303F)かEAW=Fの文字、またU+2018, U+201Cで、半角にする場合は左半分もしくは上半分を消す
  * `fullwidth closing punctuation`: `Pe`中、CJK (U+3000からU+303F)かEAW=Fの文字、またU+2019, U+201Dで、もしくは`fullwidth colon punctuation`と`fullwidth dot punctuation`も含むことがある。半角にする場合は右半分かう下半分を消す
  * `fullwidth middle dot punctuation`: U+00B7, U+2027, U+30FBで、`fullwidth colon punctuation`と`fullwidth dot punctuation`を含むことがある
  * `fullwidth colon punctuation`: U+FF1A, U+FF1B
  * `fullwidth dot punctuation`: U+3001, U+3002, U+FF0C, U+FF0E


