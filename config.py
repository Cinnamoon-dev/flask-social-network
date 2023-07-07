DEBUG = True

USER = "postgres"
PASSWORD = "1234"
HOST = "localhost"
DATABASE_NAME = "flask-social"

DATABASE = {
    "sqlite": "sqlite:///storage.db",
    "postgres": f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE_NAME}"
}

SQLALCHEMY_DATABASE_URI = DATABASE["sqlite"]
SQLALCHEMY_TRACK_MODIFICATIONS = True