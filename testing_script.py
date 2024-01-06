# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:37:19 2023

@author: Aditya
"""

import requests

#---- Below parameter needs to be udpated 

data = {'text1':'He likes to play',
        'text2': 'Ram loves cricket'}

url = 'http://127.0.0.1:5000/home'
#------------------


header = {"Content-Type": "application/json"}
response = requests.post(url, json=data)


print("Status Code", response.status_code)
print("JSON Response ", response.text)


