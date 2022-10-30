from app import db, app
from models import Category

def addCategory(name):
    cate = Category(name=name)

    db.session.add(cate)
    db.session.commit()


def getCategory():
    return Category.query.all()

with app.app_context():
    addCategory('Phone')
    addCategory('Car')
    addCategory('Computer')