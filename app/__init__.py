from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import pymysql
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)
db = pymysql.connect("localhost",'root','0','mydb')
migrate = Migrate(app,db)
login = LoginManager(app)
bootstrap = Bootstrap(app)


from app import view
