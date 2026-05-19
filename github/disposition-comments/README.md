# disposition-comments

scripts for generating static archive from github discussions.

## configuration and run

* call APIs via pygithub library
* `config.json` is loaded by script for runtime configuration
  * use skelton as `config.json.skel`
  * `gh_pat`: GitHub access token (personal access token), to extend limit of GitHub API limit
  * `hlevel`: heading level for issue top and to separate comments (one level down)
* `generate_comments.py`: generate html archive from single issue
  * usage: `<script> (file) <github url> (<from date>)`
    * if `file` is inserted, load `<github url>` from specified file, one URL per line
    * if `<from date>` (in YYYYMMDD) is specified, only comments after specified date (in UTC) will be output
  * output html, via markdown conversion API called per each comment
    * not taking way first to composite all comments w/ separation by `###` and to convert, difficulty to seek separation point when comment has heading markup
  * output content - to file
    * name of file : `<org>-<repo>-<issue id>(-from-<from date>).html`
      * output file will be newly created (or overrided)
    * heading: hX including repository ID with link
    * issue metadata
    * comments
      * heading: h(X+1) "Comment by `name`"w/link (@`login`w/link) at `date (in UTC)`w/time (followed by edit history)
      * content: converted html, wrapped by blockquote


## features not confirmed to work, and known issue

* `generate_comments.py`
  * long thread, with over 100 comments
  * whether can run with PR, discussion, etc.

