from functools import wraps
from flask_sqlalchemy import BaseQuery
from pydantic import BaseModel, ValidationError
from flask import make_response, request, jsonify
from werkzeug.security import generate_password_hash


class ResponseFactory:
    def successAction():
        return make_response(jsonify({"error": False, "message": "Action done successfully"}), 200)

    def databaseError():
        return make_response(jsonify({"error": True, "message": "Database error"}), 500)

    def notFound(field: str):
        return make_response(jsonify({"error": True, "message": f"{field} not found"}), 404)
    
    def alreadyRegistered(field: str):
        return make_response(jsonify({"error": True, "message": f"{field} already registered"}), 409)


# update table line
def instance_update(instance, request_json):
    """
    This function updates every key received from the request in an instance of a table, if the key exists in that table.
    
    Example: The table User has three columns (id, name, email) and the request object has five fields (name, age, bloodType, email, address).
    The updated fields in the instance will be (name, email).

    The parameter instance should be a query from a table (class that extends BaseModel). 

    `instance = Table.query.get(id)`
    """

    instance_keys = list(instance.to_dict().keys())

    for key in instance_keys:
        if key in request_json:
            setattr(instance, key, request_json.get(key))
    
    if "email" in request_json:
        setattr(instance, 'email', request_json.get("email").lower())
    
    if "password" in request_json:
        setattr(instance, 'password', generate_password_hash(request_json.get("password"), method="sha256"))


# pydantic validator
def request_validator(ModelClass: BaseModel):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            data = request.get_json()

            try:
                ModelClass.model_validate(data)
            except ValidationError as e:
                return make_response({"error": True, "message": e.json()}, 400)

            return f(*args, **kwargs)
        return wrapped
    return wrapper


# item pagination
def paginate(query: BaseQuery, page: int=1, rows_per_page: int=1):

    pagination = query.paginate(page=page, per_page=rows_per_page, error_out=False)

    data = pagination.items

    output = {
        "pagination": {
            "pages_count": pagination.pages,
            "itens_count": pagination.total,
            "itens_per_page": rows_per_page,
            "prev": pagination.prev_num,
            "next": pagination.next_num,
            "current": pagination.page,
        },
        "itens": [],
        "error": False,
    }

    return data, output