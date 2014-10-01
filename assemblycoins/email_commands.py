import requests
import os
import json

def email_one(from_email, to_email, subject, content, html):
  api_url=os.environ['mailgun_url']
  api_key=os.environ['mailgun_api_key']
  authobject=("api", api_key)
  datas={}
  datas['from']=from_email
  datas['to']=to_email
  datas['subject']=subject
  datas['text']=content
  datas['html']=html
  response=requests.post(api_url, auth=authobject, data=datas)
  return response.content

def email_creation(their_email, colorname, colornumber, description, txhash):
  from_email="barisser@assembly.com"

  coloraddress=requests.get("https://coins.assembly.com/v1/colors/name/"+str(colorname)).content
  coloraddress=json.loads(coloraddress)['color_address']
  explorerlink="https://coins.assembly.com/colors/"+str(coloraddress)

  subject="Your Colored Coins, "+str(colorname)+" are on the Blockchain"
  content=""
  html="<h2>You just created a cryptocurrency.</h2><p><br>"+str(colornumber)+" "
  html=html+"<a href='"+str(explorerlink)+"'>"+str(colorname)+"</a>"
  html=html+" Coins were just created on the Bitcoin Blockchain."
  html=html+"<br><br>Check out the Genesis Transaction: <a href='https://blockchain.info/tx/"+str(txhash)+"'>https://blockchain.info/tx/"+str(txhash)+"</a>."
  html=html+"<br><br>There were declared with the following metadata on the Blockchain:<br><br>"+str(description)+"</p>"
  print "EMAIL CREATED"
  print html
  print ''
  response=email_one(from_email, their_email, subject, content, html)
  return response
