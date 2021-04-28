# WebFont関係まとめ

まだ作成中

ToC

* [関連仕様、ノート類](#関連仕様ノート類)
* [TTF/OTF/OFF/CFF関連](#ttfotfoffcff関連)
* [WOFF2の概要](#woff2の概要)
  * [WOFF2ファイル構成](#woff2ファイル構成)
  * [フォントデータのtransformation](#フォントデータのtransformation)
  * [Brotli](#brotli)
* [WOFF2後のwebfont高速化](#woff2後のwebfont高速化) (PFE)
  * [evaluation reportでの評価対象](#evaluation-reportでの評価対象)
  * [Incremental font transferの提案仕様](#incremental-font-transferの提案仕様)

## 関連仕様、ノート類

WOFF関係のパートはいれた。Brotliの詳細、OFF以降はまだ

* WOFF関係 (Web Open Font Format; [WebFonts WG](https://www.w3.org/Fonts/WG/))
  * [WOFF2](https://www.w3.org/TR/2018/REC-WOFF2-20180301/) (2018/03/01 REC)
    * [WOFF2 Evaluation Report](http://www.w3.org/TR/2016/NOTE-WOFF20ER-20160315/) (2016/03/15 WG-NOTE)
  * [WOFF1](https://www.w3.org/TR/2012/REC-WOFF-20121213/) (2012/12/13 REC)
  * [MicroType Express (MTX) Font Format](https://www.w3.org/Submission/2008/SUBM-MTX-20080305/) (2008/03/05 Monotype Imaging SUBM)
    * WOFF2の開発の際に参考とされた効率化の手法の文書、仕様書よりも各項目の導入背景などが詳しい
    * TTFを変換して中間形式のCTFに、LZCOMPで圧縮してMTXに
  * [Incremental Font Transfer](https://w3c.github.io/PFE/Overview.html) PFE向けの仕様
    * 開発中、このページの現状では2021/3/22版を参照している
  * [Progressive Font Enrichment (PFE) Evalucation Report](https://www.w3.org/TR/2020/NOTE-PFE-evaluation-20201015/) (2020/10/15 WG-NOTE)
* [RFC 7932 (Brotli Compressed Data Format)](https://tools.ietf.org/html/rfc7932)
* [Open Font Format (OFF; ISO/IEC 14496-22:2015)](http://standards.iso.org/ittf/PubliclyAvailableStandards/c066391_ISO_IEC_14496-22_2015.zip)
  * [Amendment 1: Updates for font collections functionality](http://standards.iso.org/ittf/PubliclyAvailableStandards/c069450_ISO_IEC_14496-22_2015_Amd_1_2017.zip)
  * [Amendment 2: Updated text layout features and implementations](http://standards.iso.org/ittf/PubliclyAvailableStandards/c070994_ISO_IEC_14496-22_2015_Amd_2_2017.zip)
* [OpenType](http://www.microsoft.com/typography/otspec/)
* [TrueType](https://developer.apple.com/fonts/TrueType-Reference-Manual/)
* [Compact Font Format (CFF; Adobe Tech Note 5176)](http://partners.adobe.com/public/developer/en/font/5176.CFF.pdf)

## TTF/OTF/OFF/CFF関連

* SFNT?
* OTF = TTF + PS CFF/Type2

## WOFF2の概要

* 重複データなどを除くようなフォントのテーブル自体を簡単化するプリプロセスを行う
* フォントデータ本体は圧縮形式でファイル内に格納される、WOFF2ではBrotliの単独ストリーム、WOFF1ではzlib/compress2を利用しテーブルごと圧縮

MTXでは以下のような処理を行っており、その中からピックアップされている。Data setへの分割は取り入れられなかった部分。

* TTFからCTFの際に`glyf` (重複情報削除), `loca` (いれない、デコード時に再生成), `cvt ` (より小さく格納), `hdmx` (bitエンコード), `VDMX` (bitエンコード)に変換を掛けた
  * `glyf`の変換は`Triplet Encoding`を含め、WOFF2の変換に持ち込まれている
* フォントデータを３パートに分け、各パートごとにテーブルごとにLZCOMPで圧縮
  * Data set 1: `glyf`のアウトラインデータとその他のテーブル全部、`cvt `, `hdmx`, `VDMX`, `glyf`を圧縮、その他は非圧縮
  * Data set 2: `glyf`のpush dataを格納
    * WOFF2での255UInt16は255USHORTとして定義されている
  * Data set 3: Glyph instructionを格納

### WOFF2ファイル構成

概要

* 一番最後のブロックを除き、ブロックごとに4byteでパディングされる
* (数値)データ型として、UInt8, Int16, UInt16, 255UInt16, UIntBase128が定義されている
  * 255UInt16: UInt16の1-3バイトへのマッピング、0-252は1バイト、762以上は3バイトになる
  * UIntBase128: 32bit非負数値の1-5バイトへのマッピング、元数値の7bitごとの切り出しで最後のバイトで先頭ビットがたつ

ファイルの構成ブロックは以下、リストの並び順にファイルの中に並ぶ

* WOFF2Header : 全体についてのデータを格納するヘッダ、圧縮時・解凍後のデータサイズやデータブロックまでのオフセット
  * UInt32 signature: `wOF2`
  * UInt32 flavor: sfnt version - `ttcf`などのフォントコレクションといったフォーマットの指定
  * UInt32 length: WOFFファイルの全サイズ
  * UInt16 numTables: フォントテーブルのディレクトリのエントリ数
  * UInt16 reserved: `0`
  * UInt32 totalSfntSize: sfntヘッダ、ディレクトリ、フォントテーブル、の非圧縮時の全サイズ、パディング込み（`glyf`テーブルなどの記述によって展開後に異なる可能性があるので参照用のみ）
  * UInt32 totalCompressedSize: 圧縮部分の全サイズ
  * UInt16 majorVersion: WOFFファイルのメジャーバージョン
  * UInt16 minorVersion: WOFFファイルのマイナーバージョン
  * UInt32 metaOffset: ExtendedMetadataまでのオフセット
  * UInt32 metaLength: 解凍後のExtendedMetadataのデータサイズ
  * UInt32 privOffset: PrivateDataまでのオフセット
  * UInt32 privLength: PrivateDataのデータサイズ
* TableDirectory : WOFF2Header.numTablesの数のテーブルのエントリ、各エントリは可変長なので読まないとサイズは決まらない。またフォントコレクションの場合も全テーブルをここに並べる（分別は次のブロックで）。
  * 各エントリは以下の４つの値の配列、圧縮領域に格納されている順に並べられる
    * UInt8 flags: `0..5`の6bitがテーブル定義(`63`以外は定義値、`63`は次の値を利用)、`6..7`の2bitがプリプロセスでのtransformationのバージョン番号`0-3`を示す
    * UInt32 tag: （オプション）`flags=63`の時のテーブル名４文字、後ろ空白パディング
    * UIntBase128 origLength: 非圧縮時のサイズ (null transforationでない場合は戻した後のサイズ、また処理によっては複数の結果になる場合があるので必ずしも正しくはならない)
    * UIntBase128 transformLength: transform適用後のサイズ（null transformationでない場合にのみ必要、格納されたデータのサイズとなる)
  * 未定義のtransformationのバージョンが指定されたものはテーブルごと拒否
* CollectionDirectory : 該当のWOFFファイルがフォントコレクションの場合にのみ必要
  * データは`CollectionHeader`と`CollectionFontEntry`のリストで構成され、一つの`CollectionHeader`の直後に定義された数の`CollectionFontEntry`が並ぶ
  * `CollectionHeader`はテーブル数の定義
    * UInt32 version: オリジナルのフォントのTTCヘッダにあるバージョン
    * 255UInt16 numFonts: コレクションの中のフォント数
  * `CollectionFontEntry`は各フォントに対応するテーブルのピックアップ用のデータ
    * 255UInt16 numTables: 利用するテーブル数
    * UInt32 flavor: `sfnt` version
    * 255UInt16 index (`numTables`分の配列): `TableDirectory`のエントリを0始まりで数えたときの利用するテーブルの番号の配列
  * コレクション間のテーブルの共有は可能 = 違うコレクションで`index`の中に同じ番号が出現してもよい（逆に同じテーブルデータを複数回含むことは禁止）
    * `glyf`と`loca`のペアについて、片方のみを共有しているような設定は禁止
    * エンコーダは入力されたフォントファイルに対してここの並び順を維持するように設定する必要がある
    * デコーダはこのコレクションの圧縮処理を行わない元の形式に戻すようにすべき（あとのブラウザ処理の中でTTF/OTFと同じように利用できるようにするため？）
* CompressedFontData : テーブル全体のデータが圧縮されたデータ領域
  * デコーダは展開後のデータをOFF仕様に合うように展開する必要があり、`checkSum`の値が正しいものである必要がある（再計算必要）、また全体に対して`checkSumAdjustment`の値を再計算し`head`テーブルを更新する
  * 展開後のサイズはTableDirectoryのサイズの合計に一致する必要がある
  * transformation : `glyf`, `loca`, `hmtx`に適用される
    * `glyf`: アウトラインデータの保持
    * `loca`: それぞれのグリフのデータが`glyf`のどこに保持されているかのオフセットデータ
    * `hmtx`: グリフの水平方向のメトリクスの保持
  * ここの最適化処理のために入力の元ファイルとデコードされて得られたファイルはバイナリで一致しないことがあるので、WOFFには`DSIG`テーブルは含めない
  * エンコーダは`head`テーブルの`flags`のbit 11をたてないといけない（ロスレス変換を経たということの提示のため）
* ExtendedMetadata
  * 圧縮されたXML (UTF-8)のデータ、vendor, copyrightなどのデータを入れられる部分
  * XMLの形式やエレメント定義はWOFF1/WOFF2で変化なし
* PrivateData
  * 非定型のベンダー固有データ領域

テーブル・フォントデータの並び順について（以下の詳細は[section 5.5](https://www.w3.org/TR/WOFF2/#table_order)から）

* OFFではテーブルの並び順を`ascending alphabetical order`としているが、WOFFでは処理の高速化のために制限をつけている
* `glyf`と`loca`は常にペアでこの順に配置されている必要がある。reverse transformが`glyf`に設定されている時に`loca`が必要なため。
* `glyf`と`loca`はWOFFが一つのフォントセットのみの場合は間に別なものが入っていいが、フォントコレクションの場合は必ず対応関係の`glyf`と`loca`は連続しなければならない
  * `cmap`, `glyf`, `hhea`, `hmtx`, `loca`, `maxp`の並び順は可能
  * フォントコレクションでは`cmap`, `glyf`, `loca`, `hhea`, `hmtx`, `glyf`, `loca`, `maxp`, `post` のような並び順になる必要がある

#### WOFF v1からの変更

* 圧縮がBrotilになった
  * 詳細の検討の流れはWOFF2 Evaluation Reportに、WOFF1はテーブルごとにzlib/compress2圧縮だったのが、テーブル全体をBrotil圧縮に変更
* 圧縮効率を上げるためにテーブルのtransformationを導入 (MTX形式から一部の処理を持ってきた)

### フォントデータのtransformation

#### `glyf`

* `3`: null transform (unmodified)
* `0`: table transformation, 重複情報の削除と実際のグリフアウトラインに対する効率的なエンコード
  * エンコード(transform)してデコード(reconstruct)したものは、意味・機能的には同じであるが、ビット列として異なる可能性があるという意味で可逆変換ではない
  * WOFF2 Table Directoryの`origLength`とデコード後のサイズは一致しない可能性がある
  * 圧縮効率向上を目的に複数のストリームに分割することがあり、サブストリームのサイズの配列の後に各サブストリームを並べた配置となることがある
  * デコーダは１グリフごとに処理を行い、再構成した`glyf`テーブル内でのオフセットが`loca`テーブルの値になる

##### transform後の`glyf`テーブルのデータ構造

* Fixed/UInt32 (0x00000000): version
* UInt16 numGlyphs: 定義されたグリフの数
* UInt16 indexFormat: `loca`テーブルのオフセットの形式、`head`テーブルの`indexToLocFormat`と一致
* UInt32 nCounterStreamSize: `nCounter`ストリームのバイト数
* UInt32 nPointsStreamSize: `nPoints`ストリームのバイト数
* UInt32 flagStreamSize: `flag`ストリームのバイト数
* UInt32 glyphStreamSize: `glyph`ストリームのサイズ数
* UInt32 compositeStreamSize: `composite`ストリームのバイト数
* UInt32 bboxStreamSize: `bbox`データのバイト数、`bboxBitmap`と`bboxStream`の合計
* UInt32 instructionStreamSize: `instruction`ストリームのサイズ
* Int16 nCounterStream (array): 各グリフレコードの`counter`の数の配列
* 255UInt16 nPointsStream (array): グリフレコード中の各`counter`のアウトライン点の数の配列
* UInt8 flagStream (array): 各アウトライン点に対するフラグの配列
* Vary glyphStream (array): [5.2節](https://www.w3.org/TR/WOFF2/#triplet_decoding)に定義される形式でのアウトライン点座標の配列
* Vary compositeStream (array): `component`フラグの値と付属するcomposite glyphのデータの配列
* UInt8 bboxBitmap (array): explicit bounding boxかを示す、ビット数で`numGlyphs`分の長さの配列
  * ビット列は先頭ビットから順に、全データサイズは`4 * floor((numGlyphs + 31) / 32)` (4byteパッド)
  * 明確なbboxなのか点座標から導出可能なbboxなのかのフラグ、`bboxStream`に対応するbboxが格納されていれば立てる
  * simple glyphについてはエンコーダがx/y Min/Maxを計算して一致したらデータを格納しない、一致しなければこのフラグを立ててデータを格納する
  * `counter`がゼロ個の場合はbboxがすべて0であることを確認し、違ったらエンコーダは入力フォントを無効として却下する、okならフラグを下す
  * composite glyphについては必ず立ててbboxを格納する
* Int16 bboxStream (array): グリフのbounding boxデータの配列
* UInt8 instructionStream (array): 各対応するグリフの`instruction` setの配列

glyphStreamに格納されるデータは一つ前の点座標に対するdeltaで表記され、先頭は(0, 0)に対するdeltaである。
バイト列からのdelta値の再構成の対応表は[5.2節 `Triplet Encoding`](https://www.w3.org/TR/WOFF2/#triplet_decoding)にあり、
先頭バイトがIndexで`flagStream`からの1バイトを含み2-5バイトで表記される値(`glyphStream`からは1-4バイト)で格納され、計算後は(`flag`, `x`, `y`)のセットとなる。
`flagStream`からの`flag`は

* 先頭bit: on/off-curveの点のフラグ
* 残り7bit: `glyphStream`からの値を評価するためのインデックス
  * `glyphStream`からのデータをX/Yに対して割り振るビット長 (割り振る場合は先頭ビットからXに利用)
  * 割り振られた値に対して出力を計算するデータ、値に追加する量と正負
    * たとえばIndex=4だと、１バイトをXに0bit、Yに8bitで割り振り、Yに512を足して負の値として評価する、となる

##### デコーダの再構成の流れ

* `nCounterStream`からInt16 1データを読み、`glyf`の`numberOfCounters`の値とする
  * 0なら空、正ならsimple glyphでアウトラインのcounterの数、0xFFFF (-1)ならcomposite glyph、となり、以下の各処理を行う
  * 空の場合
    * `loca`は一つ前のグリフと同じ値に設定する
  * simple glyph
    * `nPointsStream`から`numberOfCounters`分の255UInt16データを取得、それぞれがcounter内のデータ点数となり、`endPtsOfCounters[]`へ格納 (数でなく終了位置とするので-1する)
    * `flagStream`から一つ前に計算した全ポイント数分のUInt8データを取得、これがデータ点のフラグの配列になる
    * 全ポイント数分の点座標を`glyphStream`から読んでいき、各データから計算したdelta-x/yを`glyf`に格納していく
    * `glyphStream`から一つの255UInt16の値を取得、`instruction`の配列の長さ(`instructionLength`)となる
    * `instructionLength`分のデータを`instructionStream`から取得する
  * composite glyph
    * `compositeStream`から一つのUInt16の値を取得、TrueTypeの`component flag word`のデータとする
    * `component flag word`のデータに対応する長さの追加データを`compositeStream`から読みだし (4-14バイト)、`glyf`に格納する
      * `glyph index`, `arg1`, `arg2`, `optional scale`, `affine matrix`のデータ
      * この段階で読みだされた`component flag word`の`FLAG_MORE_COMPONENTS` (bit 5)が立っていれば再度このステップを繰り返す
    * 取得された`component flag word`のどれかに`FLAG_WE_HAVE_INSTRUCTIONS` (bit 8)が立っているものがあれば、`instruction`が存在するのでsimple glyphの4-5ステップ目を行う
* bboxについて`bboxBitmap`でデータが格納されているグリフについて、`bboxStream`から4つのInt16を取得しxMin/yMin/xMax/yMaxの値とする
  * simple glyphについては必要であれば計算する
  * composite glyphについては必ずついている

#### `loca`

独立してtransformationの設定の値を持つが、`glyf`のtransformationに依存するので現実には`glyf`の値と同じとなる

* `3`: null transform (unmodified)
  * データをそのまま格納し、オリジナルのフォントテーブルの解析時と同じくデータを読むのに必要となる
* `0`: table transformation
  * `glyf`のデコーダの処理の中で`loca`テーブルが作成されるのでデータはない
  * `transformLength`は必ず0
  * `origLength`は`numGlyphs`+1にグリフごとのサイズを掛けたもの、`glyf`の`indexFormat`が0の場合2バイト、それ以外は4バイト

#### `hmtx`

* `0`: null transform (unmodified)
* `1`: table transformationを行う、`hmtx`テーブルの冗長部分を削る
  * OFFでは`hmtx`はMin側にプロポーショナル・モノスペースの２種のグリフに対応する２つの配列を持つが、通常はTrueTypeの推奨通り同じなので省ける

##### transform後の`hmtx`テーブルのデータ構造

フォントが`glyf`テーブルを持つなどのTrueType系列の場合にのみ適用可能である。
エンコーダは全グリフについて`leftSideBearing`がbbox `xMin`に一致するかを確認する必要があり、一致していればこのtransformを適用する必要がある。
なお、コレクション内で`hmtx`テーブルが共有されている場合は全ての対応先についてこの確認をする必要がある。

* UInt8 Flags: 適用した変換の詳細を示すビット列
  * `TableDirectory`で変換が指定されている場合、bit 0/1は立て、bit 2-7は予約(0)となる。なので必ず0xC0、そして`advanceWidth`のみ存在することになる。
  * bit 0: 設定時には`lsb[]`が存在しない、`glyf`のxMinから
  * bit 1: 設定時には`leftSideBearing[]`が存在しない、`glyf`のxMinから
* UInt16 advanceWidth (array): プロポーショナルグリフの水平方向の`advanceWidth`の配列、`hhea`テーブルの`numOfHMetrics`の個数分
* Int16 lsb (array): プロポーショナルグリフの水平方向の`left side bearing`の配列、`hhea`テーブルの`numOfHMetrics`の個数分
  * `Flags`のbit 0が設定されていない場合のみ存在する
* Int16 leftSideBearing (array): モノスペースの水平方向の`left side bearing`の配列、`numGlyphs` - `numOfHMetrics`の数分
  * `Flags`のbit 1が設定されていない場合のみ存在する


### Brotli

* LZ77とハフマン符号化ベースの圧縮アルゴリズム
* 120KiB/13000 words程度のコーパスから生成された事前定義辞書を利用
* CFFアウトラインデータがde-subroutinizedされている方が圧縮後のサイズが5-10%程度小さくなることが観測されている、が同時にde-subroutinizationにより～10%サイズが増えていた: WOFF2では取り入れられていない
* 同じ圧縮用テーブルを利用しての後ろに追加していくバイナリパッチが可能


## WOFF2後のwebfont高速化

Evaluation reportではCSSによるunicode-rangeでのstatic subsetが導入された後のwebfontの問題点として

* CJKなどのグリフが多い言語において全部いりフォントのデータサイズが巨大になり利用されにくい
* 約物を含む複数言語に共通して利用される文字についてstatic subsetの場合にフォントが混ざって複雑なshapingやカーニング情報などが正しく利用できない

などが挙げられている。これに対応するためにprogressive subsetが提案され、一つ目については必要なコードポイントの部分のみのダウンロード、
二つ目については整合性のある大きいセットから必要部分だけを持ってくることでshaping/kerningを整合性をもって適用することが可能になる。

### evaluation reportでの評価対象

フォント全体を落としてくるという操作に対して、unicode rangeでの複数woff2ファイルへの分割、以外に、２種類の方式が追加で評価されている

* patch subset: 個別リクエストに向けてサーバ上で動的にサブセットを作成する方式、サーバ上での処理が可能でなければならない
  * 初回は必要とされたグリフだけが入ったOpenTypeフォント、その後継続してのリクエストではBrotilのバイナリパッチ方式を利用して追加のグリフを供給
* range request: ビデオストリームのように必要とされた部分だけを抜き出してリクエストする、クライアントがサーバにbyte rangeのリクエストを出す
  * 最初にクライアントはtableDirectoryまでをサーバから取得し、必要なテーブル・グリフのみをbyte rangeのリクエストで要求する
  * グリフのテーブルはプリプロセスされている必要があり、また、ファイルの一番最後に配置、アウトラインのグリフが相互に独立している必要がある
    * 取得してくるbyte rangeの簡単化のためにプリプロセスでよく同時に使われるコードポイントを近くに配置するなどの処理も行える
  * グリフ以外のテーブルは全部落としてくることになる

評価はいくつかの言語グループを想定して行われている。それぞれ転送されるであろうバイト数、転送速度によるコスト評価が行われた。

* alphabetic
  * 転送量はどの方式でも改善、patch subsetで50%、unicode rangeで40%
  * コスト評価はrange requestの場合(と低速ネットワークの場合出は全て)のみ非常に悪くなった
* glyph shaping
  * 転送量はどの方式でも改善、patch subsetで55%、unicode rangeとrange requestで25%
  * コスト評価はrange requestの場合非常に悪くなった
* CJK
  * 転送量はpatch subsetで90%超、range requestで80%、unicode rangeで50%の改善
  * コスト評価は高速ネットワークではどれでも改善、低速では悪くなった。patch subsetが一番改善が大きい。

評価での結論は、patch subsetもrange requestも高い効果をもたらしたとするが、
patch subsetはサーバの更新が必要だがrange requestは既存のフレームワーク内で処理可能とも指摘。
今後の作業として以下の点を挙げている:

* シミュレーションではWOFF2圧縮の一つ目の処理であるテーブル再配置を行っていないので、その点で改善の可能性
* コードポイント推定をよりよくし、ネットワーク速度依存性について追加で解析
* ストリーミングフォント向けのプリプロセス方式をさらに追及する
* HTTP/2 POSTはキャッシュをバイパスするので、キャッシュ可能な方式を検討する
* patch subsetの方式でCJKフォントでは90%以上のデータ量削減が行えたので、利用率向上に資する可能性がある
* PFE有効のフォントの利用にはCSSへの変更が必要となるので、新しいフォーマットタイプの割り当てが必要かもしれない


### Incremental font transferの提案仕様

2021/3/22版ではpatch subsetの方式(Patch Based Incremental Transfer)のデータ型定義の途中までしかない。
転送方式などについてはなにもまだ掛れていない。データのEncodingにはCBOR (RFC #8949)を利用する。
