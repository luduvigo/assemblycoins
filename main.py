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

@app.route('/blocks/count')
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
  jsonresponse[public_address]=[]
  jsonresponse[public_address].append(answer)
  response=make_response(str(jsonresponse), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/addresses/<public_address>')
def colorbalances(public_address=None): #show all colors for one address
  answer=databases.color_balance(public_address, None)
  answer=json.dumps(answer)
  response=make_response(str(answer), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#COLORS

@app.route('/v1/coins/prepare', methods=['POST'])   #WORKS

@app.route('/v1/colors/', methods=['POST'])
def makenewcolor():
  fromaddr=str(request.form['fromaddr'])
  colornumber=str(request.form['colornumber'])
  colorname=str(request.form['colorname'])
  destination=str(request.form['destination'])
  fee_each=str(request.form['fee_each'])
  private_key=str(request.form['private_key'])
  ticker=str(request.form['ticker'])
  description=str(request.form['description'])

  print str(fromaddr)
  result=transactions.make_new_coin(fromaddr, colornumber, colorname, destination, fee_each, private_key, ticker, description)
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

@app.route('/colors/')
def colormeta():
  answer=databases.dbexecute("SELECT * FROM COLORS;",True)
  answer=json.dumps(answer)
  response=make_response(str(answer), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#MESSAGES
@app.route('/opreturns/<blockn>')           #WORKS
def opreturns_in_block(blockn=None):
    print blockn
    blockn=int(blockn)
    message=bitsource.op_return_in_block(blockn)
    return str(message)

@app.route('/v1/colors/statements/<address>')     #WORKS
def readmultistatements(address=None):
  result=addresses.read_opreturns_sent_by_address(address)
  response=make_response(result, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response
  return str(result)

@app.route('/v1/colors/metadata/<source_address>')
def parsemultistatements(source_address=None):
  result=addresses.read_opreturns_sent_by_address(address)

@app.route('/v1/messages/<address>')
def opreturns_sent_by_address(address=None):
  results=addresses.find_opreturns_sent_by_address(address)
  return str(results)

@app.route('/v1/messages/', methods=['POST'])
def newdeclaration():
  fromaddr=str(request.form['public_address'])
  fee_each=str(request.form['fee_each'])
  privatekey=str(request.form['private_key'])
  message=str(request.form['message'])
  results=transactions.declaration_tx(fromaddr, fee_each, privatekey, message)

  response=make_response(str(results), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#TXS
@app.route('/oa/blocks/<blockn>')         #WORKS, needs color address
def oas_in_block(blockn=None):
  oas=workertasks.oa_in_block(int(blockn))
  return str(oas)

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

@app.route('/v1/transactions/<transaction_hash>')
def getrawtransaction(transaction_hash=None):
  transaction_hash=transaction_hash.encode('ascii')
  response=bitsource.tx_lookup(str(transaction_hash))
  response=make_response(str(response), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/colors/issue/signed', methods=['POST'])    #WORKS
def issuenewcoinsserverside():   #TO ONE RECIPIENT ADDRESS
  private_key=str(request.form['private_keys'])
  public_address=str(request.form['public_address'])
  more_coins=int(request.form['initial_coins'])
  recipient=str(request.form['recipients'])
  fee_each=0.00005
  name=str(request.form['name'])
  othermeta=str(name)

  print private_key
  response=transactions.create_issuing_tx(public_address, recipient, fee_each, private_key, more_coins, 0, othermeta)
  return response
  return str(name)

@app.route('/v1/colors/issue', methods = ['POST'])      #WORKS
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
  #return 'a'
  return str(tx)

@app.route('/v1/colors/transfer', methods=['POST'])
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

  response=make_response(result, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/transactions', methods = ['POST'])
def pushtx():
  txhex=str(request.form['transaction_hex'])
  response=transactions.pushtx(txhex)
  return str(response)

@app.route('/colors/transactions/') #WORKS
def color_txs_in_block():

  dbstring="SELECT * FROM outputs ORDER BY blockmade DESC;"
  results= databases.dbexecute(dbstring,True)
  maxreturnlength=100
  if len(results)>maxreturnlength:
    results=results[0:maxreturnlength]

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
    #workertasks.checkaddresses()
    #try:
    workertasks.more_blocks(20)
  else:
    print "working is off"
  #except:
#    print "FAILED READING BLOCKS"


if __name__ == '__main__':
    app.run()
