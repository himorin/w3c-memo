# Notes on i18n-test and web-platform-test

Random memo on writting or modifying files for 
[i18n-tests](https://github.com/w3c/i18n-tests/)
and 
[wpt - web-platform-test](https://github.com/web-platform-tests/wpt)

## lint tool

Run as `<path_to>/wpt lint --repo-root <repo_root> --json ./<target>`.

* target need to be specified per file, not directory
* at repo root, need to have 'lint.whitelist' file (blank file is ok)


* Possible outputs
  * [List of errors](https://web-platform-tests.org/writing-tests/lint-tool.html)
  * if 'font' is added for [CSS metadata](https://web-platform-tests.org/writing-tests/css-metadata.html), test will be parsed as 'Manual'
* Last part in filename is test type, [as listed](https://web-platform-tests.org/writing-tests/file-names.html)
  * Reference target is named as '-ref.html'


