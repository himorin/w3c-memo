#! /usr/bin/env python3

import sys
import json
import os
import urllib.request

CONF_NAME = 'config.json'
GHAPI_HEAD = 'https://api.github.com/repos/'

class ITCConfig(object):

    def Load(self):
        try:
            fjson = open(CONF_NAME, 'r')
        except IOError as e:
            raise Exception("File '{}' open error: {}".format(CONF_NAME, e))
        try:
            self.config = json.load(fjson)
        except:
            raise Exception("json format parse error for '{}'".format(CONF_NAME))

    def GetConfig(self, name):
        if self.config is None:
            raise Exception("Config not loaded")
        if not name in self.config:
            raise Exception("No such key '{}'".format(name))
        return self.config[name]

#def GetListIssues(repo, apikey, label):

    # call _getAPIIssues


'''
    Access github api for getting 100 response of target

    repo: name as :org:/:repo:
    apikey: github api key
    page: start page count of search result (1 will be 0 to 99)
    label: target label for filtering if any
'''
def _getAPIIssues(repo, apikey, page, label):
    ghurl = "{}{}/issues?per_page=100&".format(GHAPI_HEAD, repo)
    if page is not None:
        ghurl = "{}page={}&".format(ghurl, page)
    if label is not None:
        ghurl = "{}labels={}&".format(ghurl, label)

    try:
        req = urllib.request.Request(ghurl)
        req.add_header('token', apikey)
    except Exception as e:
        raise Exception("urllib request build error: {}".format(e))
    try:
        res = urllib.request.urlopen(req)
    except HTTPError as e:
        raise Exception("Server error: {}".format(e.code))
    except URLError as e:
        raise Exception("Failed to reach URL '{}': {}".format(ghurl, e.reason))

    contents = res.read().decode('utf-8')
    return contents

def selftest():
    objConfig = ITCConfig()
    objConfig.Load()
    apikey = objConfig.GetConfig('github_key')
    print("Configured GitHub API key: '{}'".format(apikey))
    if len(sys.argv) > 1:
        res = _getAPIIssues(sys.argv[1], apikey, 1, 'i18n-tracking')
        rjson = json.loads(res)
        print("Loaded i18n-tracking issues count = {:d}".format(len(rjson)))


if __name__ == "__main__":
    selftest()

