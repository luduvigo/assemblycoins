import os
from flask import Flask
from flask import request
import requests
import json
import ast

import bitsource
#import transactions


app = Flask(__name__)


@app.route('/')
def something():
  return "Hello there!"

#GET HEX DECODED OP_RETURNS FROM A BLOCK
@app.route('/opreturns/<blockn>')           #WORKS
def opreturns_in_block(blockn=None):
    print blockn
    blockn=int(blockn)
    message=bitsource.op_return_in_block(blockn)
    return str(message)

# #GET PARSED METADATA FOR OPEN ASSETS TRANSACTIONS IN BLOCK
# @app.route('/oa/blocks/<blockn>')         #WORKS, needs color address
# def oas_in_block(blockn=None):
#   oas=bitsource.oa_in_block(int(blockn))
#   return str(oas)
#
#
# @app.route('/colors/signed', methods=['POST'])
# def makenewcoin():
#   public_address=str(request.form['public_address'])
#   initial_coins=float(request.form['initial_coins'])
#   name=str(request.form['name'])
#   recipient=str(request.form['recipient'])
#   fee_each=0.0001
#   private_key=str(request.form['private_keys'])
#
#   response=transactions.make_new_coin(public_address, initial_coins, name, recipient, fee_each, private_key)
#   #print response
#   return response
#   #return "hi"
#
# @app.route('/transactions/colored', methods=['POST'])  #DOESNT EXACTLY MATCH DOCS
# def transfer_transaction_serverside():
#   fromaddr=str(request.form['public_address'])
#   dest=str(request.form['recipient'])
#   fee=float(request.form['fee'])   #DOESNT MATCH DOCS
#   private_key=str(request.form['private_key'])
#   coloramt=int(request.form['coloramt'])
#
#   inputs=json.dumps(request.form['inputs'])  #INELEGANT BUT IT WORKS
#   inputs=ast.literal_eval(json.loads(inputs))
#
#   inputcoloramt=int(request.form['inputcoloramt'])
#   response= transactions.create_transfer_tx(fromaddr, dest, fee, private_key, coloramt, inputs, inputcoloramt)
#   return str(response)
#
#
# @app.route('/colors/issue/signed', methods=['POST'])    #WORKS
# def issuenewcoinsserverside():   #TO ONE RECIPIENT ADDRESS
#   private_key=str(request.form['private_keys'])
#   public_address=str(request.form['public_address'])
#   more_coins=int(request.form['initial_coins'])
#   recipient=str(request.form['recipients'])
#   fee_each=0.0001
#   name=str(request.form['name'])
#   othermeta=str(name)
#
#   print private_key
#   response=transactions.create_issuing_tx(public_address, recipient, fee_each, private_key, more_coins, 0, othermeta)
#   return response
#   return str(name)
#
# @app.route('/colors/issue', methods = ['POST'])      #WORKS
# def issuenewcoins_clientside():
#   #JUST RETURN RAW HEX OF UNSIGNED TX
#   issuing_address=str(request.form['issuing_address'])
#   more_coins=int(request.form['more_coins'])
#   coin_recipients=str(request.form['coin_recipients'])  #DISCREPANCY, SHOULD BE ARRAY for multiple
#   othermeta='COIN NAME HERE'
#
#   fee=0.0001
#   print coin_recipients
#   print more_coins
#   print issuing_address
#   print fee
#   print othermeta
#   tx=transactions.create_issuing_tx_unsigned(issuing_address, coin_recipients, fee, more_coins,othermeta)
#   #return 'a'
#   return str(tx)
#
#
# @app.route('/transactions', methods = ['POST'])
# def pushtx():
#   txhex=str(request.form['transaction_hex'])
#   response=transactions.pushtx(txhex)
#   return str(response)

if __name__ == '__main__':
    app.run()
