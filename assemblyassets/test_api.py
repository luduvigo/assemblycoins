import requests
import databases as db
import main
import addresses

#test connection to colordb
def test_colordb_connected():
  a=db.dbexecute("SELECT * FROM meta;",True)
  print "COLOR DB NOT RESPONDING"
  assert len(a)>0

#test that color_db is up to date, at least according to meta
def test_meta_lastblockdone():
  blockchain_blockcount=requests.get("https://blockchain.info/q/getblockcount").content
  lastblockdone=db.dbexecute("SELECT * FROM meta;",True)
  try:
    lastblockdone=lastblockdone[0][0]
  except:
    lastblockdone=-1
  print "Color DB is not up to date, stuck at "+str(lastblockdone)+" out of "+str(blockchain_blockcount)
  assert int(lastblockdone)==int(blockchain_blockcount)

#TEST READING MESSAGES IN BLOCKCHAIN
def test_address_messages():
  found=addresses.read_opreturns_sent_by_address("1N8onLuitcQR9V3HB9QSARyFV6hwxA99Sx")
  should_be='{"name": "pillars", "desc": "one small step", "total": 52352}'
  assert found==should_be


#TEST A KNOWN COLOR ADDRESS
def test_color_lookup():
  color_address=""
  data=requests.get("https://assets.assembly.com/v1/colors/"+str(color_address)).content

#Test a KNOWN TRANSACTION
def test_tx_lookup():
  url="http://assets.assembly.com/v1/transactions/88b73f03d6c594dd2e328a140a189533de52f97dccada45811554fbc6df7d802"
  data=requests.get(url).content
  should_be='{"outputs": [{"destination_address": "14vce6XiQzJ51cTKU1Dsj1X48hSdCTCq6Y", "previous_input": "source:14vce6XiQzJ51cTKU1Dsj1X48hSdCTCq6Y", "spent_at_txhash": "", "blockmade": 321435, "btc": 601, "blockspent": null, "txhash_index": "88b73f03d6c594dd2e328a140a189533de52f97dccada45811554fbc6df7d802:0", "color_amount": 1337, "txhash": "88b73f03d6c594dd2e328a140a189533de52f97dccada45811554fbc6df7d802", "color_address": "3EKq4ecPqg33gzVkd4KaWe8oicVTkG1XUd", "spent": false}]}'
  assert data==should_be
