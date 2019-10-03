## i18n-tracking check tool

* to parse i18n-activity tracker issues at local
* to check consistency between trackers and targets

## usage

## code structure summary

main code and three modules (TBC)

* main code will match lists of issues and check consistency
* modules runs by each with test code
  * i18n-activity tracker issue parser
  * target repository issue list generator
  * helper module with github access and config loader

### utils.py
  
This module is helper module with github access and config loader.

* Load 'config.json' for system wide configuration
  * refer 'config.json.skel' for skelton
  * class ITCConfig, Load() and GetConfig(name)
* Provide GetListIssues(repo, apikey, label) function to list existing issues

self test routine will print

* github api key loaded from configuration
* if repository name is handed as option, 
  number of issues with i18n-tracking label (total of open/closed)

### i18n.py

This module is to list tracker issues in i18n-activity repository, with 
some analysis like making list of tracker targets. 

* Retrieve all (open/closed) issues from i18n-activity repository
* Build following hash internally
  * `list_tracker`: key 'track target URL', value 'issue ID'
  * `list_issues`: key 'issue ID', value 'ghapi issue hash (modified)'
    * `track` key has value of tracker target URL
    * `track_status` key has value of tracker status
  * `list_labels`: key 'label name', value list of 'issue ID'
  * `list_status`: key 'isuse ID', value 'tracker status' ('open', 'close?', 'closed')

self test routine will print

* issue ID with tracker status and target link of tracking

