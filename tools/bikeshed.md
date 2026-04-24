# memo related to bikeshed

## install

* requestsなどのpythonモジュールの新しいバージョン要求の都合でstable debianに入らないことが多い
* debian testingのVMを立ててそこに入れる
* apt: python3-pip, git
* install
  * `sudo pip3 install --break-system-package --root-user-action ignore -e .`
  * `sudo bikeshed update`

### related path

* `/usr/local/bin/bikeshed`
* `/usr/local/lib/pythonXXX/dist-packages/bikeshed-XXX.dist-info/`
  * `/usr/local/lib/pythonXXX/dist-packages/bikeshed-XXX.dist-info/direct_url.json`: urlに実行するファイルのディレクトリ
  * 基本的にはインストールに使ったgit cloneの場所になる

## boilerplate関係

* `bikeshed update`で更新されるboilerplateは`<git root>/bikeshed/spec-data/boilerplate/`に落ちる
