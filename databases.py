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


def add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade):
  dbstring="INSERT INTO addresses (btc, color_amount, color_address, spent, spent_at_txhash, destination_address, txhash, txhash_index, blockmade)"
  dbstring=dbstring + " VALUES ('"+
  dbstring=dbstring + btc+"','"+coloramt+"','"+coloraddress+"','"+spent+","+spentat+"','"+destination+"','"+txhash
  dbstring=dbstring+"','"+ txhash_index+"','"+blockmade+"');"

  print dbstring
  result dbexecute(dbstring)


#def edit_output():


#def add_address()

#def edit_address():

#def add_color():

#def edit_color():
