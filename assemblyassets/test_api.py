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
