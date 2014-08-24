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

def dbexecute(sqlcommand, receiveback):
  databasename=os.environ['DATABASE_URL']
  #username=''
  con=psycopg2.connect(
    database= url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
  )
  result=''
  cur=con.cursor()
  cur.execute(sqlcommand)
  if receiveback:
    result=cur.fetchall()
  con.commit()
  cur.close()
  con.close()
  return result


def add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade):
  dbstring="INSERT INTO outputs (btc, color_amount, color_address, spent, spent_at_txhash, destination_address, txhash, txhash_index, blockmade)"
  dbstring=dbstring + " VALUES ('"
  dbstring=dbstring + btc+"','"+coloramt+"','"+coloraddress+"','"+spent+"','"+spentat+"','"+destination+"','"+txhash
  dbstring=dbstring+"','"+ txhash_index+"','"+blockmade+"');"

  print dbstring
  result=dbexecute(dbstring, False)
  return result

def edit_output(txhash_index, btc, coloramt, coloraddress, spent, spentat, destination, blockmade):
  dbstring="UPDATE outputs SET btc="+'btc'+", color_amount='"+coloramt+"',color_address='"+coloraddress+"',"
  dbstring=dbstring+"spent='"+spent+"',spent_at_txhash='"+spentat+"',destination_address='"+destination
  dbstring=dbstring+"',blockmade='"+blockmade+"' WHERE txhash_index='"+txhash_index+"';"

  print dbstring
  result=dbexecute(dbstring, False)
  return result

def read_output(txhash_index):
  dbstring="'SELECT * FROM outputs WHERE txhash_index='"+txhash_index+"';"
  result=dbexecute(dbstring,True)
  return result


def add_address()

#def edit_address():

#def add_color():

#def edit_color():
