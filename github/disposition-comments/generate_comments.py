#! /usr/bin/env python3

import base_routines
import json
import sys
import datetime

DEF_ISSUE_HEAD = "<h[HL]>Comments provided to [ICAT] <a href=\"[IURL]\">[IREPO] #[IID]: [ITITLE]</a></h[HL]>"
DEF_ISSUE_META = "<ul><li>Status: [ISTAT]</li><li>Created: <time datetime=\"[ICREDT]\">[ICREDAY]</time></li>[ICLOSE][IPRMRG][IPRSTAT]</ul>"
DEF_ISSUE_CLOSE = "<li>Closed: <time datetime=\"[ICLOSEDT]\">[ICLOSEDAY]</time> [ICLOSEBY]</li>"
DEF_ISSUE_CLOSE_NOT = "<li>Not yet closed</li>" 
DEF_ISSUE_MERGE = "<li>PR Merged: <time datetime=\"[IPRMRGDT]\">[IPRMRGDAY]</time> [IPRMRGBY]</li>"
DEF_ISSUE_MERGE_NOT = "<li>PR not yet merged</li>"
DEF_ISSUE_END_BY = "by [IENDBYNAME] (@<a href=\"[IENDBYURL]\">[IENDBY]</a>)"
DEF_PR_RSTAT = "<li>Reviews provided:<ul>[PRSTATLIST]</ul></li>"
DEF_PR_DATE = "<li>[PRBYNAME] (@<a href=\"[PRBYURL]\">[PRBY]</a>) at <time datetime=\"[PRBYDT]\">[PRBYDAY]</time></li>"
DEF_COMMENT_INIT = "<section>\n\n<h[HL]><a href=\"[CURL]\">Initial comment by [CNAME]</a> (<a href=\"[CLOGINURL]\">@[CLOGIN]</a>) at <time datetime=\"[CDATEDT]\">[CDATE]</time> [CEDITED]</h[HL]>"
DEF_COMMENT_HEAD = "<section>\n\n<h[HL]><a href=\"[CURL]\">Comment by [CNAME]</a> (<a href=\"[CLOGINURL]\">@[CLOGIN]</a>) at <time datetime=\"[CDATEDT]\">[CDATE]</time> [CEDITED]</h[HL]>"
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
  c_dat['CDATEDT'] = c_obj.created_at.isoformat()
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

def PrintComments(c_comments, c_from, c_fh, c_cnf, c_gh, c_repo):
  for c_comment in c_comments:
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

def PrintIssue(c_cnf, c_gh, url, fromdate = None):
  c_icfg = url.split('/') # 3:org, 4:repo, 6:id
  c_repo_name = "%s/%s" % (c_icfg[3], c_icfg[4])
  c_repo = c_gh.get_repo(c_repo_name)
  c_pull = False
  if c_icfg[5] == 'pull':
    c_pull = True
    c_issue = c_repo.get_pull(number = int(c_icfg[6]))
  else:
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
  c_dat['ICAT'] = "PR" if c_pull == True else "issue"
  c_dat['IURL'] = c_issue.html_url
  c_dat['IREPO'] = c_repo_name
  c_dat['IID'] = str(c_issue.number)
  c_dat['ITITLE'] = c_issue.title
  c_dat['ISTAT'] = c_issue.state
  c_dat['ICREDT'] = c_issue.created_at.isoformat()
  c_dat['ICREDAY'] = c_issue.created_at.strftime('%Y-%m-%d')
  if c_issue.closed_at is not None:
    c_dat['ICLOSE'] = DEF_ISSUE_CLOSE
    c_dat['ICLOSEDT'] = c_issue.closed_at.isoformat()
    c_dat['ICLOSEDAY'] = c_issue.closed_at.strftime('%Y-%m-%d')
    if c_pull == True:
      c_dat['ICLOSEBY'] = ""
    else:
      c_dat['ICLOSEBY'] = DEF_ISSUE_END_BY
      c_dat['IENDBYNAME'] = c_issue.closed_by.name
      c_dat['IENDBY'] = c_issue.closed_by.login
      c_dat['IENDBYURL'] = c_issue.closed_by.html_url
  else:
    c_dat['ICLOSE'] = DEF_ISSUE_CLOSE_NOT
  if c_pull == True:
    if c_issue.merged:
      c_dat['IPRMRG'] = DEF_ISSUE_MERGE
      c_dat['IPRMRGDT'] = c_issue.merged_at.isoformat()
      c_dat['IPRMRGDAY'] = c_issue.merged_at.strftime('%Y-%m-%d')
      c_dat['IPRMRGBY'] = DEF_ISSUE_END_BY
      c_dat['IENDBYNAME'] = c_issue.merged_by.name
      c_dat['IENDBY'] = c_issue.merged_by.login
      c_dat['IENDBYURL'] = c_issue.merged_by.html_url
    else:
      c_dat['IPRMRG'] = DEF_ISSUE_MERGE_NOT
    # review status
    c_dat['IPRSTAT'] = DEF_PR_RSTAT
    c_dat['PRSTATLIST'] = ""
    c_prr_status = {}
    for c_prr in c_issue.get_reviews():
      if c_prr.state == "COMMENTED":
        continue
      if c_prr.state not in c_prr_status:
        c_prr_status[c_prr.state] = ""
      c_prr_status[c_prr.state] += base_routines.ReplaceBracket(DEF_PR_DATE, {
        'PRBYNAME': c_prr.user.name,
        'PRBY': c_prr.user.login,
        'PRBYURL': c_prr.user.html_url,
        'PRBYDT': c_prr.submitted_at.isoformat(),
        'PRBYDAY': c_prr.submitted_at.strftime('%Y-%m-%d')
      })
    for c_prr_stat in c_prr_status:
      c_dat['PRSTATLIST'] += "<li>%s<ul>%s</ul></li>" % (c_prr_stat, c_prr_status[c_prr_stat])
  else:
    c_dat['IPRMRG'] = ''
    c_dat['IPRSTAT'] = ''
  print(base_routines.ReplaceBracket(DEF_ISSUE_HEAD, c_dat), file = c_fh)
  print(base_routines.ReplaceBracket(DEF_ISSUE_META, c_dat), file = c_fh)

  c_dat['HL'] = str(c_cnf['hlevel'])
  c_dat = PackCommentUpdate(c_issue, c_dat)
  c_dat['COMMENT'] = c_gh.render_markdown(text = c_issue.body, context = c_repo)
  print(base_routines.ReplaceBracket(DEF_COMMENT_INIT, c_dat), file = c_fh)
  print(base_routines.ReplaceBracket(DEF_COMMENT_BODY, c_dat), file = c_fh)
  print(DEF_COMMENT_CLOS, file = c_fh)

# XXX: switch to use since: than filtering after comments requested
#  c_dat = c_issue.get_comments().totalCount
#  c_dat = c_issue.get_comments().get_page(0)
  if c_pull == True:
    print("\n\n<!-- get_issue_comments -->\n\n", file = c_fh)
    PrintComments(c_issue.get_issue_comments(), c_from, c_fh, c_cnf, c_gh, c_repo)
    print("\n\n<!-- get_review_comments -->\n\n", file = c_fh)
    PrintComments(c_issue.get_review_comments(), c_from, c_fh, c_cnf, c_gh, c_repo)
  else:
    PrintComments(c_issue.get_comments(), c_from, c_fh, c_cnf, c_gh, c_repo)

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

