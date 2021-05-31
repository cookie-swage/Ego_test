import os
# 定义项目的url
BASE_URL = "http://e.cn"
HANDERS = {"Content-Type": "application/json", "token":None }
JSON_CODE = {"code":"081bmkll2KP9774sy4nl2Fd9TT3bmklR"}


# 定义项目的根目录

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
'''
os.path.abspath(__file__)    结果是  D:\测试基础班\第五阶段 ego微商项目实战\代码接口测试\app.py   文件路径
os.path.dirname(os.path.abspath(__file__))  结果是 D:\测试基础班\第五阶段 ego微商项目实战\代码接口测试  文件的根目录
'''
 #print(BASE_DIR)
# 轮播图数据
bid = 1
#
ids = "1,2,3"
# 查询参数  用户订单
PAGE = 1