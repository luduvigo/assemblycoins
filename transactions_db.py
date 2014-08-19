#from sqlalchemy.dialects.postgresql import JSON
from hello import db

class Transaction(db.Model):
  hashid= db.Column(db.String(120), primary_key=True)
  source_address=db.Column(db.String(80), primary_key=True)
  destination_address=db.Column(db.String(80), primary_key=True)

  # public_address=db.Column(db.String(80), unique=True)
  # private_key=db.Column(db.String(80), unique=True)
  # amount_expected=db.Column(db.Integer())
  # amount_received=db.Column(db.Integer())
  # amount_withdrawn=db.Column(db.Integer())  #Amount we actually remove
  # coin_name=db.Column(db.String(80), unique=True)
  color_amount=db.Column(Integer())
  color_address=db.Column(db.String(80))
  # issued_amount=db.Column(db.Integer())
  # destination_address=db.Column(db.String(80))
  # description=db.Column(db.String(400))

  def __init__(self, hashid, source, destination, coloramt, coloraddress):
    self.hashid=hashid
    self.source_address=source
    self.destination_address=destination
    self.color_amount=coloramt
    self.color_address=coloraddress

#db.create_all()
