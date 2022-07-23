from fastapi import APIRouter
from src.controllers import pppController

pppRouter = APIRouter()


@pppRouter.get("/{IP}/ppp/secrets")
def get_all_secrets(IP: str):
    return pppController.get_all_secret_users(IP)

@pppRouter.get("/{IP}/ppp/secret/{username}")
def get_one_secret(IP: str, username: str):
    return pppController.get_secret_user(IP, username)

@pppRouter.get("/{IP}/ppp/actives")
def get_all_actives(IP: str):
    return pppController.get_all_active_users(IP)

@pppRouter.get("/{IP}/ppp/active/{username}")
def get_one_active(IP: str, username: str):
    return pppController.get_active_user(IP,username)


# -------------Add model for update secret-----------------
@pppRouter.put("/{IP}/ppp/secret/")
def update_secret(IP: str, **kwargs):
    return pppController.update_secret_user(IP,**kwargs)

@pppRouter.delete("/{IP}/ppp/secret/{username}")
def delete_secret(IP: str, username: str):
    return pppController.delete_secret_user(IP, username)


# -------------Add model for create user-----------------
@pppRouter.post("/{IP}/ppp/secret/")
def create_secret(IP: str, **kwargs):
    return pppController.create_secret_user(IP,**kwargs)