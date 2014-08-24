import transactions_db
import address_db
import meta_db
#db.create_all()

import psycopg2
import sys

con=None

def dbexecute(sqlcommand):
  databasename=os.environ['DATABASE_URL']
  #username=''
  con=psycopg2.connect(database=databasename)
  cur=con.cursor()
  cur.execute(sqlcommand)
