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

