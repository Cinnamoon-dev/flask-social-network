DEBUG = True

USER = "postgres"
PASSWORD = "1234"
HOST = "localhost"
PORT = "5432"
DATABASE_NAME = "flask-social"

DATABASE = {
    "sqlite": "sqlite:///storage.db",
    "postgres": f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
}

SQLALCHEMY_DATABASE_URI = DATABASE["sqlite"]
SQLALCHEMY_TRACK_MODIFICATIONS = True