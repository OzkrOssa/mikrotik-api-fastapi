import routeros_api
import os

from dotenv import load_dotenv

load_dotenv()

class Mikrotik:

    def __init__(self, host):
        
        self.host = host
        username = os.getenv("API_USER")
        password = os.getenv("API_PASS")
        self.api = routeros_api.RouterOsApiPool(host, username=username, password=password, plaintext_login=True).get_api()
        