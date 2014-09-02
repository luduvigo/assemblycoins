import requests
import json
import addresses
import transactions
import bitsource
import databases
import node

#HERE I USE BLOCKCHAIN.INFO, GO TO BITSOURCE FOR NODE VERSION

def getblock_blockchain(blockn):
  url='http://blockchain.info/block-height/'+str(blockn)+'?format=json'
  data=requests.get(url)
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
  counter=0
  for tx in txs:
    message=''

    #print "TXs: "+str(counter)+" / "+str(data['n_tx'])
    counter=counter+1

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
          if 'prev_out' in x:
            amount=amount+x['prev_out']['value']

        results.append([str(tx['hash'])+":"+str(n),message, amount])
      n=n+1

  return results

def oa_in_block(blockn):
  opreturns=opreturns_in_block(blockn)
  oatxs=[]
  for x in opreturns:
    if x[1][0:2]=='OA':
      try:
        parsed=bitsource.parse_colored_tx(x[1], x[0])
      #take txhash, find address corresponding to parsed metadata colored behavior
        oatxs.append([x[0],parsed,x[2]])  #TXHASH_WITH_INDEX, METADATA PARSED,  BTC CONTENT,  OUTPUT ADDRESSES as array
      except:
        "Invalid OA TX detected"
  return oatxs

#def add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade):

def add_output_db(blockn):
  results=oa_in_block(blockn)

  for tx in results:
    try:
      if 'issued' in tx[1]:
        for outputs in tx[1]['issued']:
          #ISSUED FIRST, no check necessary

          btc=str(outputs['btc'])
          coloramt=str(outputs['quantity'])
          coloraddress=str(outputs['color_address'])   #THIS WORKED!
          spent="False"
          spentat=""
          destination=str(outputs['destination_address'])
          txhash=str(tx[0][0:len(tx[0])-2])
          txhash_index=str(outputs['txhash_index'])
          blockmade=str(blockn)
          prev_input=outputs['previous_inputs']
          databases.add_output(btc,coloramt,coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade, prev_input)

          #ADD NEW ISSUED to COLORS META INFO
          oldamount=databases.read_color(coloraddress)
          if len(oldamount)==0:
            source_address=outputs['previous_inputs'][outputs['previous_inputs'].index(':')+1:len(outputs['previous_inputs'])]
            databases.add_color(coloraddress, source_address, coloramt, "color_name")
          else:
            oldamount=oldamount[0][2]
            databases.edit_color(coloraddress, int(oldamount)+int(coloramt))

        for inps in tx[1]['transferred']:
          #TRANSFERS
          btc=str(inps['btc'])
          coloramt=str(inps['quantity'])
          coloraddress=str(inps['color_address'])
          spent="False"
          spentat=""
          destination=str(inps['destination_address'])
          #print tx
          txhash=str(tx[0][0:len(tx[0])-2])
          txhash_index=str(inps['txhash_index'])
          blockmade=str(blockn)

          prev_inputs=inps['previous_inputs']
          #print prev_inputs

          # totalin=0
          # inputlist=[]
          # for x in prev_inputs:  #for each previnput txhash_with_index
          #   print "CHECKING PREV INPUT: "+str(x)
          #   old=databases.read_output(x,False)   #read that input
          #   print old
          #   if len(old)>0:   #if it is found in the DB
          #     old=old[0]  #get that element
          #     totalin=totalin+old[1]   #add its color amount to the total inputted
          #     coloraddress=databases.dbexecute("SELECT color_address from outputs WHERE txhash_index='"+x+"';",True)[0][0]   #get the color address of that input
          #     inputlist.append([x,old[1], coloraddress])  #append it to the total list
          #
          #   print inputlist

          #CHECK AMT ON PREVIOUS INPUT
              #oldamt=databases.read_output(prev_input, True)

          totalin=int(coloramt) #so it always passes
          if totalin>=int(coloramt): #LEGITIMATE
            #ADD NEW OUTPUT
            print "color address"+str(coloraddress)

            prev_input="FIX HERE"

            #decide which inputs to spend
            totalspent=0
            inputcounter=0
            cont=True
            while int(coloramt)-totalspent>0 and cont:
              if inputcounter<len(inputlist):
                prev_input=inputlist[inputcounter][0]
                totalspent=totalspent+inputlist[inputcounter][1]
                databases.add_output(btc,coloramt,coloraddress,spent,spentat,destination,txhash,txhash_index, blockmade, prev_input)
                inputcounter=inputcounter+1
              elif inputcounter>=len(inputlist):
                cont=False


            #MARK OLD OUTPUT AS SPENT
            #print str(prev_input)+"  "+str(txhash)
            databases.spend_output(prev_input, txhash, blockn)


          else:
            print "ILLEGITIMATE TX: "+str(tx[0])
            print str(totalin)+" / "+str(coloramt)

        previnplist=[]
        for previnps in tx[1]['transferred']:
          for x in previnps['previous_inputs']:
            previnplist.append([x,previnps['txhash_index']])
        for x in previnplist:
          databases.spend_output(x[0], x[1], blockn)
      else:
        print "Invalid OA TX cannot be processed: " +str(tx)+"   END "
    except:
      databases.dbexecute("insert into errors (txhash) values ('"+tx[0]+"')")

  #CHECK BLOCK SPENT TXS FOR VERACITY AT END OF BLOCK
  for tx in results:
    for inps in tx[1]['transferred']:
      prev_inputs=inps['previous_inputs']
      totalin=0
      inputlist=[]
      for x in prev_inputs:  #for each previnput txhash_with_index
        print "CHECKING PREV INPUT: "+str(x)
        old=databases.read_output(x,False)   #read that input
        print old
        if len(old)>0:   #if it is found in the DB
          old=old[0]  #get that element
          totalin=totalin+old[1]   #add its color amount to the total inputted
          coloraddress=databases.dbexecute("SELECT color_address from outputs WHERE txhash_index='"+x+"';",True)[0][0]   #get the color address of that input
          inputlist.append([x,old[1], coloraddress])  #append it to the total list

        print inputlist

    coloramt=str(inps['quantity'])
    if totalin>=int(coloramt):
      #everything was OK
      h=0
    else:
      txhash_index=str(outputs['txhash_index'])
      print "ILLEGITIMATE TX DETECTED "+txhash_index

def output_db(blockn):
    #ADD OUTPUTS TO DB assuming correctness
    txdata=oa_in_block(blockn)
    for tx in txdata:
      try:
        #ISSUED
        for txissued in tx[1]['issued']:
          coloraddress = txissued['color_address']
          btc= str(txissued['btc'])
          coloramt = str(txissued['quantity'])
          spent=str(False)
          spentat=""
          destination=str(txissued['destination_address'])
          txhash_index=str(txissued['txhash_index'])
          txhash = txhash_index[0:len(txhash_index)-2]
          blockmade=str(blockn)
          prev_input=txissued['previous_inputs']
          databases.add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade, prev_input)

          #EDIT COLOR OVERVIEW DATA
          oldamount=databases.read_color(coloraddress)
          if len(oldamount)==0:
            source_address=prev_input[7:len(prev_input)]
            databases.add_color(coloraddress, source_address, coloramt, "color_name")
          else:
            oldamount=oldamount[0][2]
            databases.edit_color(coloraddress, int(oldamount)+int(coloramt))

        #TRANSFERRED
        for txtransfer in tx[1]['transferred']:
          coloraddress=txtransfer['color_address']
          btc=str(txtransfer['btc'])
          coloramt=str(txtransfer['quantity'])
          spent=str(False)
          spentat=""
          destination=txtransfer['destination_address']
          txhash_index=txtransfer['txhash_index']
          txhash=txhash_index[0:len(txhash_index)-2]
          blockmade=str(blockn)
          prev_input=txtransfer['previous_inputs']
          databases.add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade, prev_input)
      except:
        databases.dbexecute("insert into errors txhash values ('"+tx[0]+"');",False)

    #after entire block is processed check that the sums match, SPEND SPENT OUTPUTS
    recentlyaddedtxs=databases.dbexecute("SELECT txhash FROM OUTPUTS WHERE blockmade="+str(blockn)+";", True)

      #FIND TX (not outputs but parent) and SUM TOTAL IN
    for tx in recentlyaddedtxs:
      txhash=tx[0]
      #sum total in
      totalin=0
      inputs=databases.dbexecute("SELECT previous_input from outputs where txhash='"+txhash+"';",True)
      for inpa in inputs:
        for inp in inpa:
          if inp[0:7]=="source:": #WAS ISSUED, need not be check
            totalin=999999999999
          else:
            inp=inp.split("_")
            inp=inp[0:len(inp)-1]
            for x in inp:
              dbstring="SELECT color_amount from outputs where txhash_index='"+x+"';"
              #print dbstring
              colinps=databases.dbexecute(dbstring,True)
              for colinp in colinps:
                totalin=totalin+colinp[0]

      #THEN SUM TOTAL OUT
      outps=databases.dbexecute("SELECT color_amount from outputs where blockmade="+str(blockn)+" and txhash='"+txhash+"'", True)
      totalout=0
      for outp in outps:
        totalout=totalout+outp[0]
      #IF TOTALIN>= TOTAL OUT, its OK, else, SPENT ALL OUTPUTS AND UNSPEND ALL INPUTS

      if totalout<=totalin:
        #everything OK
        print "legit tx: "+str(tx)

        #SPEND INPUTS FINALLY
        inputs=databases.dbexecute("SELECT previous_input from outputs where txhash='"+txhash+"';",True)
        for inp in inputs:
          for x in inp:
            if not x[0:7]=="source:":
              x=x.split("_")
              x=x[0:len(inputs)-1]
              for y in x:
                databases.spend_output(str(y), txhash,blockn)

      else:
        print "ILLEGITIMATE TX DETECTED: "+str(tx)
        #spend outputs
        #databases.spend_output()




def blocks_outputs(blockend):
  lastblockprocessed=databases.dbexecute("SELECT * FROM META;",True)
  currentblock=node.connect('getblockcount',[])
  if blockend>currentblock:
    blockend=currentblock
  for i in range(lastblockprocessed[0][0]+1,blockend+1):
    add_output_db(i)
    print "processed block "+str(i)
    databases.dbexecute("UPDATE META SET lastblockdone='"+str(i)+"';",False)

def more_blocks(moreblocks):
    currentblock=node.connect('getblockcount',[])
    lastblockprocessed=databases.dbexecute("SELECT * FROM META;",True)
    nextblock=lastblockprocessed[0][0]+moreblocks
    if nextblock>currentblock:
      nextblock=currentblock
      for i in range(lastblockprocessed[0][0]+1, nextblock+1):
        try:
          output_db(i)
          print "processed block "+str(i)
          databases.dbexecute("UPDATE META SET lastblockdone='"+str(i)+"';",False)
        except:
          print "error updating db"
    elif nextblock<=currentblock:
      for i in range(lastblockprocessed[0][0]+1, nextblock+1):
        #try:
        output_db(i)
        print "processed block "+str(i)
        databases.dbexecute("UPDATE META SET lastblockdone='"+str(i)+"';",False)
        #except:
          #print "error updating db"

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
      specific_inputs=txdata[1]['output']  #THIS IS CRUCIAL IN FINDING COLOR ADDRESS

      #mark as completed
      databases.edit_address(fromaddr, value, value, colornumber)

      #add entry to colors db
      #referencehex=bitsource.tx_lookup(specific_inputs)
      color_address=bitsource.script_to_coloraddress()
      databases.add_color(color_address, fromaddr, colornumber, colorname)

      #add entry to outputs db

      #send profits elsewhere
      # extra=
      # transactions.make_raw_transaction(fromaddr,extra,profit_address, 0.00003)
