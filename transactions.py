import addresses
import requests
import json
from bitcoin import *
import node
import bitsource
import cointools
import databases

dust=2461*0.00000001
max_op_length=35 #in bytes

def find_suitable_inputs(public_address, amount_needed, spend_dust, sought_for_tag):
  inputs=cointools.unspent(public_address)
  amount_needed=int(amount_needed*100000000)
  result=[]
  totalin=0
  n=0
  for ins in inputs:
    if totalin<amount_needed:
      if not spend_dust and inputs[n]['value']>dust*100000000:
        result.append(inputs[n])
        totalin=totalin+inputs[n]['value']
      elif spend_dust:
        result.append(inputs[n])
        totalin=totalin+inputs[n]['value']
    n=n+1
  return result

def make_raw_transaction(fromaddress,amount,destination, fee):
    #try:
      global ins, outs,h, tx, tx2, totalin, extra

      unspents=find_suitable_inputs(fromaddress, amount+fee, False, '')
      fee=int(fee*100000000)
      amount=int(amount*100000000)

      #unspents=addresses.getunspent(fromaddress)
      #unspents=unspent(fromaddress)  #using vitalik's version could be problematic

      print "FOUND INPUTS:"
      print unspents
      print ''

      ins=[]
      outs=[]
      totalin=0

      for uns in unspents:
        totalin=totalin+uns['value']
        ins.append(uns)

      if totalin>=amount+fee:
        outs.append({'value': amount, 'address': destination})
      extra=totalin-amount-fee
      if extra>=dust*100000000:
        outs.append({'value':extra, 'address':fromaddress})

      tx=mktx(ins,outs)
      #print tx
      return tx

def make_raw_one_input(fromaddress,amount,destination,fee, specific_inputs):  #NEEDS REWORKING
  global ins, outs, totalin
  fee=int(fee*100000000)
  amount=int(amount*100000000)
  #unspents=unspent(fromaddress)
  #unspents=[unspents[input_n]]
  unspents=specific_inputs

  ins=[]
  outs=[]
  totalin=0

  print 'unspents below'
  print unspents
  print ''

  for uns in unspents:
    if 'value' in uns:
      totalin=totalin+uns['value']
      ins.append(uns)

  if totalin>=amount+fee:
    outs.append({'value': amount, 'address': destination})
  extra=totalin-amount-fee
  if extra>=dust*100000000:
    outs.append({'value':extra, 'address':fromaddress})


  tx=mktx(ins,outs)
  return tx

def make_raw_multiple_outputs(fromaddress, output_n, output_amount_each, destination, fee):

  global ins, outs,h, tx, tx2, outputs
  outputs=[]
  for i in range(0,output_n):
    outputs.append({'value': int(output_amount_each*100000000), 'address': destination})

  fee=int(fee*100000000)

  unspents=unspent(fromaddress)  #using vitalik's version could be problematic

  totalout=0
  for x in outputs:
    totalout=totalout+x['value']
  ins=[]
  ok=False
  outs=[]
  totalfound=0
  for unsp in unspents:
    ins.append(unsp)
    totalfound=totalfound+unsp['value']
  change_amount=totalfound-totalout-fee
  outs=outputs
  if change_amount>int(dust*100000000):
    outs.append({'value': change_amount, 'address': fromaddress})

  print 'ins'
  print ins
  print ''
  print 'outs'
  print outs

  tx=mktx(ins,outs)

  return tx

def make_multiple_outputs(fromaddress, privatekey, output_n, value_each,  total_fee):  #WORKS
  tx=make_raw_multiple_outputs(fromaddress, output_n, value_each, fromaddress, total_fee)
  tx2=sign_tx(tx, privatekey)
  response=pushtx(tx2)
  free_outputs=[]
  for i in range(0,output_n):
    outputdata={}
    outputdata['output']=str(response)+":"+str(i)
    outputdata['value']= int(value_each*100000000)
    free_outputs.append(outputdata)
  print ''
  print free_outputs
  return free_outputs

def make_op_return_script(message):
   #OP RETURN SCRIPT
   hex_message=message.encode('hex')
   hex_message_length=hex(len(message))

   r=2
   f=''
   while r<len(hex_message_length):
      f=f+hex_message_length[r]
      r=r+1
   if len(f)<2:
      f='0'+f

   b='6a'+f+hex_message
   return b

def add_op_return(unsigned_raw_tx, message, position_n):
  deserialized_tx=deserialize(unsigned_raw_tx)

  newscript=make_op_return_script(message)

  newoutput={}
  newoutput['value']=0
  newoutput['script']=newscript

  if position_n>=len(deserialized_tx['outs']):
    deserialized_tx['outs'].append(newoutput)
  else:
    deserialized_tx['outs'].insert(position_n,newoutput)
  #deserialized_tx['outs'].append(newoutput)

  reserialized_tx=serialize(deserialized_tx)

  return reserialized_tx

def sign_tx(unsigned_raw_tx, privatekey):
  tx2=unsigned_raw_tx

  detx=deserialize(tx2)
  input_length=len(detx['ins'])

  for i in range(0,input_length):
    tx2=sign(tx2,i,privatekey)

  return tx2

def pushtx(rawtx):
  print "Trying to push: "+ str(rawtx)
  response=node.connect('sendrawtransaction',[rawtx])
  print "Push Response was "+str(response)

  return response

def send_op_return(fromaddr, dest, fee, message, privatekey, specific_inputs):
  #specific_input=cointools.unspent(fromaddr)
  #specific_input=specific_input[specific_input_n]

  #tx=make_raw_one_input(fromaddr,dust,dest,fee, specific_input)

  tx=make_raw_one_input(fromaddr, dust, dest, fee, specific_inputs)

  tx2=add_op_return(tx,message,1)
  tx3=sign_tx(tx2,privatekey)
  print tx3
  response=pushtx(tx3)
  #response=''
  #print "Trying to push op return: "
  print tx3
  print "Response: "+str(response)
  return response

def create_issuing_tx(fromaddr, dest, fee, privatekey, coloramt, specific_inputs, othermeta):
  #ONLY HAS ONE ISSUE
  global tx, tx2, tx3
  amt=dust
  tx=make_raw_one_input(fromaddr,amt,dest,fee, specific_inputs)

  asset_quantities= [coloramt]

  metadata=bitsource.write_metadata(asset_quantities, othermeta).decode('hex')
  position_n=1

  tx2=add_op_return(tx, metadata, position_n)
  print tx2
  tx3=sign_tx(tx2,privatekey)
  print tx3

  response=pushtx(tx3)
  print response
  return response

def create_issuing_tx_unsigned(fromaddr, dest, fee, coloramt, othermeta):
  #ONLY HAS ONE ISSUE
  global tx, tx2, tx3
  amt=dust
  tx=make_raw_transaction(fromaddr,amt,dest,fee)

  asset_quantities= [coloramt]

  metadata=bitsource.write_metadata(asset_quantities, othermeta).decode('hex')
  position_n=1

  tx2=add_op_return(tx, metadata, position_n)
  print tx2
  return tx2

def declaration_tx(fromaddr, fee_each, privatekey, message):
  global specific_inputs
  n_transactions=len(message)/max_op_length+1
  continu=True
  responses=[]
  #PREPARE OUTPUTS
  value_each=0.000105
  specific_inputs=make_multiple_outputs(fromaddr, privatekey, n_transactions+1, value_each, 0.00005)

  for n in range(0,n_transactions):
    if continu:
      indexstart=max_op_length*n
      indexend=indexstart+max_op_length
      if indexend>len(message):
        indexend=len(message)
      specific_input=specific_inputs[n:n+1]
      submessage=str(n)+" "+message[indexstart:indexend]
      #print submessage
      r=send_op_return(fromaddr, fromaddr, fee_each, submessage, privatekey,specific_input)

      if r is None:
        continu=False
      else:
        responses.append(r)
  return specific_inputs

  #send_op_return(fromaddr,fromaddr,fee, message, privatekey)

def create_transfer_tx(fromaddr, dest, fee, privatekey, coloramt, inputs, inputcoloramt, othermeta):
  global tx, tx2, tx3, outputs, sum_inputs

  fee=int(fee*100000000)
  sum_inputs=0
  for x in inputs:
    sum_inputs=x['value']+sum_inputs

  outputs=[]
  transfer={}
  transfer['value']=int(dust*100000000)
  transfer['address']=dest
  outputs.append(transfer)
  colorchange={}
  colorchange['value']=int(dust*100000000)
  colorchange['address']=fromaddr
  outputs.append(colorchange)
  btcchange={}
  btcchange['value']=int(sum_inputs-fee-2*int(dust*100000000))
  btcchange['address']=fromaddr
  if btcchange['value']>=int(dust*100000000):
    outputs.append(btcchange)

  tx=mktx(inputs,outputs)

  asset_quantities=[coloramt, inputcoloramt-coloramt]

  message=bitsource.write_metadata(asset_quantities, othermeta)
  message=message.decode('hex')
  tx2=add_op_return(tx,message, 0)  #JUST TRANSFERS

  for i in range(len(inputs)):
    tx3=sign_tx(tx2,privatekey)
  print tx3
  response=pushtx(tx3)
  return response

def find_transfer_inputs(fromaddr, coloraddress, coloramt, btc):
  available_inputs=databases.dbexecute("SELECT * FROM OUTPUTS WHERE spent='False' and destination_address='"+fromaddr+"' and color_address='"+coloraddress+"';",True)
  totalfound=0
  btc=int(btc*100000000)
  totalavailable=0
  btcfound=0
  btcavailable=0
  answer=[]
  for x in available_inputs:
    totalavailable=totalavailable+x[1]
    btcavailable=btcavailable+x[0]
  if totalavailable>=coloramt and btcavailable>=btc:
    n=0
    while totalfound<coloramt:
      r={}
      r['output']=available_inputs[n][7]
      r['value']=available_inputs[n][0]
      btcfound=btcfound+r['value']
      answer.append(r)
      n=n+1

    while btcfound<btc:
      r={}
      if n<len(available_inputs):
        r['output']=available_inputs[n][7]
        r['value']=available_inputs[n][0]
        answer.append(r)
      n=n+1

  return answer

def transfer_tx(fromaddr, dest, fee, privatekey, coloraddress, coloramt, othermeta):
  btcneeded=fee+dust*4
  inputs=find_transfer_inputs(fromaddr, coloraddress, coloramt, btcneeded)
  result=create_transfer_tx(fromaddr, dest, fee, privatekey, coloramt, )
  return result

def formation_message(colornumber, colorname, ticker, description):
  message="I declare "+str(colorname)+" with ticker: "+str(ticker)+'\nTotal Issued: '+str(colornumber)
  message=message+'\n'+str(description)
  return message

def creation_cost(colornumber, colorname, ticker, description, fee_each, markup):
  message=formation_message(colornumber, colorname, ticker, description)
  n_transactions=len(message)/max_op_length+1
  cost=fee_each  #making outputs
  cost=cost+n_transactions*fee_each  #declaration statements
  cost=cost + fee_each #Issuance to single person
  cost=cost*(1.0+markup)
  return cost

def make_new_coin(fromaddr, colornumber, colorname, destination, fee_each, private_key, ticker, description):
  global tx1, tx
  message=formation_message(colornumber, colorname, ticker, description)
  txs=declaration_tx(fromaddr, fee_each, private_key, message)
  print 'txs below'
  print txs
  specific_inputs=txs[len(txs)-1:len(txs)]  #problem with this
  print ''
  print specific_inputs
  print ''
  tx1=create_issuing_tx(fromaddr, destination, fee_each, private_key, colornumber, specific_inputs, colorname)

  # hashid=tx1
  # if len(hashid)>1:
  #   color_address=''
  #   color_amount=int(colornumber)
  #   source_address=fromaddr
  #   databases.add_color(color_address, source_address, "0", colorname)

  return tx1, specific_inputs
