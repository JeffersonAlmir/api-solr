from flask import Flask
from flask_restful import Api
import os


app = Flask(__name__)

DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
# DB_PORT = os.environ["DB_PORT"]

# DB_USER = os.environ.get("DB_USER", "postgres")
# DB_PASSWORD = os.environ.get("DB_PASSWORD", "12345")
# DB_HOST = os.environ.get("DB_HOST", "localhost")
# DB_PORT = os.environ.get("DB_PORT", "5434")
# DB_NAME = os.environ.get("DB_NAME", "meu_banco")


app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)