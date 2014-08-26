import requests
import json
import os
from requests.auth import HTTPBasicAuth

#url="blockway.asm.co"
url='3950472c.ngrok.com'
#node_port='8332'

username=os.environ['node_username']
password=os.environ['node_password']

def connect(command,params):
  connect_url='https://'+url#+':'+node_port
  headers={'content-type':'application/json'}
  payload=json.dumps({'method':command,'params':params})
  response=requests.get(connect_url,headers=headers,data=payload, verify=False, auth=HTTPBasicAuth(username, password))

  response=json.loads(response.content)
  return response['result']
