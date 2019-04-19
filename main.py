import json
import traceback
import sys
import pandas as pd
from pathlib import Path
import csv
import time
import requests
import os
from typing import Callable, Any, Union, Iterable
import urllib


def get(base_url,
        endpoint_id,
        personal_access_token,
        account_id,
        user_email,
        user_agent = 'ha-harvest-integration'):

    url = base_url + endpoint_id
    headers = {'Authorization': 'Bearer '+ personal_access_token,
               'Harvest-Account-Id': account_id,
               'User-Agent': user_agent + ' (' + user_email +')'}
    
    r = requests.get(url, headers = headers)
    print(r.status_code)
    
    if not r.ok:
        raise ValueError('get failed for endpoint' + endpoint_id)
        
    return r.json()

def main(params):
    print(params)
    
    user_email = params['user_email']
    personal_access_token = params['#personal_access_token']
    account_id = params['account_id']
    base_url = params['base_url']
    endpoints = params['endpoints']
    
    for endpoint in endpoints:
        endpoint_id = endpoint['endpoint_id']
        response = get(base_url,
                       endpoint_id,
                       personal_access_token,
                       account_id,
                       user_email)
#        TODO: Write JSON to CSV

if __name__ == "__main__":
    print("hello world")
    with open("data/config.json") as f:
        cfg = json.load(f)
    try:
        main(cfg['parameters'])
    except Exception as err:
        print(err)
        traceback.print_exc()
        sys.exit(1)

#try:
#    f = open("data/config.json")
#    ghlj
#    
#    
#    
#    
#    
#except Exceptio as err:
#    print(err)
#    traceback.print_exc()
#    sys.exit(1)
#finally:
#    f.close()
        
def irene():
    print("I don't get it")
    
def francis(hair_colour):
    print("Francis' hair is ")
    print(hair_colour)