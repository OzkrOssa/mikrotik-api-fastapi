import routeros_api
import os
from dotenv import load_dotenv

load_dotenv()

def ros_get_secrets(host):

    username = os.getenv("API_USER")
    password = os.getenv("API_PASS")

    api = routeros_api.RouterOsApiPool(host, username=username, password=password, plaintext_login=True).get_api()
    data = api.get_resource('/ppp/secret').get()

    return data
