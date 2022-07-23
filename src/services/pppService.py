from src.services.mikrotik import Mikrotik

class PPPService(Mikrotik):

    def __init__(self, host):
        super().__init__(host)

    
    def get_secrets(self):
        data = self.api.get_resource('/ppp/secret').get()
        return data

    def get_secret(self,username:str):
        data = self.api.get_binary_resource('/ppp/secret/').call('print', {'numbers': username.encode()})
        return data


    def get_actives(self):
        data = self.api.get_resource('/ppp/active').get()
        return data

    def update_secret(self,**kwargs:dict):
        data = self.api.get_binary_resource('/ppp/secret/').call('set', {**kwargs.encode()})
        return data

    def delete_secret(self,username:str):
        self.api.get_binary_resource().call('/ppp/secret/remove', {'numbers': username.encode()})
        return True