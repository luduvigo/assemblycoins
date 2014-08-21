import requests
import json

#HERE I USE BLOCKCHAIN.INFO, GO TO BITSOURCE FOR NODE VERSION

def getblock_blockchain(blockn):
  url='http://blockchain.info/block-index/'+str(blockn)+'?format=json'
  data=requests.get(url)
  jsondata=json.loads(data.content)
  return jsondata


def opreturns_in_block(blockn):
  data=getblock_blockchain(blockn)
  txs=data['tx']
  results=[]

  for tx in txs:
    message=''
    n=0
    for out in tx['out']:
      script=out['script']
      if script[0:2]=='6a':
        m=script[2:len(script)]
        m=m.decode('hex')
        message=m[1:len(m)]
        results.append([str(tx['hash'])+":"+str(n),message])

        n=n+1
  return results
