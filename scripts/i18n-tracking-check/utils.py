#! /usr/bin/env python3

import sys
import json
import os
import urllib.request
import re

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


'''
    List all issues in condition, calling API multiple times
    Wrapper and handling multiple calls to _getAPIIssues

    repo: name as :org:/:repo:
    apikey: github api key
    label: target label for filtering if any

    return: array of issues
'''
def GetListIssues(repo, apikey, label):
    id_last = 0
    list_all = []
    # simple first call
    api_res = _getAPIIssues(repo, apikey, 1, label)
    list_all.extend(api_res['data'])
    if api_res['pages'] is not None:
        if 'last' in api_res['pages']:
            id_last = api_res['pages']['last']
    # crawl all to last
    for pid in range(2, int(id_last) + 1):
        api_res = _getAPIIssues(repo, apikey, pid, label)
        list_all.extend(api_res['data'])
    return list_all


'''
    Access github api for getting 100 response of target

    repo: name as :org:/:repo:
    apikey: github api key
    page: start page count of search result (1 will be 0 to 99)
    label: target label for filtering if any

    return: dict { 'data': [], 'pages': {xxx} }
      pages: generated from 'Link' header, rel: page=X
        note, if no multipage results, no data in pages
        for now, list all status both close and open
'''
def _getAPIIssues(repo, apikey, page, label):
    ghurl = "{}{}/issues?per_page=100&state=all&".format(GHAPI_HEAD, repo)
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
    res_link = res.getheader('Link')
    list_page = None
    if res_link is not None:
        list_page = {}
        res_pages = res_link.split(',')
        for val in res_pages:
            re_res = re.search(r"&page=(\d+)>; rel=\"(\w+)\"", val)
            if re_res is not None:
                list_page[re_res.group(2)] = re_res.group(1)
            re_res = re.search(r"&page=(\d+)&.*>; rel=\"(\w+)\"", val)
            if re_res is not None:
                list_page[re_res.group(2)] = re_res.group(1)
    return { 'data': json.loads(contents), 'pages': list_page }

def selftest():
    objConfig = ITCConfig()
    objConfig.Load()
    apikey = objConfig.GetConfig('github_key')
    print("Configured GitHub API key: '{}'".format(apikey))
    if len(sys.argv) > 1:
        res = GetListIssues(sys.argv[1], apikey, 'i18n-tracking')
        print("Loaded i18n-tracking issues count in {} (total of open/close) = {:d}".format(sys.argv[1], len(res)))
    else:
        print("To test ghapi, run as <script_name> <target :org:/:repo:>")

if __name__ == "__main__":
    selftest()

