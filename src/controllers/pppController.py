from src.services import pppService

def get_all_secret(IP: str):
    data = pppService.ros_get_secrets(IP)
    return {
        "status": "success",
        "data": data,
    }

def get_all_active():
    return {"message": "Hello World"}

def update_secret():
    return {"message": "Hello World"}

def delete_secret():
    return {"message": "Hello World"}

def get_secret():
    return {"message": "Hello World"}

def get_active():
    return {"message": "Hello World"}