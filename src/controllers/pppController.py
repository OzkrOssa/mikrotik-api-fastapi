from src.services.pppService import PPPService

def get_all_secret_users(IP: str):
    data = PPPService(IP).get_secrets()
    return {
        "status": "success",
        "data": data,
    }

def get_all_active_users(IP:str):
    data = PPPService(IP).get_actives()
    return {
        "status": "success",
        "data": data,
    }

def update_secret_user(IP:str, **kwargs):
    PPPService(IP).update_secret(**kwargs)
    return {
        "status": "success",
        "message": "Secret updated",
    }

def delete_secret_user(IP:str, username:str):
    PPPService(IP).delete_secret(username)
    return {
        "status": "success",
        "message": "Secret deleted",
    }

def get_secret_user(IP:str, username:str):
    data = PPPService(IP).get_secret(username)
    print(data)
    return {
        "status": "success",
        "data": data,
    }

def get_active_user(IP:str, username:str):
    data = PPPService(IP).get_active(username)
    return {
        "status": "success",
        "data": data,
    }