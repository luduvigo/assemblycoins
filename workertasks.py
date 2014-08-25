import requests
import json
import addresses
import transactions
import bitsource
import databases

#HERE I USE BLOCKCHAIN.INFO, GO TO BITSOURCE FOR NODE VERSION

def getblock_blockchain(blockn):
  url='http://blockchain.info/block-height/'+str(blockn)+'?format=json'
  data=requests.get(url)
  print url
  jsondata=json.loads(data.content)
  answer={}
  for x in jsondata['blocks']:
    if x['main_chain']==True:
      answer=x
  return answer


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
        print m
        message=m[1:len(m)]
        amount=0
        for x in tx['inputs']:
          amount=amount+x['prev_out']['value']

        results.append([str(tx['hash'])+":"+str(n),message, amount])
      n=n+1

  return results

def oa_in_block(blockn):
  opreturns=opreturns_in_block(blockn)
  oatxs=[]
  for x in opreturns:
    if x[1][0:2]=='OA':
      parsed=bitsource.parse_colored_tx(x[1])
      oatxs.append([x[0],parsed,x[2]])
  return oatxs

#def add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade):

def add_output_db(blockn):
  results=oa_in_block(blockn)

  for x in results:
      btc=str(x[2])
      coloramt=str(x[1]['asset_quantities'][0])
      coloraddress="coloraddress"
      spent="False"
      spentat=""
      destination=""
      txhash=str(x[0][0:len(x[0])-2])
      txhash_index=str(x[0])
      blockmade=str(blockn)

      databases.add_output(btc,coloramt,coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade)

def blocks_outputs(blockend):
  lastblockprocessed=databases.dbstring("SELECT * FROM META;",True)
  if blockend>currentblock:
    blockend=currentblock
  currentblock=node.connect('getblockcount',[])
  if blockend>currentblock:
    blockend=currentblock
  for i in range(lastblockprocessed+1,currentblock+1):
    add_output_db(i)
    print "processed block "+str(i)
    databases.dbexecute("UPDATE META SET lastblockdone='"+i+"';",False)

def checkaddresses():  #FOR PAYMENT DUE      #WORKS
  #check all addresses that are still pending
    #for each that is ready, go through makenewcoins process
    #mark as completed
    #send profits elsewhere

  #read all addresses
  dbstring="SELECT * FROM ADDRESSES WHERE amount_withdrawn=0;"
  addresslist=databases.dbexecute(dbstring,True)
  print addresslist

  for address in addresslist:
    unspents=addresses.unspent(address[0])
    value=0
    for x in unspents:
      value=value+x['value']
    print "currently available in "+str(address[0])+" : "+str(value/100000000)

    if value>=address[2] and address[3]<address[2]:
      #makenewcoins
      fromaddr=address[0]
      colornumber=address[6]
      colorname=address[5]
      destination=address[7]
      fee_each=0.00004
      private_key=address[1]
      ticker=address[9]
      description=address[8]
      txdata=transactions.make_new_coin(fromaddr, colornumber, colorname, destination, fee_each, private_key, ticker, description)

      txhash=txdata[0]
      txhash=txhash+":0" #issuance always first output
      specific_inputs=txdata[1]['output']

      #mark as completed
      databases.edit_address(fromaddr, value, value, colornumber)

      #add entry to colors db
      color_address='COLOR HERE'
      databases.add_color(color_address, fromaddr, colornumber, colorname)

      #add entry to outputs db

      #send profits elsewhere
