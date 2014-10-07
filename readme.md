##How to Contribute

####Sign up for Assembly.com to Contribute and Earn Ownership

- https://assembly.com

- visit this project's page at
  https://assembly.com/assemblycoins

- or our front page at
  https://coins.assembly.com

- Check out this project's current App Coin distribution
  https://coins.assembly.com/addresses/16ucRhebuqcoDngLoZNwz2d6TjtNnLunKE

## Setup

  - ####Installing Libraries

    - $ pip install assemblycoins
    - $ pip setup.py install


  - ####Get Latest from Github

    - Run API Server + static site

      - $ git clone git@github.com:assemblymade/assemblycoins.git
      - $ cd assemblycoins
      - $ python main.py


  - ####Setup Database

    - set DATABASE_URL local variable to postgres database url
    - python setupdb.py


  - ####Running the static website

    - gem install jekyll
    - jekyll serve -w
    - open browser to http://localhost:4000


##Run Tests

    $ py.test -vv

##File Structure

/assemblycoins

  - /static
    - Compiled Site


  - addresses.py - Bitcoin Address Tools
  - bitsource.py - Colored Coin Manipulation Tools
  - databases.py - Interact with Postgres Database
  - leb128.py - LEB128 Encoding with Open Assets
  - main.py - API calls
  - node.py - Talking with local Bitcoind Node
  - otherworker.py - Worker Loop
  - test-api.py - Tests
  - transactions.py - Writing Bitcoin and Colored Coin Transactions
  - workertasks.py - Updating the Colored Coin Database, queuing transactions to write


/web
  - Jekyll Version of site

###Dependencies
 - Django==1.6.5
 - Flask==0.10.1
 - Flask-SQLAlchemy==1.0
 - Jinja2==2.7.3
 - MarkupSafe==0.23
 - SQLAlchemy==0.9.7
 - Werkzeug==0.9.6
 - bitcoin==1.1.10
 - ecdsa==0.11
 - gunicorn==19.1.0
 - itsdangerous==0.24
 - psycopg2==2.5.3
 - redis==2.10.3
 - requests==2.3.0
 - rq==0.4.6
 - virtualenv==1.11.6
 - wsgiref==0.1.2
 - pytest
 - memory_profiler
 - Flask-Scss

##Setting up your own Bitcoind Node
  - Install Bitcoin-Qt
  - Edit bitcoin.conf server file with
    - server=1 to activate server
    - set a username and password, rpcusername= something, rpcpassword= somethingelse
    - set the server url (probably set as localhost) to local variable "node_url"
    - set the node username as local variable "node_username"
    - set the node password as local variable "node_password"
    - write txindex=1
  - Test with
    - python
    - import node
    - node.connect("getblockcount", []) this should return the last block
    - or merely perform py.test in the shell since the node-connection is tested

##Library Tools with Examples

###ADDRESSES.PY
#####Get unspent outputs for address
 - addresses.get_unspent(public_address)
    - Returns an array of unspent outputs for an address.

###BITSOURCE.PY
#####Translate a transaction input script to a color address according to the Open Assets protocol
 - bitsource.script_to_coloraddress(script)
   - Returns the color address

#####Read a Bitcoin Transaction for OPRETURN DATA
  - bitsource.read_tx(txhash)
    - Returns the OPRETURN message, Value in Satoshi of transaction outputs

#####Parse metadata from an OPRETURN for Open Assets Content
  - bitsource.parse_colored_tx(metadata, txhash_with_index)
    - returns a dictionary detailing the colored coin meaning of this transaction, issuance of coins, transfers, amounts, etc.


###TRANSACTIONS.PY
#####Write Raw Transaction, Primitive Steps
 - transactions.make_raw_transaction(fromaddress,amount,destination, fee)   ONE OUTPUT
    - returns an unsigned bitcoin transaction taking ALL unspent outputs for fromaddress.  It sends the BTC amount to the destination, and returns the leftover minus fees to "fromaddress"

  - transactions.sign_tx(unsigned_raw_tx, privatekey)
    - Returns a signed bitcoin transaction.  All inputs are signed with the given private key.

 - transactions.pushtx(rawtx)
    - Pushes a signed Bitcoin transaction to your connected Bitcoin Node

 - transactions.pushtx_toshi(rawtx)
    - Pushes a signed Bitcoin transaction to Coinbase's Toshi Node API

#####Send OPRETURN transaction

 - transactions.send_op_return(fromaddress, destination, fee, message, privatekey, specific_inputs)
   - Writes and sends a Bitcoin transaction to destination with an OPRETURN including message.  Specific_inputs refers to an array of inputs to use as gathered from addresses.get_unspent(publicaddress)

##API Calls

- See https://coins.assembly.com/docs

##Whitepaper

- See https://coins.assembly.com/whitepaper
