from my_cafe import db
from datetime import datetime

class Profile(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String, nullable=False)
   email = db.Column(db.String, nullable=False, unique=True)
   password = db.Column(db.String, nullable=False)

   def __init__(self, name, email, password):
      self.name = name
      self.email = email
      self.password = password


class RawPurchase(db.Model):
   id = db.Column('product_id', db.Integer, primary_key = True)
   name = db.Column(db.String)
   purchase_date = db.Column(db.DateTime, default=datetime.now)
   expiry_date = db.Column(db.DateTime)
   price = db.Column(db.Float)

   def __init__(self, name, purchase_date, expiry_date,price):
      self.name = name
      self.purchase_date = purchase_date
      self.expiry_date = expiry_date
      self.price = price