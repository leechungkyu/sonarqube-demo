# -*- coding: utf-8 -*-
#############
# 사전 설치
##############
# pip install python-jenkins
# pip install requests

import jenkins 
import json
import requests 
import sys
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
server_url = '' # ex) http://jenkinskorea.jenkins.org
user = '' # ex) admin
passwd = '' # ex) admin
 
server = jenkins.Jenkins(server_url, username=user, password=passwd)
 
# get console output
job_name = 'sonarqube-demo'
build_num = 1
console_output = server.get_build_console_output(job_name, build_num)
 
print('*' * 200)
print(console_output)
print('*' * 200)
 
# send to slack...
slack_url = '' # ex) https://hooks.slack.com/services/T75QJS2AC/BAHLN2P8R/o5Q3IsOE8q7le123456789
slack_payload = {"text" : str(console_output)}
res = requests.post(url=slack_url, data=json.dumps(slack_payload))
print(res)
