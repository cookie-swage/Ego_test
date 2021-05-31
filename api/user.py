import requests
import app

class UserApi():
    def __init__(self):
        self.token_url = app.BASE_URL + "/api/v1/token/user"
        self.verify_token_url = app.BASE_URL + "/api/v1/token/verify"
        self.address_url = app.BASE_URL + "/api/v1/address"
        


    def get_token(self):
        resp = requests.post(url=self.token_url, headers= app.HANDERS, json=app.JSON_CODE)

        return resp

    def verify_token(self,token):
        resp = requests.post(url=self.verify_token_url, headers=app.HANDERS, json=token)
        return resp
    def get_address(self,token):

        resp =  requests.get(url=self.address_url, headers= token)
        return resp

