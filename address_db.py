from sqlalchemy.dialects.postgresql import JSON
from hello import db

class Address(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  public_address=db.Column(db.String(80), unique=True)
  private_key=db.Column(db.String(80), unique=True)
  amount_expected=db.Column(db.Integer())
  amount_received=db.Column(db.Integer())
  amount_withdrawn=db.Column(db.Integer())  #Amount we actually remove
  coin_name=db.Column(db.String(80), unique=True)
  color_address=db.Column(db.String(80), unique=True)
  issued_amount=db.Column(db.Integer())
  destination_address=db.Column(db.String(80))
  description=db.Column(db.String(400))

  def __init__(self, publicaddress, privatekey, amount_expected, amount_received, amount_withdrawn, coin_name, color_address, issued_amount, destination, description):
    self.public_address=publicaddress
    self.private_key=privatekey
    self.amount_expected=int(amount_expected)
    self.amount_received=int(amount_received)
    self.amount_withdrawn=int(amount_withdrawn)
    self.coin_name=coin_name
    self.color_address=color_address
    self.issued_amount=issued_amount
    self.destination_address=destination
    self.description=description



#db.create_all()
