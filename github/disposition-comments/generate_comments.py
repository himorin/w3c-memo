#! /usr/bin/env python3

import base_routines
import json
import sys

DEF_ISSUE_HEAD = "<h[HL]>Comments provided to issue <a href=\"[IURL]\">[IREPO] #[IID]: [ITITLE]</a></h[HL]>"
DEF_ISSUE_META = "<ul><li>Status: [ISTAT]</li><li>Created: <time datetime=\"[ICREDT]\">[ICREDAY]</time></li></ul>"
DEF_COMMENT_INIT = "<h[HL]><a href=\"[CURL]\">Initial comment by [CNAME]</a> (<a href=\"[CLOGINURL]\">@[CLOGIN]</a>) at [CDATE] [CEDITED]</h[HL]>"
DEF_COMMENT_HEAD = "<h[HL]><a href=\"[CURL]\">Comment by [CNAME]</a> (<a href=\"[CLOGINURL]\">@[CLOGIN]</a>) at [CDATE] [CEDITED]</h[HL]>"
DEF_COMMENT_EDIT = "(edited in <time datetime=\"[CEDITEDDT]\">[CEDITEDDAY]</time>)"
DEF_COMMENT_BODY = "<blockquote>[COMMENT]</blockquote>"

def PackCommentUpdate(c_obj, c_dat):
  c_dat['CURL'] = c_obj.html_url
  c_user = base_routines.GetUser(c_obj.user.login)
  c_dat['CNAME'] = c_user.name
  c_dat['CLOGIN'] = c_user.login
  c_dat['CLOGINURL'] = c_user.html_url
  c_dat['CDATE'] = c_obj.created_at.strftime('%Y-%m-%d')
  if c_obj.created_at == c_obj.updated_at:
    c_dat['CEDITED'] = ''
  elif c_obj.created_at.date() == c_obj.updated_at.date():
    c_dat['CEDITED'] = DEF_COMMENT_EDIT
    c_dat['CEDITEDDAY'] = 'the same day'
    c_dat['CEDITEDDT'] = c_obj.updated_at.isoformat()
  else:
    c_dat['CEDITED'] = DEF_COMMENT_EDIT
    c_dat['CEDITEDDAY'] = c_obj.updated_at.strftime('%Y-%m-%d')
    c_dat['CEDITEDDT'] = c_obj.updated_at.isoformat()
  return c_dat

def PrintIssue(c_cnf, c_gh, url):
  c_icfg = url.split('/') # 3:org, 4:repo, 6:id
  c_repo_name = "%s/%s" % (c_icfg[3], c_icfg[4])
  c_repo = c_gh.get_repo(c_repo_name)
  c_issue = c_repo.get_issue(number = int(c_icfg[6]))

  print("\n<!--\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n-->\n\n" % (c_issue.html_url, c_issue.number, c_issue.state, c_issue.title, c_issue.user.login, c_issue.created_at, c_issue.updated_at, c_issue.closed_at))
  c_dat = {}
  c_dat['HL'] = str(c_cnf['hlevel'] - 1)
  c_dat['IURL'] = c_issue.html_url
  c_dat['IREPO'] = c_repo_name
  c_dat['IID'] = str(c_issue.number)
  c_dat['ITITLE'] = c_issue.title
  c_dat['ISTAT'] = c_issue.state
  c_dat['ICREDT'] = c_issue.created_at.isoformat()
  c_dat['ICREDAY'] = c_issue.created_at.strftime('%Y-%m-%d')
  print(base_routines.ReplaceBracket(DEF_ISSUE_HEAD, c_dat))
  print(base_routines.ReplaceBracket(DEF_ISSUE_META, c_dat))

  c_dat = PackCommentUpdate(c_issue, c_dat)
  c_dat['COMMENT'] = c_gh.render_markdown(text = c_issue.body, context = c_repo)
  print(base_routines.ReplaceBracket(DEF_COMMENT_INIT, c_dat))
  print(base_routines.ReplaceBracket(DEF_COMMENT_BODY, c_dat))

#  c_dat = c_issue.get_comments().totalCount
#  c_dat = c_issue.get_comments().get_page(0)
  for c_comment in c_issue.get_comments():
    print("\n\n<!--\n%s\n%s\n%s\n%s\n-->\n" % (c_comment.id, c_comment.user.login, c_comment.created_at, c_comment.updated_at))
    c_dat = {}
    c_dat['HL'] = str(c_cnf['hlevel'])
    c_dat = PackCommentUpdate(c_comment, c_dat)
    c_dat['COMMENT'] = c_gh.render_markdown(text = c_comment.body, context = c_repo)
    print(base_routines.ReplaceBracket(DEF_COMMENT_HEAD, c_dat))
    print(base_routines.ReplaceBracket(DEF_COMMENT_BODY, c_dat))

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Invalid parameter: command <issue_url> / https://github.com/<org>/<repo>/issues/<id>")
  c_cnf = base_routines.LoadConfig()
  c_gh = base_routines.AuthGhapi(c_cnf['gh_pat'])
  if sys.argv[1] == 'file':
    with open(sys.argv[2], 'r') as flist:
      for c_url in flist.readlines():
        PrintIssue(c_cnf, c_gh, c_url.strip())
  else:
    PrintIssue(c_cnf, c_gh, sys.argv[1])

# no cache save, consider json dump for object of pygithub
#  base_routines.SaveCache()

