from app import db, app
from models import Category, Product, User


# User
def addUser(name, email, username, password, active=False, avatar=None, user_role=0):
    user = User(name=name,
    email=email,
    username=username, 
    password=password, 
    active = True if active else False, 
    avatar = avatar, 
    user_role=user_role)

    db.session.add(user)
    db.session.commit()
def getUser():
    return User.query.all()  


# Category
def addCategory(name):
    cate = Category(name=name)

    db.session.add(cate)
    db.session.commit()
def getCategory():
    return Category.query.all()

# Product
def addProduct(name, description='', price=0, image=None, category_id=None, owner_id=None):
    product = Product(name=name, 
    description=description,
    price=price,image=image,
    category_id=category_id,
    owner_id=owner_id)

    db.session.add(product)
    db.session.commit()
def getProduct():
    return Product.query.all()

# with app.app_context():
#     addCategory('Phone')
#     addCategory('Car')
#     addCategory('Computer')