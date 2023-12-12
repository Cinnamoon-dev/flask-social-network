from functools import wraps
from flask import make_response, request
from pydantic import BaseModel, ValidationError
from werkzeug.security import generate_password_hash


class ResponseFactory:
    def successAction():
        return make_response({"error": False, "message": "Action done successfully"}, 200)

    def databaseError():
        return make_response({"error": True, "message": "Database error"}, 500)

    def notFound(field: str):
        return make_response({"error": True, "message": f"{field} not found"}, 404)
    
    def alreadyRegistered(field: str):
        return make_response({"error": True, "message": f"{field} already registered"}, 409)


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

# TODO
# Test decorator
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