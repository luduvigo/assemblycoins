## Setup

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt --allow-all-external
    $ cp .env.sample .env
    $ # edit .env
    $ forego start

##API Calls

####API ROOT
- bitwrangle.herokuapp.com

####Colors
- Make New Coin Directly with Server Side Transaction Signing
  - POST /v1/colors/makenew
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


- #####Prompt API Server for New Coin Issuing Address
  - POST /v1/coins/prepare
    >    curl http://bitwrangle.herokuapp.com/v1/coins/prepare \
    > -X POST \
    > -d "coin_name"="mikoin" \
    > -d "issued_amount=999" \
    > -d "destination_address=TESTD" \
    > -d "description=letsdoit" \
    > -d "ticker=TST" \
    > -d "email=barisser@gmail.com"

      - Response
        {"name": "mikoin", "issuing_private_key": "5KUABpsoZKMqpvm3yFe9Zg52QXhXY8Xw8pa4ntuK7SBdVt7CkrK", "minting_fee": "0.0004", "issuing_public_address": "1EmnqhfvjcAdA71gs2exugXkgHrJw9QcuA"}


- #####Transfer Colored Coins with Server Side signing
  - POST /v1/colors/transfer
      - curl http://bitwrangle.herokuapp.com/v1/colors/transfer \
        X POST \
        -d "from_public_address=" \
        -d "from_private_key= "  \
        -d "amount=" \
        -d "color_address=" \
        -d


####Addresses

- #####Check Address Balances
  - /v1/addresses/"public_address"

  - Response
    - {"3PCYV99KrPxGK61ZjqLBRgtqiG7F3wKSGT": 50000000}


- #####Check Holders of particular Coin Type
  - /v1/colors/"color_address"

  - Response
    - {"14bVh46DdUapEJyCCTf7qMu8tndYcBXqN6": 50000000}



- Generate Public/Private Address Pair
  - GET /v1/addresses/generate

    - Response
      {'private_key': '5Hs2ztSw4T239kH2jDmm7nBTqycmsaVzQSxsE4MYrv3ogVhuM5J', 'public_address': '1JfMoC98NTxYiHwMDoA3TTiiW5cf7rXApY'}


- #####Read stitched-together multi-part OP_RETURN statements issued by an address
  - GET /v1/colors/statements/"public_address"
    - Response
        - I declare augusto with ticker: aug Total Issued: 137 hey


- OP_RETURN messages sent by address
  - GET /v1/messages/"public_address"

   - Response
      - [[message, txhash]]
      - [['aiueo', '16a1d36da5b35a9f993d69febb7b10a45c5a1a3fc57c6f45b207f9befc9114fc:2']]
