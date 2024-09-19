from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

# link externo do banco (criar as tabelas)
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://banco_fakepinterest_ws41_user:yM8beJ3jVkxjmnvBr6rzhzSLL0XGYDUE@dpg-crlofstumphs73eajlpg-a.oregon-postgres.render.com/banco_fakepinterest_ws41"
app.config["SECRET_KEY"] = "861432d83a520c9c139406e464ba73ab"
app.config["UPLOAD_FOLDER"] = "static/fotos_post"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


from Pinterest import routes

