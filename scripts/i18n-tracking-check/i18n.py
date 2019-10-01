#! /usr/bin/env python3

import utils
import re

I18N_TRACKER = 'w3c/i18n-activity'
I18N_TARGET = '§ '

class ListI18n(object):

    def __init__(self):
        self.re_target = None
        self.list_tracker = {}  # track url to ID
        self.list_issues = {}   # ID to issue detail
        self.list_labels = {}   # label to list of ID

    def LoadList(self):
        self.config = utils.ITCConfig()
        self.config.Load()
        self.ghkey = self.config.GetGHKey()

        self.listRaw = utils.GetListIssues(I18N_TRACKER, self.ghkey)
        self._buildTracking()

    def _buildTracking(self):
        for val in self.listRaw:
            track = self._getTrackTarget(val['body'])
            if track is not None:
                self.list_tracker[track] = val['number']
                val['track'] = track
            for clbl in val['labels']:
                if clbl['name'] in self.list_labels:
                    self.list_labels[clbl['name']].append(val['number'])
                else:
                    self.list_labels[clbl['name']] = [val['number']]
            self.list_issues[val['number']] = val

    def _getTrackTarget(self, comment):
        if self.re_target is None:
            self.re_target = re.compile("^{}(https.+)$".format(I18N_TARGET), re.MULTILINE)
        re_match = self.re_target.search(comment)
        if re_match is not None:
            return re_match.group(1)
        return None

    def GetAllTrackers(self):
        return self.list_tracker

    def GetTrackerForUrl(self, url):
        if url in self.list_tracker:
            return self.list_issues[self.list_tracker[url]]
        return None

def selftest():
    objLI18n = ListI18n()
    objLI18n.LoadList()
    trackers = objLI18n.GetAllTrackers()
    for val in trackers:
        print("ID {} to {}".format(trackers[val], val))

if __name__ == "__main__":
    selftest()

