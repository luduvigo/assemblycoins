import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import request
from flask import make_response
import requests
import json
import ast
import time
import node
import bitsource
import transactions
import addresses
import workertasks
import unicodedata
import databases

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
dbname='barisser'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']  #"postgresql://localhost/"+dbname

#META

@app.route('/')
def something():
  response=make_response("Welcome to the Assembly Assets API ", 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/blocks/count')
def getblockcount():
  count=node.connect("getblockcount",[])
  jsonresponse={}
  jsonresponse['block_count']=int(count)
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#ADDRESSES

@app.route('/v1/addresses/')   #  WORKS
def makerandompair():
  pair=addresses.generate_secure_pair()
  response=make_response(str(pair), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/addresses/<public_address>/<color_address>')
def colorbalance(public_address=None, color_address=None):  #WORKS
  answer=databases.color_balance(public_address, color_address)
  jsonresponse={}
  jsonresponse[public_address]=answer
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/addresses/<public_address>')
def colorbalances(public_address=None): #show all colors for one address
  answer=databases.color_balance(public_address, None)
  jsonresponse={}
  jsonresponse[public_address]=answer
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#COLORS

@app.route('/v1/coins/prepare', methods=['POST'])   #WORKS
def givenewaddress():
  pair=addresses.generate_secure_pair()
  public_address=pair['public_address']
  private_key=pair['private_key']

  coin_name=request.form['coin_name']
  color_amount=request.form['issued_amount']
  dest_address=request.form['destination_address']
  description=request.form['description']
  #ticker=request.form['ticker']
  email=request.form['email']

  fee_each=0.00005
  markup=1
  tosend=str(transactions.creation_cost(color_amount, coin_name, coin_name, description, fee_each, markup))

  responsejson={}
  responsejson['name']=coin_name
  responsejson['minting_fee']=tosend
  responsejson['issuing_public_address']=public_address
  responsejson['issuing_private_key']=private_key
  responsejson=json.dumps(responsejson)

  #color_address='SFSDF'#addresses.hashlib.sha256(coin_name).hexdigest() #FIGURE THIS OUT

  # #write address to db
  amount_expected=str(int(float(tosend)*100000000))
  amount_received="0"
  amount_withdrawn="0"
  k=databases.add_address(public_address, private_key, amount_expected, amount_received, amount_withdrawn, coin_name, color_amount, dest_address, description, email)
  print k

  response=make_response(responsejson, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/colors/', methods=['POST'])
def makenewcolor():
  fromaddr=str(request.form['fromaddr'])
  colornumber=str(request.form['colornumber'])
  colorname=str(request.form['colorname'])
  destination=str(request.form['destination'])
  fee_each=str(request.form['fee_each'])
  private_key=str(request.form['private_key'])
  description=str(request.form['description'])

  print str(fromaddr)
  result=transactions.make_new_coin(fromaddr, colornumber, colorname, destination, fee_each, private_key, description)
  response=make_response(str(results), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/colors/<color_address>')
def colorholders(color_address=None):
  answer=databases.color_holders(color_address)
  answer=json.dumps(answer)
  response=make_response(str(answer), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/colors/')
def colormeta():
  answer=databases.dbexecute("SELECT * FROM COLORS;",True)
  jsonresponse={}
  jsonresponse['colors']=[]
  for x in answer:
    r={}
    r['color_address']=x[0]
    r['source_address']=x[1]
    r['total_issued']=x[2]
    #ADD COLOR NAME SOON
    jsonresponse['colors'].append(r)
  answer=json.dumps(jsonresponse)
  response=make_response(str(answer), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#MESSAGES
@app.route('/v1/opreturns/<blockn>')           #DEPRECATED, NOT SUPPORTED
def opreturns_in_block(blockn=None):
    print blockn
    blockn=int(blockn)
    message=bitsource.op_return_in_block(blockn)
    # jsonresponse={}
    # jsonresponse['block_height']=int(blockn)
    # jsonresponse['op_returns']=[]
    # for x in message:
    #   r={}
    #   r['transaction_hash']=x[0]
    #   r['message']=x[1]
    #   r['btc']=x[2]
    #   jsonresponse['op_returns'].append(r)
    #
    # answer=json.dumps(jsonresponse)
    response=make_response(str(message), 200)
    response.headers['Access-Control-Allow-Origin']= '*'
    return response

@app.route('/v1/messages/<address>')     #WORKS
def readmultistatements(address=None):
  result=addresses.read_opreturns_sent_by_address(address)
  jsonresponse={}
  jsonresponse['statements']=result
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/messages/raw/<address>')
def opreturns_sent_by_address(address=None):
  results=addresses.find_opreturns_sent_by_address(address)
  jsonresponse={}
  jsonresponse['op_returns']=results
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(jsonresponse, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/messages/', methods=['POST'])
def newdeclaration():
  fromaddr=str(request.form['public_address'])
  fee_each=str(request.form['fee_each'])
  privatekey=str(request.form['private_key'])
  message=str(request.form['message'])
  print message
  results=transactions.declaration_tx(fromaddr, fee_each, privatekey, message)
  print results
  jsonresponse={}
  jsonresponse['transaction_id']=results
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(jsonresponse, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#TXS
@app.route('/v1/transactions/parsed/<blockn>')         #WORKS, needs color address
def oas_in_block(blockn=None):
  oas=workertasks.oa_in_block(int(blockn))
  answer={}
  answer['parsed_transactions']=[]
  for x in oas:
    r={}
    r['transaction_hash_with_index']=x[0]
    r['parsed_colored_info']=x[1]
    answer['parsed_transactions'].append(r)
  answer=json.dumps(answer)
  response=make_response(str(answer), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/transactions/colored', methods=['POST'])  #DOESNT EXACTLY MATCH DOCS
def transfer_transaction_serverside():
  fromaddr=str(request.form['public_address'])
  dest=str(request.form['recipient'])
  fee=float(request.form['fee'])   #DOESNT MATCH DOCS
  private_key=str(request.form['private_key'])
  coloramt=int(request.form['coloramt'])

  inputs=str(request.form['inputs'])
  inputs=ast.literal_eval(inputs)
  inputcoloramt=int(request.form['inputcoloramt'])
  print fromaddr
  print dest
  print fee
  print private_key
  print coloramt
  print inputs
  print inputcoloramt
  othermeta=''
  result= transactions.create_transfer_tx(fromaddr, dest, fee, private_key, coloramt, inputs, inputcoloramt, othermeta)
  response=make_response(str(result), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/transactions/raw/<transaction_hash>')
def getrawtransaction(transaction_hash=None):
  transaction_hash=transaction_hash.encode('ascii')
  response=bitsource.tx_lookup(str(transaction_hash))
  jsonresponse={}
  jsonresponse['raw_transaction']=response
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/transactions/issue', methods=['POST'])    #WORKS
def issuenewcoinsserverside():   #TO ONE RECIPIENT ADDRESS
  private_key=str(request.form['private_keys'])
  public_address=str(request.form['public_address'])
  more_coins=int(request.form['initial_coins'])
  recipient=str(request.form['recipients'])
  fee_each=0.00005
  name=str(request.form['name'])
  othermeta=str(name)
  response=transactions.create_issuing_tx(public_address, recipient, fee_each, private_key, more_coins, 0, othermeta)
  jsonresponse={}
  jsonresponse['transaction_hash']=response
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/transactions/issue/client', methods = ['POST'])      #WORKS
def issuenewcoins_clientside():
  issuing_address=str(request.form['issuing_address'])
  more_coins=request.form['more_coins']
  coin_recipients=str(request.form['coin_recipients'])  #DISCREPANCY, SHOULD BE ARRAY for multiple
  othermeta='COIN NAME HERE'

  fee=0.00005
  print coin_recipients
  print more_coins
  print issuing_address
  print fee
  print othermeta
  tx=transactions.create_issuing_tx_unsigned(issuing_address, coin_recipients, fee, more_coins,othermeta)
  jsonresponse={}
  jsonresponse['transaction_hash']=tx
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/transactions/transfer', methods=['POST'])
def transfercoins_serverside():
  fromaddr=str(request.form['from_public_address'])
  privatekey=str(request.form['from_private_key'])
  coloramt=int(request.form['amount'])
  source_address=str(request.form['source_address'])
  #color_address=str(request.form['color_address'])
  destination=str(request.form['to_public_address'])
  fee=0.00005
  othermeta="Transfer"
  result=transactions.transfer_tx(fromaddr, destination, fee, privatekey, source_address, coloramt, othermeta)
  jsonresponse={}
  jsonresponse['transaction_hash']=result
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/transactions', methods = ['POST'])
def pushtx():
  txhex=str(request.form['transaction_hex'])
  response=transactions.pushtx(txhex)
  jsonresponse={}
  jsonresponse['transaction_id']=response
  jsonresponse=json.dumps(jsonresponse)
  response=make_response(jsonresponse, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response


@app.route('/v1/transactions/<txs_n>') #WORKS
def color_txs_in_block(txs_n=None):
  if txs_n==None:
    txs_n=10

  dbstring="SELECT * FROM outputs ORDER BY blockmade DESC limit "+str(txs_n)+";"
  print dbstring
  results= databases.dbexecute(dbstring,True)

  results=json.dumps(results)
  response=make_response(str(results), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response










#OTHER FUNCTIONS

def update_meta_db(lastblockprocessed, additional_txs):
  meta = databases.meta_db.Meta.query.all().first()

  meta.lastblockprocessed=lastblockprocessed
  meta.numberoftransactions=meta.numberoftransactions+1

  db.session.commit()

working=os.environ['working']

def workerstuff():
  if working:
    print "I am trying to work now"
    workertasks.checkaddresses()
    #try:
    workertasks.more_blocks(50)
  else:
    print "working is off"
  #except:
#    print "FAILED READING BLOCKS"


if __name__ == '__main__':
    app.run()
