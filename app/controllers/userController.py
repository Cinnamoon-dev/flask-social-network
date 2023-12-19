from app import app, db 
from flask import request, jsonify
from app import User, UserAddSchema, UserEditSchema
from werkzeug.security import generate_password_hash
from app.controllers import ResponseFactory, request_validator, paginate, instance_update


@app.route("/user/add", methods=["POST"])
@request_validator(UserAddSchema)
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
    page = request.args.get("page", 1, type=int)
    rows_per_page = request.args.get("rows_per_page", app.config["ROWS_PER_PAGE"], type=int)
    userQuery = User.query

    users, output = paginate(userQuery, page, rows_per_page)

    for user in users:
        data = user.to_dict()
        output["itens"].append(data)
    
    return jsonify(output)


@app.route("/user/view/<int:id>", methods=["GET"])
def userView(id: int):
    user = User.query.get(id)

    if not user:
        return ResponseFactory.notFound(f"User {id}")

    data = {
        "user": user.to_dict(),
        "error": False
    }

    return jsonify(data)


@app.route("/user/edit/<int:id>", methods=["PUT"])
@request_validator(UserEditSchema)
def userEdit(id: int):
    data = request.get_json()
    user = User.query.get(id)

    if not user:
        return ResponseFactory.notFound(f"User {id}")

    instance_update(user, data)
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
        return ResponseFactory.notFound(f"User {id}") 
    
    db.session.delete(user)

    try:
        db.session.flush()
        db.session.commit()

        return ResponseFactory.successAction()
    
    except:
        db.session.rollback()

        return ResponseFactory.databaseError()