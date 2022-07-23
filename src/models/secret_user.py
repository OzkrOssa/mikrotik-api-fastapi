from pydantic import BaseModel

class SecretUser(BaseModel):
    username: str
    password:str
    profile:str
    comment:str