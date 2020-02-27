#! /usr/bin/env python3

import utils
import i18n
import sys

LABEL_TRACK = 'i18n-tracker'

def printIssues(label, issues):
    print("\n{}".format(label))
    for issue in issues:
        print("{}\n  {}\n  {}".format(issue['title'], issue['html_url'], issue['tracker_issue']['html_url']))


def run():
    objConf = utils.ITCConfig()
    objConf.Load()
    objLI18n = i18n.ListI18n()
    objLI18n.LoadList()

    res = utils.GetListIssues(sys.argv[1], objConf.GetGHKey(), LABEL_TRACK)
    tracker_url = objLI18n.GetAllTrackers()
    track_state = objLI18n.GetAllTrackState()
    tracker_issue = objLI18n.GetAllTrackerIssues()

    # list of target issues (not ID)
    check_ok_open = [] # both open, no 'close?' label
    check_ok_close = [] # target closed, has 'close?' label
    check_ok_closed = [] # both closed
    check_close_missing = [] # target closed, no 'close?' label
    check_wrong_close = [] # target open, has 'close?' label
    check_wrong_closed = [] # target open, tracker closed
    check_missing_open = [] # tracker missing and target open
    check_missing_closed = [] # tracker missing and target closed

    for issue in res:
        curl = issue['html_url']
        if curl in tracker_url:
            ctid = tracker_url[curl]
            ctissue = tracker_issue[ctid]
            issue['tracker_id'] = ctid
            issue['tracker_issue'] = ctissue
            if issue['state'] == 'open':
                if ctissue['track_status'] == 'open':
                    check_ok_open.append(issue)
                elif ctissue['track_status'] == 'close?':
                    check_wrong_close.append(issue)
                else:
                    check_wrong_closed.append(issue)
            else:
                if ctissue['track_status'] == 'open':
                    check_close_missing.append(issue)
                elif ctissue['track_status'] == 'close?':
                    check_ok_close.append(issue)
                else:
                    check_ok_closed.append(issue)
        else:
            if issue['state'] == 'open':
                check_missing_open.append(issue)
            else:
                check_missing_closed.append(issue)

    print("Results:")
    printIssues("OK: both open, no close? label", check_ok_open)
    printIssues("OK: target closed, has close? label", check_ok_close)
    printIssues("OK: both closed", check_ok_closed)
    print("\nOK: tracker missing, already closed")
    for issue in check_missing_closed:
        print("{}\n  {}".format(issue['title'], issue['html_url']))
    printIssues("NG: target closed, missing close? label", check_close_missing)
    printIssues("NG: target open, has close? label", check_wrong_close)
    printIssues("NG: target open, tracker closed", check_wrong_closed)
    print("\nNG: tracker missing")
    for issue in check_missing_open:
        print("{}\n  {}".format(issue['title'], issue['html_url']))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Usage <script> <target repo>")
    run()

