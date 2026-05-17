#! /usr/bin/env python3

import sys
import json
import re

from github import Github
from github import Auth

DEF_CONF_NAME = 'config.json'
DEF_CACHE_HEAD = 'cache.'

DEF_CACHE_USER = 'user'

o_cache = {}
o_re = {}
o_gh = None

def LoadCache(name):
  c_ret = {}
  try:
    fname = "%s%s" % (DEF_CACHE_HEAD, name)
    fjson = open(fname, 'r')
  except IOError as e:
    # if not exist, just return vacant hash
    return c_ret
  try:
    c_ret = json.load(fjson)
  except:
    raise Exception("json format parse error for '%s'" % (fname))
  return c_ret

def SaveCache():
  global o_cache
  for c_name in o_cache:
    try:
      fname = "%s%s" % (DEF_CACHE_HEAD, c_name)
      fjson = open(fname, 'w')
    except IOError as e:
      print("Error on SaveCache to '%s'" % (c_name))   # XXX insert debug handler
      continue
    json.dump(o_cache[c_name], fjson)

def LoadConfig(cnf = DEF_CONF_NAME):
  try:
    fjson = open(cnf, 'r')
  except IOError as e:
    raise Exception("File '%s' open error: %s" % (DEF_CONF_NAME, e))
  try:
    c_cnf = json.load(fjson)
  except:
    raise Exception("json format parse error for '%s'" % (DEF_CONF_NAME))
  return c_cnf

def AuthGhapi(token):
  global o_gh
  c_auth = Auth.Token(token)
  o_gh = Github(auth = c_auth)

  return o_gh

def GetUser(login):
  global o_cache, o_gh
  if not (DEF_CACHE_USER in o_cache):
    o_cache[DEF_CACHE_USER] = LoadCache(DEF_CACHE_USER)
  if login in o_cache[DEF_CACHE_USER]:
    return o_cache[DEF_CACHE_USER][login]
  o_cache[DEF_CACHE_USER][login] = o_gh.get_user(login)
  return o_cache[DEF_CACHE_USER][login]

def ReplaceBracket(tgt, dat):
  global o_re
  for c_key in dat:
    if not (c_key in o_re):
      o_re[c_key] = re.compile('\\[' + c_key + '\\]')
    tgt = re.sub(o_re[c_key], dat[c_key], tgt)
  return tgt


