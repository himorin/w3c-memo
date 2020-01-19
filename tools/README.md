List of tools used for W3C works

## Daily use tools

* [github-notify-ml-config](https://github.com/w3c/github-notify-ml-config) : configuration repository for [github-notify-ml](https://github.com/dontcallmedom/github-notify-ml/)
* [pr-preview](https://github.com/tobie/pr-preview): preview tool for non merged gh-pages PR branch

## Strategic documents

* [modern-tooling](https://github.com/w3c/modern-tooling) : modern tooling task force notes

## W3C Team tools

* [Process transition request](https://github.com/w3c/transitions/)
  * links on readme will make skelton per each type of requests
* [Repository manager for IPR (Ash-Nazg)](https://github.com/w3c/ash-nazg/)
  * create new repository with a set of required files, or import to tool
  * check PR is made by github account which has proper IPR statement (via W3C user repository)
  * [Live site at labs.w3.org](https://labs.w3.org/hatchery/repo-manager/)
  * [overview note](https://w3c.github.io/repo-management.html)
  * run `ulimit -n 2560` (bash) or `limit descriptors 2560` (tcsh) before `npm install -d`
    * once failed `node_modules` created, seems need to delete whole...
* [echidna](https://github.com/w3c/echidna/wiki)
  * dry run: `curl 'https://labs.w3.org/echidna/api/request' --data 'url=<W3CTRMANIFEST>&decision=<decision>&token=<token>' -d 'dry-run=true'`
  + from tar archive: `curl 'https://labs.w3.org/echidna/api/request' --user '<username>:<password>' -F 'dry-run=true' -F "tar=@/some/path/spec.tar" -F "decision=<decisionUrl>"`
  * check echidna result: `https://labs.w3.org/echidna/api/status?id=<uuid>`
  * [echidna token](https://www.w3.org/Web/publications/register), can check existing token (as error message for dup)
  * pubrules validate: `https://www.w3.org/pubrules/api/validate?url=<url>&profile=WD`
    * [Error messages](https://github.com/w3c/specberus/blob/master/lib/l10n-en_GB.js#L45)
  * [link checker](http://validator.w3.org/checklink)

## Working repositories

* [Draft charters for public review (charter-drafts)](https://github.com/w3c/charter-drafts)
  * drafts to be checked and reviewed in public
  * need to be in w3.org date-space for AC review etc. (as in [note](https://github.com/w3c/charter-drafts#notes-for-w3c-team))

## Documentating

* [ReSpec](https://github.com/w3c/respec) JS library to be included in any published documents online
  * [very basic guide](https://github.com/w3c/respec/wiki/ReSpec-Editor's-Guide)
* [tr-design](https://github.com/w3c/tr-design) CSS improvement project on ones used for TR

