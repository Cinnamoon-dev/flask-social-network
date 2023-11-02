import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True

USER = os.getenv('POSTGRES_USER', 'postgres')
PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
HOST = os.getenv('POSTGRES_HOST', 'localhost')
PORT = os.getenv('POSTGRES_PORT', 5432)
DATABASE_NAME = os.getenv('POSTGRES_DB', 'postgres')

DATABASE = {
    "sqlite": "sqlite:///storage.db",
    "postgres": f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
}

SQLALCHEMY_DATABASE_URI = DATABASE["sqlite"]
SQLALCHEMY_TRACK_MODIFICATIONS = True
