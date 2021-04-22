# WebFont関係まとめ

## 関連仕様、ノート類

* WOFF関係 (Web Open Font Format; [WebFonts WG](https://www.w3.org/Fonts/WG/))
  * [WOFF2](https://www.w3.org/TR/2018/REC-WOFF2-20180301/) (2018/03/01 REC)
    * [WOFF2 Evaluation Report](http://www.w3.org/TR/2016/NOTE-WOFF20ER-20160315/) (2016/03/15 WG-NOTE)
  * [WOFF1](https://www.w3.org/TR/2012/REC-WOFF-20121213/) (2012/12/13 REC)
  * [MicroType Express (MTX) Font Format](https://www.w3.org/Submission/2008/SUBM-MTX-20080305/) (2008/03/05 Monotype Imaging SUBM)
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
* フォントデータ本体は圧縮形式でファイル内に格納される、WOFF2ではBrotliの単独ストリーム、WOFF1ではzlib/compress2を利用

### WOFF2ファイル構成

概要

* 一番最後のブロックを除き、ブロックごとに4byteでパディングされる
* (数値)データ型として、UInt8, Int16, UInt16, 255UInt16, UIntBase128が定義されている
  * 255UInt16: UInt16の1-3バイトへのマッピング、0-252は1バイト、762以上は3バイトになる
  * UIntBase128: 32bit非負数値の1-5バイトへのマッピング、元数値の7bitごとの切り出しで最後のバイトで先頭ビットがたつ

ファイルの構成ブロックは以下、リストの並び順にファイルの中に並ぶ

* WOFF2Header : 全体についてのデータを格納するヘッダ、圧縮時・解凍後のデータサイズやデータブロックまでのオフセット
  * UInt32 signature: `wOF2`
  * UInt32 flavor: sfnt version
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
* TableDirectory : WOFF2Header.numTablesの数のテーブルのエントリ、各エントリは可変長なので読まないとサイズは決まらない
  * 各エントリは以下の４つの値の配列、圧縮領域に格納されている順に並べられる
    * UInt8 flags: `0..5`の6bitがテーブル定義(`63`以外は定義値、`63`は次の値を利用)、`6..7`の2bitがプリプロセスでのtransformationのバージョン番号`0-3`を示す
    * UInt32 tag: （オプション）`flags=63`の時のテーブル名４文字、後ろ空白パディング
    * UIntBase128 origLength: 非圧縮時のサイズ
    * UIntBase128 transformLength: transform適用後のサイズ（null transformationでない場合、また処理によっては複数の結果になる場合があるので必ずしも正しくならない）
  * 未定義のtransformationのバージョンが指定されたものはテーブルごと拒否
* CollectionDirectory
* CompressedFontData
* ExtendedMetadata
  * 圧縮されたXML (UTF-8)のデータ、vendor, copyrightなどのデータを入れられる部分
  * XMLの形式やエレメント定義はWOFF1/WOFF2で変化なし
* PrivateData
  * 非定型のベンダー固有データ領域

テーブル・フォントデータの並び順について（詳細は[section 5.5](https://www.w3.org/TR/WOFF2/#table_order)に）

* OFFではテーブルの並び順を`ascending alphabetical order`としているが、WOFFでは処理の高速化のために制限をつけている
* `glyf`と`loca`は常にペアでこの順に配置されている必要がある。reverse transformが`glyf`に設定されている時に`loca`が必要なため。
* `glyf`と`loca`はWOFFが一つのフォントセットのみの場合は間に別なものが入っていいが、フォントコレクションの場合は必ず対応関係の`glyf`と`loca`は連続しなければならない


### Brotli

* LZ77とハフマン符号化ベースの圧縮アルゴリズム
* 120KiB/13000 words程度のコーパスから生成された事前定義辞書を利用
