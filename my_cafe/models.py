from my_cafe import db
from datetime import datetime

class Profile(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String, nullable=False)
   email = db.Column(db.String, nullable=False, unique=True)
   password = db.Column(db.String, nullable=False)
   customer = db.Column(db.Boolean, nullable=False, default=True)


class Purchase(db.Model):
   id = db.Column("transaction_id", db.Integer, primary_key = True)
   purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
   expiry_date = db.Column(db.DateTime, nullable=False)
   price = db.Column(db.Float, nullable=False)
   seller = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
   product = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)


class Product(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String, nullable=False)
   category = db.Column(db.String, nullable=False)
   availability_count = db.Column(db.Float, nullable=False)
   unit = db.Column(db.String, nullable=False)
   purchase = db.relationship('Purchase', backref='product', lazy=True)


class Supplier(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   first_name = db.Column(db.String, nullable=False)
   middle_name = db.Column(db.String, nullable=True)
   last_name = db.Column(db.String, nullable=True)
   supply_type = db.Column(db.String, nullable=False)
   contact = db.Column(db.Integer, nullable=False)
   email = db.Column(db.String, nullable=True)
   transaction = db.relationship('Purchase', backref='seller', lazy=True)