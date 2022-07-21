#! /usr/bin/env python3

# print login from each entry
# use as $ ls -1 *json | awk '{print "./print_login.py", $1,"|sort > " $1 "-list"}'

import sys
import os
import json


def LoadJson(target_json):
  try:
    obj_specs = open(target_json)
    team_data = json.load(obj_specs)
    obj_specs.close()
  except:
    raise Exception("json format parse error")
  logins = []
  for login in team_data:
    logins.append(login['login'])
  return logins


if __name__ == "__main__":
  if len(sys.argv) < 2:
    raise Exception("Usage <script> <target json>")
  list_login = LoadJson(sys.argv[1])
  for login in list_login:
    print(login)
