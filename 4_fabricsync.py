#!/usr/bin/python

import requests
from xml.etree import ElementTree

url1='https://nsxmgr01.corp.local.com//api/2.0/nwfabric/resolveIssues/domain-c77'
url2='https://nsxmgr01.corp.local.com//api/2.0/nwfabric/resolveIssues/domain-c53'
url3='https://nsxmgr02.corp.local.com//api/2.0/nwfabric/resolveIssues/domain-c76'

nsxmanager_user='admin'
nsxmanager_password='VMware1!'

nsx_headers={'content-type':'application/xml'}


try:
        response = requests.post(url1, headers=nsx_headers,auth=(nsxmanager_user,nsxmanager_password), verify=False)
except requests.exceptions.ConnectionError as e:
        print ("Connection error")

print (response.text)


try:
        response = requests.post(url2, headers=nsx_headers,auth=(nsxmanager_user,nsxmanager_password), verify=False)
except requests.exceptions.ConnectionError as e:
        print ("Connection error")

print (response.text)

try:
        response = requests.post(url3, headers=nsx_headers,auth=(nsxmanager_user,nsxmanager_password), verify=False)
except requests.exceptions.ConnectionError as e:
        print ("Connection error")

print (response.text)
