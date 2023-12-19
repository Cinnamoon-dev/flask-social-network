import re
from typing import Optional
from pydantic import BaseModel, field_validator


class UserAddSchema(BaseModel):
    name: str
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def email_validator(cls, email):
        email = email.lower()
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is None:
            raise ValueError('Insert a valid email')
        return email

class UserEditSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

    @field_validator("email")
    @classmethod
    def email_validator(cls, email):
        email = email.lower()
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is None:
            raise ValueError('Insert a valid email')
        return email