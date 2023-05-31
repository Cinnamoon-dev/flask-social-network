from flask import Flask, jsonify
import os

app = Flask(__name__)

from app.controllers import testController
