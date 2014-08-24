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
        results.append([str(tx['hash'])+":"+str(n),message])
      n=n+1

  return results

def oa_in_block(blockn):
  opreturns=opreturns_in_block(blockn)
  oatxs=[]
  for x in opreturns:
    if x[1][0:2]=='OA':
      parsed=bitsource.parse_colored_tx(x[1])
      oatxs.append([x[0], parsed])
  return oatxs

#def add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade):

def add_output_db(blockn):
  results=oa_in_block(blockn)

  for x in results:
      btc=''
      coloramt=''
      coloraddress=''
      spent='False'
      spentat=''
      destination=''
      txhash=''
      txhash_index=''
      blockmade=str(blockn)

      databases.add_output(btc,coloramt,coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade)


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

  owed_data=[]
  for x in owedlist:
    r={}
    r['public_address']=x.public_address
    r['private_key']=x.private_key
    r['amount_expected']=x.amount_expected
    r['amount_received']=x.amount_received
    r['amount_withdrawn']=x.amount_withdrawn
    r['coin_name']=x.coin_name
    r['color_address']=x.color_address
    r['issued_amount']=x.issued_amount
    r['destination_address']=x.destination_address
    r['description']=x.description
    owed_data.append(r)

  for address in owed_data:
    if value>=address['amount_expected'] and address['amount_withdrawn']<address['amount_expected']:
      #WITHDRAW IT AND PROCESS AND MARK AS WITHDRAWN IN DB
      fromaddr=address['public_address']
      colornumber=address['issued_amount']
      colorname=address['coin_name']
      destination=address['destination_address']
      fee_each=0.00004
      private_key=address['private_key']
      ticker=address['coin_name'][0:3]
      description=address['description']

      txid=txdata[0]
      txid=txid+":0" #ISSUED COINS ARE ALWAYS IN FIRST POSITION, NOT TRUE WITH TRANSFERS
      print inputs
      inputs=txdata[1][0]['output']  #MARK NEW COLOR ADDRESS
      scriptoutputs=bitsource.tx_lookup(inputs)
      script=''
      try:
        script=scriptoutputs['vout'][0]['scriptPubKey']['hex']
      except:
        print "problem with getting script"
      print "INPUT script"
      print script

      #MARK AS WITHDRAWN IN DB
      address_entry=databases.address_db.Address.query.filter_by(private_key=address['private_key']).first()
      address_entry.amount_withdrawn=address['amount_expected']
      address_entry.amount_received=value;

      colorscript=script
      coloraddress=bitsource.script_to_coloraddress(colorscript)
      spent=False
      currentblock=node.connect("getblockcount",[])
      transaction_entry=databases.transactions_db.Transaction(txid, fromaddr, destination, colornumber, coloraddress, spent, currentblock)
      db.session.add(transaction_entry)
      db.session.commit()   #WORKS


  return owed_data
