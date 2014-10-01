import requests
import os

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
