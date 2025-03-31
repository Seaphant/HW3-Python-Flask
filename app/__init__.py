from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'devkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login = LoginManager(app)
csrf = CSRFProtect(app)

from app import routes

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
