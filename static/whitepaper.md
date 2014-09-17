#Assembly Assets
by Andrew Barisser at Assembly
July 29, 2014


##Introduction

####	Assembly
At Assembly, we provide an environment for individuals to collaborate on products from around the world.  As
 members make contributions to specific tasks, called bounties, they earn ownership in the
  corresponding product.  This ownership is represented by Assembly Assets.  If and when the product
  later makes money, its profits are distributed as royalties to coinholders proportionately.  Payments
  are issued monthly as long as the product remains profitable.

Assembly contributors are already receiving regular, monthly cash payments from profitable products.  As
 members get paid, we are working to expand their capabilities as owners.  While we currently store all product information
 on our servers, we are excited about the potential of blockchain-based technologies in revolutionizing digital ownership.
 As a platform where members create companies, Assembly is well-placed to reinvent the way businesses are built.  This
 means innovating in finance as well as software.  We see decentralizing the instruments of ownership as the next big step forward.

####	What we are doing with Bitcoin

Assembly is putting members' ownership in individual products on the Bitcoin Blockchain.  A 'metacoin' existing as a layer
on top of Bitcoin, Assembly Assets are digital ownership tokens with all the advantages of Bitcoin and none of the currency risk.  We aim
to give users the best tools, extending to cryptographic guarantees of control, such that ownership is no longer a
matter of trust, but mathematically self-evident.  Satoshi's
    central innovation of proof-of-work and decentralization has a lot more potential than has
    so far been implemented.  We are building Bitcoin 2.0 tools that utilize new aspects of the Blockchain
     beyond currency.  As a site where members contribute digitally and own assets digitally, Assembly is an ideal platform to
     capitalize on the latest developments in cryptocurrency.

#### This is not another Altcoin

Assembly is not making another Altcoin.  Colored coins are a metacoin on top of the Bitcoin blockchain,
 not a separate blockchain.  This means the data recording asset ownership is much more secure and enduring
 than a newly invented, seldom used, parallel blockchain.  The Bitcoin network itself is the most
 mature option with the most stakeholders, stability, and existing architecture.  Your ownership
 isn't getting written in a meme-coin.

We are not selling anything.  Colored coins is an open protocol which we are using to enhance
the Assembly platform's value for our users.  There is no premining, no presale.  There is no internal
 currency with a separate Bitcoin exchange rate.  There is no intermediary between you and Assembly Assets.  Because
 our sole incentive is the maximize the experience of our users, we approached the
   design of ownership crypto-representation so as to produce the most sensible tool and not necessarily the
    most profitable one.  This stands in stark contrast to many other 'Bitcoin 2.0' technologies out there,
     designed from the bottom up to raise money before real work gets done.  Our products already make money,
      so Assembly Assets themselves will immediately have value based on real-world revenue streams.

Our Assembly Assets tools will be completely open-source and there are no barriers to entry.  If you like it,
fork it and make it better.  We're making this service because we want to consume it.


##Colored Coins

The idea behind colored coins, which has been around for some time in the Bitcoin community, is
that assets besides bitcoins can be represented as abstractions on the Bitcoin Blockchain.  Whereas
bitcoins natively are indistinguishable from one another, colored coins are distinguishable abstractions
 represented on the Bitcoin Blockchain, consisting of more than just Satoshi.  Colored coins have been
 specially labelled in such a way that they retain that label through all subsequent transactions.  They
  come in quantities which may not coincide with their value in Satoshi.  And they come labelled with
  their ‘issuing address’, which states the ‘identity’ or ‘type’ of each colored coin.

Colored coins are a powerful concept for several reasons.  Because they exist on the Bitcoin Blockchain,
 they enjoy all the benefits therein.

- Since colored coins can represent a wide variety of items, new services can be designed around the transparency of their ownership.

- Colored coins can be easily transferred from one address to another, quickly and at low cost.  Ownership has never has never been so easy to move around.

- Colored coins provide proof-of-ownership of whatever they represent.  This opens doors for other uses not appropriate to Bitcoin, such as voting.

- Colored coins are trustless once minted.  While the issuer of a particular colored coin must be trusted, the transmission and ownership of Colored Coins are not susceptible to any third parties.

- Colored coins will be secure; it will be cryptographically impossible to forge a transaction from the private key holder.

####	Assembly Assets vs Colored Coins

While colored coins are a general concept with an existing protocol and several groups working on their
features, Assembly Assets is a specific implementation of the colored coin concept.  In that sense
it inherits from colored coins, which are of wide-ranging purpose, and applies them to a particular use
 case.  Assembly Assets represent ownership in Assembly products and a portion of their profits.

Because Assembly Assets inherits from colored coins, our API will be designed for the most general use of
 colored coins.  A user should be able to manipulate all Open Assets-compliant colored coins with Assembly tools.  Conversely, it should not be obligatory to use Assembly's API to manage Assembly Assets.  We hold no unique information; it's all on the Blockchain.

####	Example Assembly Assets Lifecycle

- Bart creates a new Product called "Doogle".  With the Assembly API, which automates this task, Bart issues
 an encrypted statement declaring the issuance of Assembly Assets which represent ownership in "Doogle". The
 initial issuing declaration states:
	- The name of the product
	- The metadata that will identify "Doogle" Assembly Assets in future Bitcoin transactions.


- A special Assembly Assets issuing address is generated via the Assembly API.  In the future it may be a
multisig address in which the controlling keys are distributed to product stakeholders.
As the issuer, this address controls the supply of this particular variety of colored coins.
  - The issuing address's private keys are used to encrypt Bart's issuance declaration, proving
   the founders' control over that address.  His declaration includes metadata corresponding to the product.


- As the first founder, Bart receives an initial 6000 Assembly Assets of
"Doogle", as is done presently.  These are sent to his personal address, not the issuing address, as
 a specially marked Bitcoin transaction.  His ownership of "Doogle" Assembly Assets is now an uncontested
 fact for all to see.  The issuance of Assembly Assets, as well as checking an address's assets, are available
 as Assembly API calls in addition to being open source.

- Mildred comes along and helps build Doogle.  Bart and other Core Team members award her a bounty
 on Assembly for that task, simultaneously signing a multisig transaction issuing Mildred new Doogle
  Assembly Assets.  Within a few minutes, Mildred has cryptographic control over her Assembly Assets.

- Soon Doogle is a smashing commercial success, receiving dollar-denominated profits through Assembly.  Since
 Doogle's ownership is plainly visible on the Blockchain, Assembly distributes royalties
to all the Assembly Assets owners.  Those desiring distributions in dollars receive them through regular
channels.  Others receive bitcoins directly to their coinholding public addresses.  There is a direct
 and immediate link between ownership of Assembly Assets on the blockchain and payment by Assembly.

- Mildred sends her Assembly Assets to another Bitcoin address that she controls.  That's fine.
  Bitcoins are awarded to whichever address holds the relevant Assembly Assets.

Perhaps down the road Bart and Mildred will have the following capabilities:

- Managing the Doogle product involves lots of small but important business decisions.  Cryptographic voting
from the private keys of coinholders, wherever they might be, is a trustless and provable way to
demonstrate consensus.

- Doogle is really taking off, but in order to hire the services of advertisers, marketers, and other
3rd party contractors, a collective pot of money is required.  To manage money in a trustless way,
Mildred, Bart, and other coinholders in Doogle create a multisignature Bitcoin address.  To spend this money, some fraction of the keyholders must sign off on each outgoing transaction.  This voting fraction does not have to be a majority,it could be 2 out of 1000, or 4 out of 5, whatever they agree to.
Now the product can control money safely.

- Doogle may raise funds, to be owned cryptographically by the product and not any individual member, by issuing new Assembly Assets.  Issuance would require consent via cryptographic voting of existing owners.

- The entire financial history related to the product, from assets, to royalty payments, and to revenue generated via Bitcoin, can be provably audited within seconds.


## The Legal Status of Assembly Assets
Assembly is a partnership in which members have contributed work and
thereby receive ownership.  That ownership is represented by Assembly Assets.  Profit distributions are royalties from
individual products.  Coinholders may transfer their assets
between addresses they control, or between existing stakeholders.  Tax
information should be registered, for withholding purposes, for each member.  Each Assembly Assets revenue stream can thus be associated with a member's tax information for IRS compliance.
Payments in Bitcoin will be reported as with dollars.  Because Assembly Assets represent partnership stakes, AssemblyCoin holders must
exercise partners' responsibilities, such as participiating in products at least once a year.


##The Assembly Assets API

### Description

The Assembly Assets API will exist as an independent service that provides general tools for navigating the world of colored coins.
It is designed to appeal to the broadest set of developers interested in leveraging the Open Assets protocol.  As such, many of the queries
developers use on the Bitcoin Blockchain have colored analogs here.  It has tools for interacting with
 addresses, blocks, transactions, colored coin metadata, encrypted messaging, and multisignature features.
  Most of these API calls are not currently available in an easy-to-use API online.

Assembly will be a consumer of the colored coins API as it implements Assembly Assets.  But the same Assembly Assets
 could be manipulated with a separate service, a forked version, or via handcrafted Bitcoin transactions.  It
 should never be obligatory to use the Assembly API to handle Assembly Assets.

##Behavior of the Protocol

Assembly Assets adopts the Open Assets protocol
(https://github.com/OpenAssets/open-assets-protocol/blob/master/specification.mediawiki).
 This is a convenient and open-ended way to label assets as a layer on top of Bitcoin.

Colored Coins are originally born with a user creating a Bitcoin public address, the issuing address.  When a user writes a Bitcoin
transaction with the correct metadata from that issuing address, a hash can be generated from the Bitcoin script
in the first input of that transaction.  This hash is a unique identifier for the coin color.  Coin colors may
have human-readable names such as 'RedCoins', but they always also have a unique hash which we call the 'Asset Hash'. To
prevent confusion, our API responds to a colored coin's Asset Hash.  Other metadata about the coin color may then be queried.

Please see the original protocol for more useful information.

There are certain important advantages to this protocol.
- All necessary information is inscribed in the Bitcoin Blockchain.
- It harnesses all the advantages of the Bitcoin Blockchain, security, protection from double-spending, ease of use, transparency, pseudonymity.
- Tools that already exist for Bitcoin can be easily applied to Colored Coins.
- Color coin assets are not tied to actual Bitcoin amounts, meaning asset transfers and creation are very cheap.
- There is basically no limit to the number of coin colors that can be issued.
- It is possible to move multiple kinds of Colored Coins to with multiple inputs and outputs in one transaction.
- There is no metacoin between Colored Coins and Bitcoin.  That means no pre-mining, presale, or other cheap gimmicks.
- This is not another Altcoin!  It exists on the Bitcoin Blockchain, which means it's going to endure.

Other services may not be directly available with Open Assets, but could be developed on top of it.
- Decentralized Exchanges are being built (Iridis).

##Our Vision of the Future
Assembly already innovates in the way products are built.  By connecting
makers
from all over the world, and incentivizing them with ownership stakes in future profits, new types of
businesses can be built on our platform.  But we want to go further.  Assembly intends to challenge the status quo in finance by distributing ownership via liberating technologies such as cryptocurrency.  We want to remove barriers to economic participation in profit-seeking enterprises.

Assembly wants to be the financial clearinghouse that simplifies life for disparate, product-oriented developers.  This means getting out of your way and putting the best tools in your hands.  The hassles of incorporating a startup and keeping track of paperwork should be minimized as much as possible.  We handle a lot of the obstacles to executing a cool new idea.

While trust is critical in doing business, in practice, it is currently a very expensive thing to acquire.  Assembly wants to square the circle and deliver you that trust via ironclad cryptographic tools, which, we believe, are the way business will be done in the future.  Assurances that would require complicated legal frameworks will be obviated by elegantly complete mathematics.

Our vision of the future is one in which companies are transparently managed, fluidly created, disbursements are easy, paperwork is automated.  Let lawyers and accountants be redundant!  The friction that ordinarily interferes with the fruition of a great idea should be reduced as much as possible.  Your ownership will be cryptographic, which means undisputed by the awesome power of math. Decisions too, and money handling, the day-to-day of business, while easy to use on the front end, are underlied by strong cryptographic guarantees.  If anyone wants to peak under the hood, audit a company, poll the stakeholders, go over the entire financial history, it should be as trivial as clicking a button.

###Glossary
```
Open Assets - The Colored Coin protocol Assembly Assets uses
Issuing Address - The address controlling the issuance of a Colored Coin.  Bitcoins sent from this address with the correct metadata become colored
Asset Hash -  A unique identifier for each coin color.  More technically, this is the RIPEMD-160 hash of the SHA-256 hash of the output script of the first input of the first transaction issuing the colored coin
Assembly Assets - Ownership in an Assembly Product as represented on the Blockchain
Metadata -  additional information labelling bitcoins into colored coins.
```


##API

  ## Setup

      $ virtualenv venv
      $ source venv/bin/activate
      $ pip install -r requirements.txt --allow-all-external
      $ cp .env.sample .env
      $ # edit .env
      $ forego start

  ##Test

      $ py.test

      Give it a minute

  ##API Calls

  ####API ROOT
  - assets.assembly.com

  ####Colors

  - #####Prompt API Server for New Coin Issuing Address
    - POST /v1/colors/prepare


      curl https://assets.assembly.com/v1/colors/prepare \
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


      curl https://assets.assembly.com/v1/colors/32dCTMMrW7XPVrfbfJtguo6LN9sg8mvttq

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
  <!--
  - #####See metadata for all known Colors

    - GET /v1/colors/


      curl https://assets-api.assembly.com/v1/colors

      Response
      {"colors": [{"source_address": "1ARyJPCkaa4cQHxjeZYApRL2CuGWhyrLX5", "total_issued": 10000000, "color_address": "3JxzvzjFgbJzxv2rEJnfVpriuX6DQhTnTq"}, {"source_address": "1AkgfUwJ3K2ZSzmToVwiZL2KxTUGCMypz3", "total_issued": 352, "color_address": "3F12nNGHAW3a5s4ET3ZfyR3A8kzpvFDbtc"}, {"source_address": "1mpC4oLBmvMNcdK4jmSAAxMA62mSsfMvv", "total_issued": 5102, "color_address": "38PfLkHYC2gb98ZXdVtvDJQ1dk6Eh75Zcf"}}
   -->

  - #####Make New Coin Directly with Server Side Transaction Signing

    - POST /v1/colors/


      curl https://assets-api.assembly.com \
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


      curl https://assets.assembly.com/v1/addresses/1CEyiC8DXT6TS3d9iSDnXRBtwyPuVGRa9P

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


      curl https://assets.assembly.com/v1/addresses

      Response
      {
        "public_address": "15EZotfUZjsT6RiYryTjwJ64WwW2MbRXRe",
        "private_key": "5JMFFPgzjgKHkKnGvTRB1aaiBhRu9Tq6ZC28Gj5v9DK5PBzSwTD"
      }

  - #####Generate Public/Private Address Pair from Phrase
  USE WITH CAUTION, only use very complex phrases!
    - /v1/addresses/brainwallet/"your_phrase"


      curl https://assets.assembly.com/v1/addresses/brainwallet/password1

      Response
      {
        "public_address": "19VAb9zAhpWLaWfEuqw9HXup2zaNoNPPyE",
        "private_key": "5HuAe6SqbZHxWJNHZ9YMxW7dFp97PdzMD2uTHChLd1nXJPS5dsR"
      }

  ####Transactions


  - #####Transfer Colored Coins with Server Side signing
    - POST /v1/transactions/transfer


      curl https://assets.assembly.com/v1/transactions/transfer \
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

  <!-- - #####Transfer Colored Coins with Client Side signing -->
  <!--
  - #####Issue Additional Coins with Server Side signing
    - POST /v1/transactions/issue


      curl https://assets.assembly.com/v1/transactions/issue \
        -X POST \
        -H "Content-Type: application/json" \
        -d '{
              "public_address": "",
              "private_key": "",
              "additional_coins": "",
              "recipient": "",
              "name": ""
          }'

      Response -->

  <!-- - #####Issue Additional Coins with Client Side signing -->

  - #####Push Raw Transaction to Bitcoin Network
    - POST /v1/transactions


      curl https://assets.assembly.com/v1/transactions \
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


      curl https://assets.assembly.com/v1/transactions/parsed/300712

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


      curl https://assets.assembly/com/v1/transactions/raw/87e7d0c02b5c518e1b5d8668c6db423fbe0d5ad461e9e7f2086d52275d98d72d

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


      curl https://assets.assembly.com/v1/transactions/201057b5915e692cbdb435b9fc390553b029dfea607fd285e01e633e7015bc6a

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


      curl https://assets.assembly.com/v1/messages \
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


      curl http://assets.assembly.com/v1/messages/1N8onLuitcQR9V3HB9QSARyFV6hwxA99Sx

      Response
      {
        "statements": "{\"name\": \"pillars\", \"desc\": \"one small step\", \"total\": 52352}"
      }



###To Be Implemented

######Multisig Issuing Colored Coin Transactions

######Multisig Transfer Colored Coin Transactions

######Client Side signing for transactions




######On Privacy and OPENSSL

Several of the API calls listed entail sending encrypted private keys to the Assembly service. While we understand that some may be uncomfortable with a 3rd party having access to their private keys, Assembly will never retain them. Since these tools are themselves open-source, they also may be forked and run independently at any time.

Our goal is to develop client-side tools to assist with processing requiring private keys.



##FAQ

  - Can I manipulate Colored Coins client-side?
      - Yes.  All of the information is secure on the Blockchain.  Since Assembly Assets is an open source service, you can
      run it yourself.


  - Is this legal?
    - Yes.  Assembly Products are partnerships in which owners earn profit shares.  Assembly Assets represent the ownership
      partners have always had.


  - How does this scale?
      - Colored coin transactions can be backscanned to the issuing address to verify their legitimacy.


  - Do I need to burn Bitcoin?
      - No.  Don't burn Bitcoin!  Dust amounts of Bitcoin are needed for transactions, that's all.  They're not lost either.
