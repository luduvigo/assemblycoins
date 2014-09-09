import requests
import os

api_key=os.environ['MAILGUN_API_KEY']
api_url="https://api:"+api_key+"@api.mailgun.net/v2/assets.assembly.com"


def send_simple_message():
    return requests.post(
        api_url,
        auth=("api", api_key),
        data={"from": "api@assets.assembly.com",
              "to": "Andrew <barisser@assembly.com>",
              "subject": "Hello Andrew, teST",
              "text": "THis is a test"})
