##API Calls

####API ROOT
- bitwrangle.herokuapp.com

####Colors
- Make New Coin Directly with Server Side Transaction Signing
  - POST /colors/makenew
      curl http://bitwrangle.herokuapp.com \
      -X POST \
      -d "public_address=1C1YLvSwh2imUsGnJ8qno1XgTKZMgcTcbp" \
      -d "initial_coins=137"  \
      -d "name=augusto"  \
      -d "recipient=173CJ9wxuZFbJyDbkJ89AfpAkqx5PatxMk" \
      -d "private_key=YOUR PRIVATE KEY HERE" \
      -d "ticker=AUG" \
      -d "description=Hey what a cool coin"

  - Response
    - "b9d3b5e409224eb1f1317932f7aaf97bad59510d5f7ecb4b83856d93f9a274f5"


- Prompt API Server for New Coin Issuing Address
  - POST /v1/coins/prepare
    >    curl http://bitwrangle.herokuapp.com/v1/coins/prepare \
    > -X POST \
    > -d "coin_name"="mikoin" \
    > -d "public_address=TEST" \
    > -d "private_key=TESTP" \
    > -d "issued_amount=999" \
    > -d "destination_address=TESTD" \
    > -d "description=letsdoit" \
    > -d "ticker=TST" \
    > -d "email=barisser@gmail.com"


####Addresses
- Generate Public/Private Address Pair
  - GET /addresses/generate

    - Response
      {'private_key': '5Hs2ztSw4T239kH2jDmm7nBTqycmsaVzQSxsE4MYrv3ogVhuM5J', 'public_address': '1JfMoC98NTxYiHwMDoA3TTiiW5cf7rXApY'}
