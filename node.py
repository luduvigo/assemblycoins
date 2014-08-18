import requests
import json
import os
from requests.auth import HTTPBasicAuth

#node_url= '199.188.192.144' #'127.0.0.1'#'71.198.63.116'##
url="blockway.asm.co"
#node_port='8332'
username='u'

username=os.environ['node_username']
password=os.environ['node_password']

def connect(command,params):
  connect_url='https://'+url#+':'+node_port
  headers={'content-type':'application/json'}
  payload=json.dumps({'method':command,'params':params})
  response=requests.get(connect_url,headers=headers,data=payload, verify=False, auth=HTTPBasicAuth(username, password))

  response=json.loads(response.content)
  return response['result']
