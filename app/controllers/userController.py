from app import app, db 
from flask import request
from app import User, UserSchema
from app.controllers import ResponseFactory, request_validator
from werkzeug.security import generate_password_hash


@app.route("/user/add", methods=["POST"])
@request_validator(UserSchema)
def userAdd():
    data = request.get_json()
    user = User(
        data.get("name"),
        data.get("email").lower(),
        data.get("password")
    )
    
    if User.query.filter_by(email=data.get("email").lower()).first():
        return ResponseFactory.alreadyRegistered("Email") 

    db.session.add(user)
    
    try:
        db.session.flush()
        db.session.commit()

        return ResponseFactory.successAction()
    
    except:
        db.session.rollback()

        return ResponseFactory.databaseError() 


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
        return ResponseFactory.notFound("User")

    data = {
        "user": user.to_dict(),
        "error": False
    }

    return data


@request_validator(UserSchema)
@app.route("/user/edit/<int:id>", methods=["PUT"])
def userEdit(id: int):
    data = request.get_json()
    user = User.query.get(id)

    if not user:
        return ResponseFactory.notFound("User")
    
    user.name = data.get("name")
    user.email = data.get("email")
    user.password = generate_password_hash(data.get("password"), "scrypt")

    db.session.add(user)

    try:
        db.session.flush()
        db.session.commit()

        return ResponseFactory.successAction()

    except:
        db.session.rollback()

        return ResponseFactory.databaseError()


@app.route("/user/delete/<int:id>", methods=["DELETE"])
def userDelete(id: int):
    user = User.query.get(id)

    if not user:
        return ResponseFactory.notFound("User") 
    
    db.session.delete(user)

    try:
        db.session.flush()
        db.session.commit()

        return ResponseFactory.successAction()
    
    except:
        db.session.rollback()

        return ResponseFactory.databaseError()