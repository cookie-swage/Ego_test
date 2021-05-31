import logging
import unittest

import app
from api.index import IndexApi


class Testidex(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.index_api = IndexApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass


    def test01_get_banner(self):
        banner_id = app.bid
        resp = self.index_api.get_banner(banner_id)
        json_data = resp.json()
        logging.info(f"获取轮播图的结果:{json_data}")      # f格式化的一种方法
        self.assertEqual(200, resp.status_code)
        self.assertEqual(banner_id,json_data.get("id"))

    def test02_get_theme(self):
        ids = app.ids
        resp = self.index_api.get_theme(ids)
        json_data = resp.json()
        logging.info(f"获取专题栏位的结果:{json_data}")
        self.assertEqual(200,resp.status_code)
        self.assertTrue(len(json_data) > 0)

    def test03_get_recent(self):
        resp = self.index_api.get_recent_product()
        json_data = resp.json()
        logging.info(f"获取最近新品的结果:{json_data}")
        self.assertEqual(200,resp.status_code)
        self.assertTrue(len(json_data) > 0)



