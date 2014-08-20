from hello import db

class Meta(db.Model):
  id=db.Column(db.Integer, primary_key=True)
  lastblockprocessed = db.Column(db.Integer)
  numberoftransactions= db.Column(db.Integer)

  def __init__(self):
    self.id=0
    self.lastblockprocessed=0
    self.numberoftransactions=0
