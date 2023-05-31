from flask import Flask, jsonify
from app import app

@app.route("/", methods=["GET"])
def testGet():
    return jsonify(
        { "test": "test" }
    )