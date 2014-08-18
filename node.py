import requests
import json


#node_url= '199.188.192.144' #'127.0.0.1'#'71.198.63.116'##
url="blockway.asm.co"
#node_port='8332'
username='u'

config_file=open('config')
username=config_file.readline().replace('\n','')
password=config_file.readline().replace('\n','')

def connect(command,params):
  connect_url='https://'+username+':'+password+'@'+url#+':'+node_port
  headers={'content-type':'application/json'}
  payload=json.dumps({'method':command,'params':params})
  response=requests.get(connect_url,headers=headers,data=payload, verify=False)

  response=json.loads(response.content)
  return response['result']
