## Setup

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt --allow-all-external
    $ cp .env.sample .env
    $ # edit .env
    $ forego start

##API Calls

####API ROOT
- api.assets.assembly.com

####Colors

- #####Prompt API Server for New Coin Issuing Address
  - POST /v1/colors/prepare
    >    curl https://api.assets.assembly.com/v1/coins/prepare \
    > -X POST \
    > -d "coin_name"="mikoin" \
    > -d "issued_amount=999" \
    > -d "destination_address=TESTD" \
    > -d "description=letsdoit" \
    > -d "email=barisser@gmail.com"

      - Response
        {"name": "mikoin", "issuing_private_key": "5KUABpsoZKMqpvm3yFe9Zg52QXhXY8Xw8pa4ntuK7SBdVt7CkrK", "minting_fee": "0.0004", "issuing_public_address": "1EmnqhfvjcAdA71gs2exugXkgHrJw9QcuA"}


- #####Check Holders of particular Coin Type
  - /v1/colors/"color_address"

  - Response
    - {"1PaCGhg1JtD4C6LrRLozjSDe5T2Uco1cAJ": 4, "19HjNMysWnjr5dpNhJxp7CZ4RejTkCsby6": 6}


- See metadata for all known Colors
  - GET /v1/colors/
      curl https://api.assets.assembly.com/v1/colors/3A5JTQS7ereJSfJCa6CVP8VNVSndyQD92s

    - Response
      - {"19aa71ZGwxTBDtazTKCHQvKoVJoEq71tEy": 1}


- Make New Coin Directly with Server Side Transaction Signing
  - POST /v1/colors/
      curl https://api.assets.assembly.com \
      -X POST \
      -d "public_address=1C1YLvSwh2imUsGnJ8qno1XgTKZMgcTcbp" \
      -d "initial_coins=137"  \
      -d "name=augusto"  \
      -d "recipient=173CJ9wxuZFbJyDbkJ89AfpAkqx5PatxMk" \
      -d "private_key=YOUR PRIVATE KEY HERE" \
      -d "description=Hey what a cool coin"

  - Response
    - "b9d3b5e409224eb1f1317932f7aaf97bad59510d5f7ecb4b83856d93f9a274f5"


####Addresses

- #####Check Address Balances
  - /v1/addresses/"public_address"
    curl https://api.assets.assembly.com/v1/addresses/1CEyiC8DXT6TS3d9iSDnXRBtwyPuVGRa9P

  - Response
    - {"1CEyiC8DXT6TS3d9iSDnXRBtwyPuVGRa9P": {"3N2bUx2XCWBfXzNd3YiDpFVAHQtSi1Yj5w": 10000}}


- Generate Public/Private Address Pair
  - GET /v1/addresses/

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


####Transactions


- #####Transfer Colored Coins with Server Side signing
  - POST /v1/transactions/transfer
      - curl https://api.assets.assembly.com/v1/colors/transfer \
        X POST \
        -d "from_public_address=" \
        -d "from_private_key= "  \
        -d "amount=" \
        -d "source_address=" \
        -d "to_public_address="

      - Response
        {}

- Push Raw Transaction to Bitcoin Network
  - POST /v1/transactions
    - curl https://api.assets.assembly.com/v1/transactions \
     -X POST \
     -d "transaction_hex="

      - Response


####Messages

  - /v1/messages/"public_address"
    - curl https://api.assets.assembly.com/v1/messages/1N8onLuitcQR9V3HB9QSARyFV6hwxA99Sx

    - Response
        - {"statements": "{\"name\": \"pillars\", \"desc\": \"one small step\", \"total\": 52352}"}

  - POST '/v1/messages/'
    - curl https://api.assets.assembly.com/v1/messages \ -X POST \
      -d "public_address=" \ -d "fee_each=0.00005" \ -d "private_key=" \ -d "message="


####Meta
