from fastapi import APIRouter
from src.controllers import pppController

pppRouter = APIRouter()


@pppRouter.get("/{IP}/ppp/secret")
def get_secrets(IP: str):
    return pppController.get_all_secret(IP)
