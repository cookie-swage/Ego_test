import requests
import app

class OrderApi():
    def __init__(self):
        self.order_url = app.BASE_URL + "/api/v1/order/by_user"

    def get_order_list(self, token, page):
        params = {"page": page}
        resp = requests.get(url=self.order_url, headers=token, params=params)
        return resp