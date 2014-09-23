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

    - 


##Run Tests

    $ py.test

##File Structure

/assemblycoins

  - /static
    - Compiled Jekyll Site


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


##API Calls

- See https://coins.assembly.com/docs.html
