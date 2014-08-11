import addresses
import requests
import json
from bitcoin import *
import node
import bitsource
import cointools

dust=5461*0.00000001
max_op_length=33 #in bytes

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

def make_raw_one_input(fromaddress,amount,destination,fee, specific_input):
  global ins, outs
  fee=int(fee*100000000)
  amount=int(amount*100000000)
  #unspents=unspent(fromaddress)
  #unspents=[unspents[input_n]]
  unspents=[specific_input]

  ins=[]
  ok=False
  outs=[]
  totalfound=0
  for unsp in unspents:
     if not ok:
           ins.append(unsp)
           if unsp['value']>=fee+amount-totalfound:
              if amount>totalfound:
                outs.append({'value':amount-totalfound,'address':destination})
              if unsp['value']>fee+amount-totalfound:
                 if unsp['value']-amount-fee>0:
                   outs.append({'value':unsp['value']-amount-fee,'address':fromaddress})
              ok=True
              totalfound=fee+amount
           else:
              if unsp['value']>0:
                outs.append({'value':unsp['value'],'address':destination})
              totalfound=totalfound+unsp['value']


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
  outs.append({'value': change_amount, 'address': fromaddress})
  tx=mktx(ins,outs)
  return tx

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

def send_op_return(fromaddr, dest, fee, message, privatekey, input_n):
  #specific_input=cointools.unspent(fromaddr)
  #specific_input=specific_input[specific_input_n]

  #tx=make_raw_one_input(fromaddr,dust,dest,fee, specific_input)

  tx=make_raw_one_input(fromaddr, dust, dest, fee, the_input)

  tx2=add_op_return(tx,message,1)
  tx3=sign_tx(tx2,privatekey)
  response=pushtx(tx3)
  #print "Trying to push op return: "
  #print tx3
  print "Response: "+str(response)
  return response

def create_issuing_tx(fromaddr, dest, fee, privatekey, coloramt, input_n, othermeta):
  #ONLY HAS ONE ISSUE
  global tx, tx2, tx3
  amt=dust
  tx=make_raw_transaction(fromaddr,amt,dest,fee)

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

def declaration_tx(fromaddr, fee_each, privatekey, message, specific_inputs):
  n_transactions=len(message)/40+1
  continu=True

  #PREPARE OUTPUTS
  # newoutputs=[]
  # noutputs=n_transactions
  # eachoutput=0.00006
  # tx=make_raw_multiple_outputs(fromaddr, noutputs, eachoutput, fromaddr, fee_each)
  # tx=sign_tx(tx,privatekey)
  # r=pushtx(tx)
  # for i in range(0,n_transactions):
  #   newoutputs.append(r+":"+str(i))

  for n in range(0,n_transactions+1):
    if continu:
      indexstart=max_op_length*n
      indexend=indexstart+max_op_length
      if indexend>len(message):
        indexend=len(message)
      specific_input=specific_inputs[n]
      submessage=str(n)+" "+message[indexstart:indexend]
      #print submessage
      r=send_op_return(fromaddr, fromaddr, fee_each, submessage, privatekey,specific_input)

      if r is None:
        continu=False

  #send_op_return(fromaddr,fromaddr,fee, message, privatekey)

def create_transfer_tx(fromaddr, dest, fee, privatekey, coloramt, inputs, inputcoloramt):
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
  othermeta='DethKoins'

  message=bitsource.write_metadata(asset_quantities, othermeta)
  message=message.decode('hex')
  tx2=add_op_return(tx,message, 0)  #JUST TRANSFERS

  for i in range(len(inputs)):
    tx3=sign_tx(tx2,privatekey)

  response=pushtx(tx3)
  return response

def make_new_coin(fromaddr, colornumber, colorname, destination, fee_each, private_key):
  global tx1
  declaration_message='I declare '+str(colorname)+"!"
  tx=send_op_return(fromaddr, fromaddr, fee_each, declaration_message, private_key, 0)
  print tx

  tx1=create_issuing_tx(fromaddr, destination, fee_each, private_key, colornumber, 1, colorname)
  print tx1

  return tx


pp=addresses.generate_privatekey('AssemblyForged')
pu=addresses.generate_publicaddress('AssemblyForged')

private_key= addresses.generate_privatekey('AssemblyWrought')
public_address=addresses.generate_publicaddress('AssemblyWrought')

m="Australia is the world's second favourite desert wasteland with only one or two interesting cities and a medium level of social-censorship, behind the UAE."
dest=addresses.generate_publicaddress('DaveNewman')
#make_new_coin(public_address, 50001, 'KiwiShillings',dest , 0.0001, private_key)

pub=addresses.generate_publicaddress('AssemblyMade')
priv=addresses.generate_privatekey('AssemblyMade')

daves_public='1G5FXBRLj9BDZWao9pj5JCA8brcuRcRYo'

#create_issuing_tx(pub,dest, 0.0002, priv, 1111111,0,'DarkCoins')
#m='oh herro'
#send_op_return(pub,dest,0.0001, m,priv,0)

#KEYS
# 'AndrewBarisser'   , 'TimurFisk'.   'AssemblyMade'.   'AssemblyWrought', 'DaveNewman'
