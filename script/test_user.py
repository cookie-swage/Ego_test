import unittest
import logging
import app
from api.order import OrderApi
from api.user import UserApi


class TestUserApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.token_api = UserApi()
        cls.order_api = OrderApi()

    def test01_verfly_token_ok(self):
        # 获取token
        resp = self.token_api.get_token()
        token = resp.json().get("token")
        app.HANDERS["token"] = token  # 定义一个全局变量
        print(app.HANDERS)
        # 验证token
        resp1 = self.token_api.verify_token(token)
        # print(resp1.json())
        json_data = resp1.json()
        logging.info(f"验证token结果:{json_data}")
        self.assertEqual(200, resp1.status_code)
        self.assertEqual(True, resp1.json().get("isValid"))


    # 登录成功
    def test02_address_ok(self):
        # print(app.HANDERS)
        resp = self.token_api.get_address(app.HANDERS)
        json_data = resp.json()
        # print(json_data)
        logging.info(f"登录成功的结果:{json_data}")
        self.assertEqual(200, resp.status_code)
        self.assertEqual("020-81167888", json_data.get("mobile"))

    def test03_order_list(self):
        page = app.PAGE                 #查询参数的传入
        print(app.HANDERS)
        resp = self.order_api.get_order_list(app.HANDERS, page)
        json_data = resp.json()
        print(json_data)
        logging.info(f"获取的订单列表:{json_data}")
        self.assertEqual(200,resp.status_code)
        # self.assertTrue(len(resp.json.data() > 0))

