import requests
import json
import os
from requests.auth import HTTPBasicAuth

#node_url= '199.188.192.144' #'127.0.0.1'#'71.198.63.116'##
#url="blockway.asm.co"
url='82db5a0.ngrok.com'
#node_port='8332'
#username='u'

username="barisser"
#username=os.environ['node_username']
password="2bf763d2132a2ccf3ea38077f79196ebd600f4a29aa3b1afd96feec2e7d80beb3d9e13d02d56de0f"#
#password=os.environ['node_password']

def connect(command,params):
  connect_url='https://'+url#+':'+node_port
  headers={'content-type':'application/json'}
  payload=json.dumps({'method':command,'params':params})
  response=requests.get(connect_url,headers=headers,data=payload, verify=False, auth=HTTPBasicAuth(username, password))

  response=json.loads(response.content)
  return response['result']
