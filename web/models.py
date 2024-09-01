from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))

    cart_items = db.relationship('Cart', backref=db.backref('user', lazy=True))

    orders = db.relationship('Order', backref=db.backref('user', lazy=True))

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    user_link = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    product_link = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False)

    def __str__ (self):
        return '<Cart %r>' % self.id
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    user_link = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    product_link = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False)

    def __str__ (self):
        return '<Order %r>' % self.id
    

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    photo = db.Column(db.String(200), nullable=False)

    carts = db.relationship('Cart', backref=db.backref('product', lazy=True))

    orders = db.relationship('Order', backref=db.backref('product', lazy=True))

    def __str__ (self):
        return '<Product %r>' % self.product_name