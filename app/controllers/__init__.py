from flask import request
from werkzeug.security import generate_password_hash


# update table line
def instance_update(instance):
    """
    This function updates every key received from the request in an instance of a table, if the key exists in that table.
    
    Example: The table User has three columns (id, name, email) and the request object has five fields (name, age, bloodType, email, address).
    The updated fields in the instance will be (name, email).

    The parameter instance should be a query from a table(class) that inherited BaseModel. 

    `instance = User.query.get(id)`
    """

    data = request.get_json()
    instance_keys = list(instance.to_dict().keys())

    for key in instance_keys:
        if key in data:
            setattr(instance, key, data.get(key))
    
    if "email" in data:
        setattr(instance, 'email', data.get("email").lower())
    
    if "password" in data:
        setattr(instance, 'password', generate_password_hash(data.get("password"), method="sha256"))