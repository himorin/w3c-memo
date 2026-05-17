#! /usr/bin/env python3

import base_routines
import json
import sys

DEF_COMMENT_HEAD = "<h[HL]><a href=\"[CURL]\">Comment by [CNAME]</a> (<a href=\"[CLOGINURL]\">@[CLOGIN]</a>) at [CDATE] [CEDITED]</h[HL]>"
DEF_COMMENT_EDIT = "(edited in <time datetime=\"[CEDITEDDT]\">[CEDITEDDAY]</time>)"
DEF_COMMENT_BODY = "<blockquote>[COMMENT]</blockquote>"


if __name__ == "__main__":
  if len(sys.argv) != 2:
    raise Exception("Invalid parameter: command <issue_url> / https://github.com/<org>/<repo>/issues/<id>")
  c_cnf = base_routines.LoadConfig()
  c_gh = base_routines.AuthGhapi(c_cnf['gh_pat'])
  c_icfg = sys.argv[1].split('/') # 3:org, 4:repo, 6:id
  c_repo = c_gh.get_repo("%s/%s" % (c_icfg[3], c_icfg[4]))
  c_issue = c_repo.get_issue(number = int(c_icfg[6]))

#  c_dat = c_issue.get_comments().totalCount
#  c_dat = c_issue.get_comments().get_page(0)
  for c_comment in c_issue.get_comments():
    print("\n----\n")
    c_user = base_routines.GetUser(c_comment.user.login)
    print("<!-- %s\n%s\n%s\n%s\n%s -->" % (c_comment.id, c_user.name, c_user.login, c_comment.created_at, c_comment.updated_at))
    c_dat = {}
    c_dat['HL'] = str(c_cnf['hlevel'])
    c_dat['CURL'] = c_comment.html_url
    c_dat['CNAME'] = c_user.name
    c_dat['CLOGIN'] = c_user.login
    c_dat['CLOGINURL'] = c_user.url
    c_dat['CDATE'] = c_comment.created_at.strftime('%Y-%m-%d')
    if c_comment.created_at == c_comment.updated_at:
      c_dat['CEDITED'] = ''
    elif c_comment.created_at.date() == c_comment.updated_at.date():
      c_dat['CEDITED'] = DEF_COMMENT_EDIT
      c_dat['CEDITEDDAY'] = 'the same day'
      c_dat['CEDITEDDT'] = c_comment.updated_at.isoformat()
    else:
      c_dat['CEDITED'] = DEF_COMMENT_EDIT
      c_dat['CEDITEDDAY'] = c_comment.updated_at.strftime('%Y-%m-%d')
      c_dat['CEDITEDDT'] = c_comment.updated_at.isoformat()
    c_dat['COMMENT'] = c_gh.render_markdown(text = c_comment.body, context = c_repo)
    print(base_routines.ReplaceBracket(DEF_COMMENT_HEAD, c_dat))
    print(base_routines.ReplaceBracket(DEF_COMMENT_BODY, c_dat))

# no cache save, consider json dump for object of pygithub
#  base_routines.SaveCache()

#  print(json.dumps(c_dat))
