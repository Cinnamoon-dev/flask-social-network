import pytest
from flask import Flask
from app import app as _app, db as _db

@pytest.fixture()
def app():
    _app.config.update({
        "TESTING": True,
        "STAGE" : 'test',
        "SQLALCHEMY_DATABASE_URI": "http:///storage.db"
    })

    yield _app

    with _app.app_context():
        _db.drop_all()
        _db.create_all()
    
    return _app

@pytest.fixture
def client(app: Flask):
    yield app.test_client()

@pytest.fixture
def runner(app: Flask):
    yield app.test_cli_runner()