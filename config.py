DEBUG = True

USER = "postgres"
PASSWORD = "postgres"
HOST = "flask_db"
PORT = "5432"
DATABASE_NAME = "postgres"

DATABASE = {
    "sqlite": "sqlite:///storage.db",
    "postgres": f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
}

SQLALCHEMY_DATABASE_URI = DATABASE["postgres"]
SQLALCHEMY_TRACK_MODIFICATIONS = True