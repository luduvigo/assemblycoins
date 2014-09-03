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
- api.assets.assembly.com

####Colors
- Make New Coin Directly with Server Side Transaction Signing
  - POST /v1/colors/
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
  - POST /v1/colors/prepare
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


- #####Check Holders of particular Coin Type
  - /v1/colors/"color_address"

  - Response
    - {"1PaCGhg1JtD4C6LrRLozjSDe5T2Uco1cAJ": 4, "19HjNMysWnjr5dpNhJxp7CZ4RejTkCsby6": 6}


- See metadata for all known Colors
  - GET /v1/colors/

      - Response
        - {{"color_address": "3PXkWCL7u9Kk64ZzUZJ5NJqMzSgkzWksaU", "source_address": "1F9CiWC8BntEA4LvmcoqdJcvk5RhU26cdG", "total_issued": 200}, {"color_address": "3LAb9XysmxeXpvKcjZ2rNW9dYPxc4kGZgx", "source_address": "1JG6snkARzfCR8J82duRjNsNfj8NTNaVFM", "total_issued": 80000}]}


####Addresses

- #####Check Address Balances
  - /v1/addresses/"public_address"

  - Response
    - {"19ZDdoBR2nQWMLNzy6yspQG622mN8wAU1p": {"3H1nMbUwsT99twBATmoVrLLK8eM9eW6y3y": 30000000}}


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
      - curl http://bitwrangle.herokuapp.com/v1/colors/transfer \
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
    - curl http://bitwrangle.herokuapp.com/v1/transactions \
     -X POST \
     -d "transaction_hex="

      - Response
        

####Messages

####Meta
