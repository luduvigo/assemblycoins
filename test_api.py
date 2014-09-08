import requests
import node
import databases as db

#test reading node for block count,   shows that node is current
def test_block_count():
  blockchain_blockcount=requests.get("https://blockchain.info/q/getblockcount").content
  my_blockcount=node.connect("getblockcount",[])
  print "Testing Communication with Bitcoin Node"
  assert int(blockchain_blockcount)==int(my_blockcount)

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

# #test reading an output (that is already spent so immutable)
# def test_readoutput():
#   txhash="7e15f1ded0192e3223ce5589e4948d1713554d7c7142963b994a70cebf80e05a"
#   result=requests.get("https://assets-api.assembly.com/v1/transactions/"+txhash)
#   result=result.content
#   expected='{"outputs": [{"spent_at_txhash": "b48548aa33640b756c827f5998cd58d3b23b19acff3a208ec663c2eb2bebfdd0", "destination_address": "1ARyJPCkaa4cQHxjeZYApRL2CuGWhyrLX5", "blockmade": 300320, "previous_input": "source:1ARyJPCkaa4cQHxjeZYApRL2CuGWhyrLX5", "blockspent": 300712, "btc": 600, "txhash_index": "7e15f1ded0192e3223ce5589e4948d1713554d7c7142963b994a70cebf80e05a:0", "color_amount": 1000000, "color_address": "3JxzvzjFgbJzxv2rEJnfVpriuX6DQhTnTq", "txhash": "7e15f1ded0192e3223ce5589e4948d1713554d7c7142963b994a70cebf80e05a", "spent": true}]}'
#   print "output DB not responding correctly to parsed color data"
#   assert result==expected
