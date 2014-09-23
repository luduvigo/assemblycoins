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



##Library Tools with Examples

####Write Raw Transaction
 - transactions.make_raw_transaction(fromaddress,amount,destination, fee)
    - returns an unsigned bitcoin transaction taking ALL unspent outputs for fromaddress.  It sends the BTC amount to the destination, and returns the leftover minus fees to "fromaddress"

 - transactions.sign_tx(unsigned_raw_tx, privatekey)
    - Returns a signed bitcoin transaction.  All inputs are signed with the given private key.

 - transactions.pushtx(rawtx)
    - Pushes a signed Bitcoin transaction to your connected Bitcoin Node

 - transactions.pushtx_toshi(rawtx)
    - Pushes a signed Bitcoin transaction to Coinbase's Toshi Node API

##API Calls

- See https://coins.assembly.com/docs.html
