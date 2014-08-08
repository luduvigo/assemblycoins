import os
from flask import Flask
from flask import request
import requests
import json

import bitsource
import transactions
#import worker
#import trader

app = Flask(__name__)


@app.route('/')
def something():
  return "Hello there!"

#GET HEX DECODED OP_RETURNS FROM A BLOCK
@app.route('/opreturns/<blockn>')
def opreturns_in_block(blockn=None):
    print blockn
    blockn=int(blockn)
    message=bitsource.op_return_in_block(blockn)
    return str(message)

#GET PARSED METADATA FOR OPEN ASSETS TRANSACTIONS IN BLOCK
@app.route('/oa/blocks/<blockn>')
def oas_in_block(blockn=None):
  oas=bitsource.oa_in_block(int(blockn))
  return str(oas)

@app.route('/colors/signed', methods=['POST'])
def makenewcoin():
  public_address=str(request.form['public_address'])
  initial_coins=float(request.form['initial_coins'])
  name=str(request.form['name'])
  recipient=str(request.form['recipient'])
  fee_each=0.0001
  private_key=str(request.form['private_keys'])

  #response=transactions.make_new_coin(public_address, initial_coins, name, recipient, fee_each, private_key)
  #print response
  #return response
  return "hi"

@app.route('/getpersonbyid', methods = ['POST'])
def getPersonById():
    return str(request.form['name'])


if __name__ == '__main__':
    app.run()
