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

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']=True
dbname='barisser'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']  #"postgresql://localhost/"+dbname

import databases

@app.route('/')
def something():
  response=make_response("Hey there!", 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/blocks/count')
def getblockcount():
  count=node.connect("getblockcount",[])
  response=make_response(str(count), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

#GET HEX DECODED OP_RETURNS FROM A BLOCK
@app.route('/opreturns/<blockn>')           #WORKS
def opreturns_in_block(blockn=None):
    print blockn
    blockn=int(blockn)
    message=bitsource.op_return_in_block(blockn)
    return str(message)

#GET PARSED METADATA FOR OPEN ASSETS TRANSACTIONS IN BLOCK
@app.route('/oa/blocks/<blockn>')         #WORKS, needs color address
def oas_in_block(blockn=None):
  oas=workertasks.oa_in_block(int(blockn))
  return str(oas)

@app.route('/colors/signed', methods=['POST'])
def makenewcoin():
  public_address=str(request.form['public_address'])
  initial_coins=int(request.form['initial_coins'])
  name=str(request.form['name'])
  recipient=str(request.form['recipient'])
  fee_each=0.00005
  private_key=str(request.form['private_key'])
  ticker=str(request.form['ticker'])
  description=str(request.form['description'])

  response=transactions.make_new_coin(public_address, initial_coins, name, recipient, fee_each, private_key, ticker, description)
  response=make_response(str(response), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response


@app.route('/transactions/colored', methods=['POST'])  #DOESNT EXACTLY MATCH DOCS
def transfer_transaction_serverside():
  fromaddr=str(request.form['public_address'])
  dest=str(request.form['recipient'])
  fee=float(request.form['fee'])   #DOESNT MATCH DOCS
  private_key=str(request.form['private_key'])
  coloramt=int(request.form['coloramt'])

  #inputs=request.form['inputs']
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
  response= transactions.create_transfer_tx(fromaddr, dest, fee, private_key, coloramt, inputs, inputcoloramt, othermeta)
  return str(response)
  #return str(coloramt)

@app.route('/transactions/<transaction_hash>')
def getrawtransaction(transaction_hash=None):
  transaction_hash=transaction_hash.encode('ascii')
  response=bitsource.tx_lookup(str(transaction_hash))
  #print response
  response=make_response(str(response), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response
  #return str(transaction_hash)

@app.route('/v1/colors/statements/<address>')     #WORKS
def readmultistatements(address=None):
  result=addresses.read_opreturns_sent_by_address(address)
  response=make_response(result, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

  return str(result)

@app.route('/colors/issue/signed', methods=['POST'])    #WORKS
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
  color_address=str(request.form['color_address'])
  destination=str(request.form['to_public_address'])
  fee=0.00005
  othermeta="Transfer"
  result=transactions.transfer_tx(fromaddr, destination, fee, privatekey, color_address, coloramt, othermeta)

  response=make_response(result, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response


@app.route('/v1/addresses/generate')   #  WORKS
def makerandompair():
  return str(addresses.generate_secure_pair())

@app.route('/v1/messages/<address>')
def opreturns_sent_by_address(address=None):
  results=addresses.find_opreturns_sent_by_address(address)
  return str(results)

@app.route('/transactions', methods = ['POST'])
def pushtx():
  txhex=str(request.form['transaction_hex'])
  response=transactions.pushtx(txhex)
  return str(response)

@app.route('/v1/coins/prepare', methods=['POST'])   #WORKS
def givenewaddress():
  pair=addresses.generate_secure_pair()
  public_address=pair['public_address']
  private_key=pair['private_key']

  coin_name=request.form['coin_name']
  color_amount=request.form['issued_amount']
  dest_address=request.form['destination_address']
  description=request.form['description']
  ticker=request.form['ticker']
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

  color_address='SFSDF'#addresses.hashlib.sha256(coin_name).hexdigest() #FIGURE THIS OUT

  # #write address to db
  amount_expected=str(int(float(tosend)*100000000))
  amount_received="0"
  amount_withdrawn="0"
  k=databases.add_address(public_address, private_key, amount_expected, amount_received, amount_withdrawn, coin_name, color_amount, dest_address, description, ticker, email)
  print k

  response=make_response(responsejson, 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

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


# @app.route('/colors/issue/signed', methods=['POST'])    #WORKS
# def issuenewcoinsserverside():   #TO ONE RECIPIENT ADDRESS
#   private_key=str(request.form['private_keys'])
#   public_address=str(request.form['public_address'])
#   more_coins=int(request.form['initial_coins'])
#   recipient=str(request.form['recipients'])

@app.route('/v1/colors/makenew', methods=['POST'])
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
  return str(result)

@app.route('/v1/addresses/<public_address>/<color_address>')
def colorbalance(public_address=None, color_address=None):  #WORKS
  answer=databases.color_balance(public_address, color_address)
  response=make_response(str(int(answer)), 200)
  response.headers['Access-Control-Allow-Origin']= '*'
  return response

@app.route('/v1/addresses/<public_address>')
def colorbalances(public_address=None): #show all colors for one address
  answer=databases.color_balance(public_address, None)
  answer=json.dumps(answer)
  response=make_response(str(answer), 200)
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

def update_meta_db(lastblockprocessed, additional_txs):
  meta = databases.meta_db.Meta.query.all().first()

  meta.lastblockprocessed=lastblockprocessed
  meta.numberoftransactions=meta.numberoftransactions+1

  db.session.commit()

def workerstuff():
  print "I am trying to work now"
  #workertasks.checkaddresses()
  #try:
  workertasks.more_blocks(20)
  #except:
#    print "FAILED READING BLOCKS"


if __name__ == '__main__':
    app.run()
