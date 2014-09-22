## Setup

    $ pip install assemblycoins

##Test

    $ py.test


##API Calls

####API ROOT
- coins.assembly.com

####Colors

- #####Prompt API Server for New Coin Issuing Address
  - POST /v1/colors/prepare


    curl https://coins.assembly.com/v1/colors/prepare \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{
          "issued_amount": 555,
          "description": "Order over Chaos",
          "coin_name": "mikoin",
          "email": "Gottfried@Leibniz.com"
        }'

    Response
    {
      "issuing_private_key": "5JczQYvFVAoGgGFJxEu6qQGUNCvKp8VmqMPtpnGfTFVmQxcvcBi",
      "name": "mikoin",
      "minting_fee": "0.00043606",
      "issuing_public_address": "1KDqfRmheS6jcq6XYDeiWfF3yako8AJKUa"
    }

- #####Check Holders of particular Coin Type
  - /v1/colors/"color_address"
    OR
    /v1/colors/"source_address"


    curl https://coins.assembly.com/v1/colors/32dCTMMrW7XPVrfbfJtguo6LN9sg8mvttq

    Response
    {
      "color_address": "32dCTMMrW7XPVrfbfJtguo6LN9sg8mvttq",
      "owners":
        [
          {
            "quantity": 6,
            "public_address": "1DzZ7DFJ4yrMzVw4ws8PdmmtqqfTnjprLB"
          },
          {
            "quantity": 4,
            "public_address": "1PaCGhg1JtD4C6LrRLozjSDe5T2Uco1cAJ"
          }
        ]
    }

- #####Make New Coin Directly with Server Side Transaction Signing

  - POST /v1/colors/


    curl https://coins.assembly.com \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{
          "public_address": "1EUV2AXvJRtyDb9j4s7nsxbs9S1MKb3EnU",
          "private_key": "5JMFFPgzjgKHkKnGvTRB1aaiBhRu9Tq6ZC28Gj5v9DK5PBzSwTD",
          "name": "OneKoin",
          "initial_coins": 9,
          "description": "One Coin to Rule Them All",
          "email": "Gandalf@MiddleEarth.mid",
          "fee_each": 0.00005
        }'

    Response
    {
      "name": "OneKoin",
      "minting_fee": "0.0003",
      "issuing_public_address": "1EUV2AXvJRtyDb9j4s7nsxbs9S1MKb3EnU",
      "issuing_private_key": "5JMFFPgzjgKHkKnGvTRB1aaiBhRu9Tq6ZC28Gj5v9DK5PBzSwTD"
    }


####Addresses

- #####Check Address Balances
  - /v1/addresses/"public_address"


    curl https://coins.assembly.com/v1/addresses/1CEyiC8DXT6TS3d9iSDnXRBtwyPuVGRa9P

    Response
    {
      "public_address": "1CEyiC8DXT6TS3d9iSDnXRBtwyPuVGRa9P",
      "assets":
        [
          {
            "color_address": "3N2bUx2XCWBfXzNd3YiDpFVAHQtSi1Yj5w",
            "quantity": 10000
          }
        ]
    }

- #####Generate Public/Private Address Pair
  - /v1/addresses/


    curl https://coins.assembly.com/v1/addresses

    Response
    {
      "public_address": "15EZotfUZjsT6RiYryTjwJ64WwW2MbRXRe",
      "private_key": "5JMFFPgzjgKHkKnGvTRB1aaiBhRu9Tq6ZC28Gj5v9DK5PBzSwTD"
    }

- #####Generate Public/Private Address Pair from Phrase
USE WITH CAUTION, only use very complex phrases!
  - /v1/addresses/brainwallet/"your_phrase"


    curl https://coins.assembly.com/v1/addresses/brainwallet/password1

    Response
    {
      "public_address": "19VAb9zAhpWLaWfEuqw9HXup2zaNoNPPyE",
      "private_key": "5HuAe6SqbZHxWJNHZ9YMxW7dFp97PdzMD2uTHChLd1nXJPS5dsR"
    }

####Transactions


- #####Transfer Colored Coins with Server Side signing
  - POST /v1/transactions/transfer


    curl https://coins.assembly.com/v1/transactions/transfer \
      -X POST \
      -H "Content-Type: application/json" \
      -d `{ \
            "from_public_address":"16ucRhebuqcoDngLoZNwz2d6TjtNnLunKE", \
            "from_private_key":"YOUR PRIVATE KEY HERE", \
            "transfer_amount":10, \
            "source_address":"16ucRhebuqcoDngLoZNwz2d6TjtNnLunKE", \
            "fee_each":0.00005, \
            "to_public_address":"17pnsRJSq23xeYW8nZdgZzmofJXr2A5wMB", \
            "callback_url":"http://www.yourserver.com" \
      }`

        Callback URL term is optional.  If specified, you will receive a JSON POST with more specific transaction hash information when the transaction is processed

    Response
      {"result": "Queued"}

    CallBack Response
      {
      "transaction_hash": "09cb295b51331eed9f9bc2b3215b1787d79f70bdc45766a7b32be1da1c84cec7"
      }


- #####Push Raw Transaction to Bitcoin Network
  - POST /v1/transactions


    curl https://coins.assembly.com/v1/transactions \
     -X POST \
     -H "Content-Type: application/json" \
     -d '{
          "transaction_hex": ""
          }'

    Response
      {
        "transaction_hash":"ac96267f7790d8d7459c0aae6160ab88458e03050d7f31d8b7310f32ebecb261"
      }

  - #####Parsed Open Assets Transactions in Block
    - /v1/transactions/parsed/"Block Height"


    curl https://coins.assembly.com/v1/transactions/parsed/300712

    Response
    {
      "parsed_transactions":
        [
          {"transaction_hash_with_index": "762c54aa55513b647e831ab91ac03ed3117525fedc5b5f45fb0f50bc9439518b:1",
          "parsed_colored_info": {
                                  "transferred": [],
                                  "asset_quantities": [2],
                                  "version": "0100",
                                  "type": "OA",
                                  "issued": [
                                              {
                                                "color_address": "38PfLkHYC2gb98ZXdVtvDJQ1dk6Eh75Zcf",
                                                "destination_address": "13LW8Y8GQzZueF6LKSgtgqcUXoxEL7puyY",
                                                "previous_inputs": "source:1mpC4oLBmvMNcdK4jmSAAxMA62mSsfMvv",
                                                "quantity": 2,
                                                "btc": 600,
                                                "txhash_index": "762c54aa55513b647e831ab91ac03ed3117525fedc5b5f45fb0f50bc9439518b:0"
                                              }
                                            ],
                                  "metadata_length": 27,
                                  "asset_count": 1,
                                  "metadata": "u=https://cpr.sm/NR64BLo62v"
                                  }
          },
          {
            "transaction_hash_with_index": "0f0169b34fe25f3ae76342c1f3b865f0d920b823daf891693830057aa90bef32:1",
            "parsed_colored_info": {
                                    "transferred": [],
                                    "asset_quantities": [13337],
                                    "version": "0100",
                                    "type": "OA",
                                    "issued": [
                                                {
                                                  "color_address": "3JqEoSCcpaNW7Pm9cQVbQQgvz7nLnAmfTc",
                                                  "destination_address": "16NZhXGySMbCgpZ3WEMqkXGaxmmNnX51W5",
                                                  "previous_inputs": "source:1CBvyTJwqwv5Vb48QXNbFbczGX6b6s8UwC",
                                                  "quantity": 13337,
                                                  "btc": 600,
                                                  "txhash_index": "0f0169b34fe25f3ae76342c1f3b865f0d920b823daf891693830057aa90bef32:0"
                                                }
                                              ],
                                    "metadata_length": 27,
                                    "asset_count": 1,
                                    "metadata": "u=https://cpr.sm/eIOxaAZ-he"
                                    }
          },
          {
            "transaction_hash_with_index": "e82956b4e2649027ca797685fb4a8c3c0140a8cad9a3b7b35cdd01279017bda0:0",
            "parsed_colored_info": {
                                    "transferred": [
                                                    {
                                                      "destination_address": "1Myvq1HeQUY9kawMy2EzGMm9KU1nnF8hkB",
                                                      "previous_inputs": [
                                                                          "0f0169b34fe25f3ae76342c1f3b865f0d920b823daf891693830057aa90bef32:0",
                                                                          "e83fd8e7ce7e8a38dddbbf5010624b4ba1962cdbb7566aaf6ffa9c8d2f22bdbd:1"
                                                                          ],
                                                      "out_n": 1,
                                                      "quantity": 500,
                                                      "btc": 600,
                                                      "txhash_index": "e82956b4e2649027ca797685fb4a8c3c0140a8cad9a3b7b35cdd01279017bda0:1"
                                                      },
                                                    {
                                                      "destination_address": "16NZhXGySMbCgpZ3WEMqkXGaxmmNnX51W5",
                                                      "previous_inputs": [
                                                                          "0f0169b34fe25f3ae76342c1f3b865f0d920b823daf891693830057aa90bef32:0",
                                                                          "e83fd8e7ce7e8a38dddbbf5010624b4ba1962cdbb7566aaf6ffa9c8d2f22bdbd:1"
                                                                          ],
                                                      "out_n": 2,
                                                      "quantity": 12837,
                                                      "btc": 600,
                                                      "txhash_index": "e82956b4e2649027ca797685fb4a8c3c0140a8cad9a3b7b35cdd01279017bda0:2"
                                                      }
                                                    ],
                                    "asset_quantities": [500, 12837],
                                    "version": "0100",
                                    "type": "OA",
                                    "issued": [],
                                    "metadata_length": 0,
                                    "asset_count": 2,
                                    "metadata": ""
                                  }
                                }
                              ]
          }

  - #####Get Raw Transaction Information

    - /v1/transactions/raw/"TX HASH"


    curl https://coins.assembly/com/v1/transactions/raw/87e7d0c02b5c518e1b5d8668c6db423fbe0d5ad461e9e7f2086d52275d98d72d

    Response
    {
      "raw_transaction":
        {
          "vout": [
                    {
                      "value": 3.0,
                      "n": 0,
                      "scriptPubKey": {
                                        "hex": "76a9142f5befb369ed9cf1c04934387a7a55bffdf8ed8688ac",
                                        "type": "pubkeyhash",
                                        "asm": "OP_DUP OP_HASH160 2f5befb369ed9cf1c04934387a7a55bffdf8ed86 OP_EQUALVERIFY OP_CHECKSIG",
                                        "reqSigs": 1,
                                        "addresses": ["15KQts8aQ84uiskjEjHFe3ZPTRnXDDppAT"]
                                        }
                    },
                    {
                      "value": 7.69703,
                      "n": 1,
                      "scriptPubKey": {
                                        "hex": "76a914c985e97940bd881f6fcfcf4f0295476d66fb326488ac",
                                        "type": "pubkeyhash",
                                        "asm": "OP_DUP OP_HASH160 c985e97940bd881f6fcfcf4f0295476d66fb3264 OP_EQUALVERIFY OP_CHECKSIG",
                                        "reqSigs": 1,
                                        "addresses": ["1KNZEvnE6A6Y9ev1kpNfxbM5kj1YSe7roa"]
                                        }
                    }
                  ],
          "time": 1409789874,
          "locktime": 0,
          "version": 1,
          "vin": [
                  {
                    "scriptSig": {
                                  "hex": "493046022100a7beee5f45a6e6c4bd4f3b91c1c3f7e95f91ea1b99cfc3ecc78d2eafb0b926d1022100848f01e8159df6ed0cf264d2b9cdd3ab4c75fe85d25b48853530e2cd6a3e2aaf0141044ab0b335f0cd9278991663560c578f1fc586a6b0a985873669dd2986c266d7812410c713bf8f45b458b8a7ba176b265f055cc34d2814c57c54bc2184737765d1",
                                  "asm": "3046022100a7beee5f45a6e6c4bd4f3b91c1c3f7e95f91ea1b99cfc3ecc78d2eafb0b926d1022100848f01e8159df6ed0cf264d2b9cdd3ab4c75fe85d25b48853530e2cd6a3e2aaf01 044ab0b335f0cd9278991663560c578f1fc586a6b0a985873669dd2986c266d7812410c713bf8f45b458b8a7ba176b265f055cc34d2814c57c54bc2184737765d1"
                                  },
                    "vout": 1,
                    "txid": "7809e998ad62201031ce4af82a358d27d588de74dc6c4f647c617e419a8db2bc",
                    "sequence": 4294967295
                  }
                  ],
          "hex": "0100000001bcb28d9a417e617c644f6cdc74de88d5278d352af84ace31102062ad98e90978010000008c493046022100a7beee5f45a6e6c4bd4f3b91c1c3f7e95f91ea1b99cfc3ecc78d2eafb0b926d1022100848f01e8159df6ed0cf264d2b9cdd3ab4c75fe85d25b48853530e2cd6a3e2aaf0141044ab0b335f0cd9278991663560c578f1fc586a6b0a985873669dd2986c266d7812410c713bf8f45b458b8a7ba176b265f055cc34d2814c57c54bc2184737765d1ffffffff0200a3e111000000001976a9142f5befb369ed9cf1c04934387a7a55bffdf8ed8688ac58bce02d000000001976a914c985e97940bd881f6fcfcf4f0295476d66fb326488ac00000000", "blockhash": "00000000000000000e9481fa2399ddd32d8d29543e92fde915319a234a3758c4", "blocktime": 1409789874, "txid": "87e7d0c02b5c518e1b5d8668c6db423fbe0d5ad461e9e7f2086d52275d98d72d",
          "confirmations": 2
        }
    }

 - #####Search for Verified Colored Coin Data on Transaction
   /v1/transactions/"TRANSACTION_HASH"


    curl https://coins.assembly.com/v1/transactions/201057b5915e692cbdb435b9fc390553b029dfea607fd285e01e633e7015bc6a

    Response
    {
      "outputs": [
                  {
                    "color_address": "3Mtjm3kYAk4CcsrbL5rhVKXWgT4tbyQH7E",
                    "spent_at_txhash": "",
                    "blockmade": 300871,
                    "previous_input": "source:1R7L7HnTgU6Ei1h7AwYc93bCyJXevM637",
                    "destination_address": "1Q4sP6gak7PE7YQduYYTUdNuhPrDoqoQQQ",
                    "txhash": "201057b5915e692cbdb435b9fc390553b029dfea607fd285e01e633e7015bc6a",
                    "blockspent": null,
                    "spent": false,
                    "color_amount": 1,
                    "btc": 600,
                    "txhash_index": "201057b5915e692cbdb435b9fc390553b029dfea607fd285e01e633e7015bc6a:0"
                  }
                ]
    }


####Messages

  - #####Write Multipart Statement on the Blockchain
    POST '/v1/messages/'


    curl https://coins.assembly.com/v1/messages \
    -X POST \
    -H "Content-Type: application/json" \
      -d '{
            "public_address": "12GWLZTL6vNcKLzewbRpGWbRw7MWdmxdWG",
            "fee_each": 0.00005,
            "private_key": "5KDN3QoQMkQ8UWRCn732766z12NTNpdWEwjSna7yC6pLpmaUHTA",
            "message": "Before the creation of Ea, Sauron was one of the countless lesser Ainur spirits created by Eru Iluvatar, known as the Maia. At this time he was known as Mairon the Admirable, and partook in the Ainulindale, or Music of the Ainur. "
      }'

    Response
    {
      "transaction_hash":"f04281ee925d927dcef21e0236023cebad522a4f08545a85cb625338f1f77896"
    }


  - #####Read stitched-together multi-part OP_RETURN statements issued by an address
    - GET /v1/messages/"public_address"


    curl http://coins.assembly.com/v1/messages/1N8onLuitcQR9V3HB9QSARyFV6hwxA99Sx

    Response
    {
      "statements": "{\"name\": \"pillars\", \"desc\": \"one small step\", \"total\": 52352}"
    }
