import sys
sys.path.insert(0, '..')

import requests
import databases as db
import main
import addresses
import json

#TEST KNOWN PUBLIC ADDRESS
def test_public_lookup():
  public_address="1CEyiC8DXT6TS3d9iSDnXRBtwyPuVGRa9P"
  url="https://coins.assembly.com/v1/addresses/"+str(public_address)
  should_be='{"public_address": "1CEyiC8DXT6TS3d9iSDnXRBtwyPuVGRa9P", "assets": [{"quantity": 10000, "color_address": "3N2bUx2XCWBfXzNd3YiDpFVAHQtSi1Yj5w"}]}'
  data=requests.get(url).content
  assert str(data)==should_be

#TEST A KNOWN COLOR ADDRESS
def test_color_lookup():
  color_address="3EKq4ecPqg33gzVkd4KaWe8oicVTkG1XUd"
  data=requests.get("https://coins.assembly.com/v1/colors/"+str(color_address)).content
  should_be='{"owners": [{"quantity": 1337, "public_address": "14vce6XiQzJ51cTKU1Dsj1X48hSdCTCq6Y"}], "color_address": "3EKq4ecPqg33gzVkd4KaWe8oicVTkG1XUd"}'
  assert str(data)==should_be

#Test a KNOWN TRANSACTION
def test_tx_lookup():
  url="https://coins.assembly.com/v1/transactions/88b73f03d6c594dd2e328a140a189533de52f97dccada45811554fbc6df7d802"
  data=requests.get(url).content
  should_be='{"outputs": [{"color_amount": 1337, "color_address": "3EKq4ecPqg33gzVkd4KaWe8oicVTkG1XUd", "destination_address": "14vce6XiQzJ51cTKU1Dsj1X48hSdCTCq6Y", "blockmade": 321435, "spent_at_txhash": "", "txhash_index": "88b73f03d6c594dd2e328a140a189533de52f97dccada45811554fbc6df7d802:0", "btc": 601, "spent": false, "txhash": "88b73f03d6c594dd2e328a140a189533de52f97dccada45811554fbc6df7d802", "blockspent": null, "previous_input": "source:14vce6XiQzJ51cTKU1Dsj1X48hSdCTCq6Y"}]}'
  assert data==should_be

