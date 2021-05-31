import requests

import app


class IndexApi(object):
    def __init__(self):
        self.banner_url = app.BASE_URL + "/api/v1/banner/{}"   # 这个1 是变化的
        self.theme_url = app.BASE_URL + "/api/v1/theme"
        self.recent_url = app.BASE_URL + "/api/v1/product/recent"

    # 获取轮播图
    def get_banner(self, banner_id):
        new_url = self.banner_url.format(banner_id)
        resp = requests.get(new_url)
        return resp
    # 获取专题栏位
    def get_theme(self,ids):
        param = {"ids":ids}
        resp = requests.get(self.theme_url, params=param)    # params 就是查询参数
        return resp
    # 获取最近新品
    def get_recent_product(self):
        resp = requests.get(self.recent_url)
        return resp




