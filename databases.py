import transactions_db
import address_db
import meta_db
import os
#db.create_all()

import psycopg2
import sys
import urlparse

con=None

urlparse.uses_netloc.append('postgres')
url = urlparse.urlparse(os.environ['DATABASE_URL'])

def dbexecute(sqlcommand):
  databasename=os.environ['DATABASE_URL']
  #username=''
  con=psycopg2.connect(
    database= url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
  )

  cur=con.cursor()
  cur.execute(sqlcommand)
  return cur.fetchall()
