#import transactions_db
#import address_db
#import meta_db
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


def add_output(btc, coloramt, coloraddress, spent, spentat, destination, txhash, txhash_index, blockmade, prev_input):
  dbstring="INSERT INTO outputs (btc, color_amount, color_address, spent, spent_at_txhash, destination_address, txhash, txhash_index, blockmade, previous_input)"
  dbstring=dbstring + " VALUES ('"
  dbstring=dbstring + btc+"','"+coloramt+"','"+coloraddress+"','"+spent+"','"+spentat+"','"+destination+"','"+txhash
  dbstring=dbstring+"','"+ txhash_index+"','"+blockmade+"','"+prev_input+"');"

  print dbstring
  result=dbexecute(dbstring, False)
  return result

def edit_output(txhash_index, btc, coloramt, coloraddress, spent, spentat, destination, blockmade):
  dbstring="UPDATE outputs SET btc="+'btc'+", color_amount='"+coloramt+"',color_address='"+coloraddress+"',"
  dbstring=dbstring+"spent='"+spent+"',spent_at_txhash='"+spentat+"',destination_address='"+destination
  dbstring=dbstring+"',blockmade='"+blockmade+"' WHERE txhash_index='"+txhash_index+"';"

  #print dbstring
  result=dbexecute(dbstring, False)
  return result

def spend_output(txhash_index, spent_at):
  dbstring="UPDATE outputs SET spent='True', spent_at_txhash='"+ str(spent_at)+"' WHERE txhash_index='"+ txhash_index+"';"
  print dbstring
  result=dbexecute(dbstring,False)
  return result

def read_output(txhash_index, require_unspent):
  if require_unspent:
    dbstring="SELECT * FROM outputs WHERE txhash_index='"+txhash_index+"' and spent='False'"
  else:
    dbstring="SELECT * FROM outputs WHERE txhash_index='"+txhash_index+"';"
  #print dbstring
  result=dbexecute(dbstring,True)
  return result

def add_address(public_address, private_key, amount_expected, amount_received, amount_withdrawn, coin_name, issued_amount, destination_address, description, ticker):
  dbstring="INSERT INTO addresses (public_address, private_key, amount_expected, amount_received, amount_withdrawn, coin_name, issued_amount, destination_address, description, ticker)"
  dbstring=dbstring+" VALUES ('"+public_address+"','"+private_key+"','"+amount_expected+"','"+amount_received+"','"+amount_withdrawn+"','"+coin_name+"','"+issued_amount+"','"+destination_address+"','"+description+"','"+ticker +"');"
  #print dbstring
  result=dbexecute(dbstring,False)
  return result

def edit_address(public_address, amount_received, amount_withdrawn, issued_amount):
  dbstring="UPDATE addresses SET amount_received='"+amount_received+"',amount_withdrawn='"+amount_withdrawn+"',issued_amount='"+issued_amount+"' WHERE public_address='"+ public_address+"';"
  #print dbstring
  result=dbexecute(dbstring,False)
  return result

def read_address(public_address):
  dbstring="SELECT * FROM addresses WHERE public_address='"+public_address+"';"
  #print dbstring
  result=dbexecute(dbstring,True)
  return result

def add_color(color_address, source_address, total_issued, color_name):
  dbstring="INSERT INTO colors (color_address, source_address, total_issued, color_name)"
  dbstring=dbstring+" VALUES ('"+color_address+"','"+source_address+"','"+total_issued+"','"+color_name+"');"
  #print dbstring
  result=dbexecute(dbstring,False)
  return result

def edit_color(color_address, total_issued):
  dbstring="UPDATE colors SET total_issued='"+str(total_issued) +"' WHERE color_address='"+color_address+"';"
  #print dbstring
  result=dbexecute(dbstring,False)
  return result

def read_color(color_address):
  dbstring="SELECT * FROM colors WHERE color_address='"+color_address+"';"
  #print dbstring
  result=dbexecute(dbstring,True)
  return result

def color_balance(public_address, color_address):
  if color_address==None or color_address=="":
    dbstring="SELECT * FROM OUTPUTS WHERE destination_address='"+public_address+"';"
  else:
    dbstring="SELECT * FROM OUTPUTS WHERE destination_address='"+public_address+"' and color_address='"+color_address+"';"
  result=dbexecute(dbstring,True)
  coloramt=0
  answer={}
  for x in result:
    coloraddress=x[2]
    coloramt=x[1]
    if coloraddress in answer:
      answer[coloraddress]=int(answer[coloraddress]+coloramt)
    else:
      answer[coloraddress]=int(coloramt)
  return answer

def color_holders(color_address):
  dbstring="SELECT * FROM OUTPUTS WHERE color_address='"+color_address+"' and spent='False';"
  result=dbexecute(dbstring,True)
  answer=[]
  for x in result:
    a={}
    a['address']=x[5]
    a['color_amount']=int(x[1])
    answer.append(a)
  return answer
