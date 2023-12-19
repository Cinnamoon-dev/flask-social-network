from typing import Optional
from pydantic import BaseModel


class UserAddSchema(BaseModel):
    name: str
    email: str
    password: str

class UserEditSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None