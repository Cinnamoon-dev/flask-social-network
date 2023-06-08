from app import app, db
from app.models.userTable import User
from flask import request, jsonify


@app.route("/user/add", methods=["POST"])
def userAdd():
    data = request.get_json()
    user = User(
        data.get("name"),
        data.get("email").lower()
    )

    if User.query.filter_by(email=data.get("email").lower()).first():
        return jsonify(
            {
                "message": "Email already registered",
                "error": True
            }
        )

    db.session.add(user)
    
    try:
        db.session.flush()
        db.session.commit()

        return jsonify(
            {
                "message": "User created successfully",
                "error": False
            }
        )
    except:
        db.session.rollback()

        return jsonify(
            {
                "message": "User creation failed",
                "error": True
            }
        )