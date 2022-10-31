from app import db, app
from datetime import datetime
from sqlalchemy import Column, String, Text, Boolean, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key = True, autoincrement = True)

class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String(100), nullable = False)
    email = Column(String(50), nullable = False)
    username = Column(String(20), nullable = False)
    password = Column(String(10), nullable = False)
    active = Column(Boolean, default = False)
    avatar = Column(String(1000))
    joined_data = Column(DateTime, default = datetime.now())
    user_role = Column(Integer, default = 0) # 0 = USER, 1 = ADMIN 

    # RELATIONSHIP
    products = relationship('Product', backref='users', lazy=True)
    receipts = relationship('Receipt', backref='users', lazy=True)

class Category(BaseModel):
    __tablename__ = 'categories'

    name = Column(String(100), nullable = False)
    # RELATIONSHIP
    products = relationship('Product', backref='categories', lazy=True)

    def __str__(self):
        return self.name

class Product(BaseModel):
    __tablename__ = 'products'

    name = Column(String(100), nullable = False) 
    description = Column(String(300))
    price = Column(Float, default = 0)
    image = Column(String(1000))

    # FOREIGN KEYS
    category_id = Column(Integer, ForeignKey(Category.id), nullable = False)
    owner_id = Column(Integer, ForeignKey(User.id), nullable = False)

    # RELATIONSHIP
    receipt_details = relationship('ReceiptDetail', backref='products', lazy=True)

    def __str__(self):
        return self.name

class Receipt(BaseModel):
    __tablename__ = 'receipts'
    
    created_date = Column(DateTime, default = datetime.now())
    paid_date = Column(DateTime, default = datetime.now())

    # FOREIGN KEYS
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)

    # RELATIONSHIP
    receipt_details = relationship('ReceiptDetail', backref='receipts', lazy=True)

class ReceiptDetail(BaseModel):
    __tablename__ = 'receipt_detail'

    unit_price = Column(Float, default = 0)
    quantity = Column(Integer, default = 1)

    # FOREIGN KEYS
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)


with app.app_context():
    db.create_all()
