from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

sys.path.append("./")


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:14042002@localhost:3306/saledb'


db = SQLAlchemy(app=app)
