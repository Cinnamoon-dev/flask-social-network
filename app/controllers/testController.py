from flask import jsonify
from app import app

@app.route("/", methods=["GET"])
def testGet():
    return jsonify(
        { "test": "test" }
    )
