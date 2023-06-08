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


@app.route("/user/all", methods=["GET"])
def userAll():
    users = User.query.all()
    all = {
        "users": []
    }

    for user in users:
        data = user.to_dict()
        all["users"].append(data)

    return all


@app.route("/user/view/<int:id>", methods=["GET"])
def userView(id: int):
    user = User.query.get(id)

    if not user:
        return {
            "message": "User not found",
            "error": True
        }

    data = {
        "user": user.to_dict(),
        "error": False
    }

    return data


@app.route("/user/edit/<int:id>", methods=["PUT"])
def userEdit(id: int):
    data = request.get_json()
    user = User.query.get(id)

    if not user:
        return {
            "message": "User not found",
            "error": True
        }
    
    user.name = data.get("name")
    user.email = data.get("email")

    db.session.add(user)

    try:
        db.session.flush()
        db.session.commit()

        return {
            "message": "User successfully edited",
            "error": False
        }

    except:
        db.session.rollback()

        return {
            "message": "User edition failed",
            "error": True
        }


@app.route("/user/delete/<int:id>", methods=["DELETE"])
def userDelete(id: int):
    user = User.query.get(id)

    if not user:
        return {
            "message": "User not found",
            "error": True
        }
    
    db.session.delete(user)

    try:
        db.session.flush()
        db.session.commit()

        return {
            "message": "User deleted successfully",
            "error": False
        }
    
    except:
        db.session.rollback()

        return {
            "message": "User could not be deleted",
            "error": True
        }