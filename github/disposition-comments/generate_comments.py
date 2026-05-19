#! /usr/bin/env python3

import base_routines
import json
import sys
import datetime

DEF_ISSUE_HEAD = "<h[HL]>Comments provided to issue <a href=\"[IURL]\">[IREPO] #[IID]: [ITITLE]</a></h[HL]>"
DEF_ISSUE_META = "<ul><li>Status: [ISTAT]</li><li>Created: <time datetime=\"[ICREDT]\">[ICREDAY]</time></li></ul>"
DEF_COMMENT_INIT = "<section>\n\n<h[HL]><a href=\"[CURL]\">Initial comment by [CNAME]</a> (<a href=\"[CLOGINURL]\">@[CLOGIN]</a>) at [CDATE] [CEDITED]</h[HL]>"
DEF_COMMENT_HEAD = "<section>\n\n<h[HL]><a href=\"[CURL]\">Comment by [CNAME]</a> (<a href=\"[CLOGINURL]\">@[CLOGIN]</a>) at [CDATE] [CEDITED]</h[HL]>"
DEF_COMMENT_EDIT = "(edited in <time datetime=\"[CEDITEDDT]\">[CEDITEDDAY]</time>)"
DEF_COMMENT_BODY = "<blockquote>[COMMENT]</blockquote>"
DEF_COMMENT_CLOS = "\n</section>\n\n"

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

def PrintIssue(c_cnf, c_gh, url, fromdate = None):
  c_icfg = url.split('/') # 3:org, 4:repo, 6:id
  c_repo_name = "%s/%s" % (c_icfg[3], c_icfg[4])
  c_repo = c_gh.get_repo(c_repo_name)
  c_issue = c_repo.get_issue(number = int(c_icfg[6]))
  c_of = "%s-%s-%s" % (c_icfg[3], c_icfg[4], c_icfg[6])
  c_from = None
  if fromdate is not None:
    c_of += "-%s" % fromdate
    c_from = datetime.datetime(int(fromdate[0:4]), int(fromdate[4:6]), int(fromdate[6:8])).replace(tzinfo = datetime.timezone.utc)
  c_of += ".html"

  try:
    c_fh = open(c_of, 'w')
  except IOError as e:
    print("Could not open file to write: %s" % (c_of))
    return None

  print("\n<!--\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n-->\n\n" % (c_issue.html_url, c_issue.number, c_issue.state, c_issue.title, c_issue.user.login, c_issue.created_at, c_issue.updated_at, c_issue.closed_at), file = c_fh)
  c_dat = {}
  c_dat['HL'] = str(c_cnf['hlevel'] - 1)
  c_dat['IURL'] = c_issue.html_url
  c_dat['IREPO'] = c_repo_name
  c_dat['IID'] = str(c_issue.number)
  c_dat['ITITLE'] = c_issue.title
  c_dat['ISTAT'] = c_issue.state
  c_dat['ICREDT'] = c_issue.created_at.isoformat()
  c_dat['ICREDAY'] = c_issue.created_at.strftime('%Y-%m-%d')
  print(base_routines.ReplaceBracket(DEF_ISSUE_HEAD, c_dat), file = c_fh)
  print(base_routines.ReplaceBracket(DEF_ISSUE_META, c_dat), file = c_fh)

  c_dat['HL'] = str(c_cnf['hlevel'])
  c_dat = PackCommentUpdate(c_issue, c_dat)
  c_dat['COMMENT'] = c_gh.render_markdown(text = c_issue.body, context = c_repo)
  print(base_routines.ReplaceBracket(DEF_COMMENT_INIT, c_dat), file = c_fh)
  print(base_routines.ReplaceBracket(DEF_COMMENT_BODY, c_dat), file = c_fh)
  print(DEF_COMMENT_CLOS, file = c_fh)

#  c_dat = c_issue.get_comments().totalCount
#  c_dat = c_issue.get_comments().get_page(0)
  for c_comment in c_issue.get_comments():
    if (c_from is not None) and (c_comment.updated_at < c_from):
      continue
    print("\n\n<!--\n%s\n%s\n%s\n%s\n-->\n" % (c_comment.id, c_comment.user.login, c_comment.created_at, c_comment.updated_at), file = c_fh)
    c_dat = {}
    c_dat['HL'] = str(c_cnf['hlevel'])
    c_dat = PackCommentUpdate(c_comment, c_dat)
    c_dat['COMMENT'] = c_gh.render_markdown(text = c_comment.body, context = c_repo)
    print(base_routines.ReplaceBracket(DEF_COMMENT_HEAD, c_dat), file = c_fh)
    print(base_routines.ReplaceBracket(DEF_COMMENT_BODY, c_dat), file = c_fh)
    print(DEF_COMMENT_CLOS, file = c_fh)

  c_fh.close()

if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Invalid parameter: command (file) <issue_url> (from_date) / URL = https://github.com/<org>/<repo>/issues/<id>")
  c_cnf = base_routines.LoadConfig()
  c_gh = base_routines.AuthGhapi(c_cnf['gh_pat'])
  c_from = None
  if sys.argv[1] == 'file':
    if len(sys.argv) >= 4:
      c_from = sys.argv[3]
    with open(sys.argv[2], 'r') as flist:
      for c_url in flist.readlines():
        PrintIssue(c_cnf, c_gh, c_url.strip(), c_from)
  else:
    if len(sys.argv) >= 3:
      c_from = sys.argv[2]
    PrintIssue(c_cnf, c_gh, sys.argv[1], c_from)

# no cache save, consider json dump for object of pygithub
#  base_routines.SaveCache()

