from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object("config")

CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.models.userTable import User

from app.controllers import userController
