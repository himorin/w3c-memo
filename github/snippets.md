## PR

PR from forked personal repo
```
git remote add pers-fork git@github.com:himorin/immersive-web-administrivia
git checkout -b himorin-issue
git push --set-upstream pers-fork himorin-issue
```

## TravisCI Key

```
ssh-keygen -t ed25519 -P "" -f REPO
setenv openssl_iv `cat /dev/urandom | head -c 16 | od -An -tx1 | tr -d "\n "`
setenv openssl_key `cat /dev/urandom | head -c 32 | od -An -tx1 | tr -d "\n "`
openssl aes-256-cbc -K $openssl_key -iv $openssl_iv -in REPO -out REPO.enc -e
env | grep openssl
```

- REPO.enc to store in github repository as `deploy_key.enc` or something
- REPO.pub to put into setting, Deploy Key
- `openssl_iv` and `openssl_key` to TravisCI environment

