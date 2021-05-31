import unittest
import app
from tools import  HTMLTestRunner_PY3
from script.test_index import Testidex
from script.test_user import TestUserApi

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Testidex))
suite.addTest(unittest.makeSuite(TestUserApi))

#runner = unittest.TextTestRunner()
#runner.run(suite)

# 定义报告文件
reporter_file = app.BASE_DIR + '/report/Ego.html'

#  打开报告文件写入结果
with open(reporter_file, mode='wb') as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,
                                               verbosity=1,
                                               title= "ego小程序测试报告",
                                               description="v1.0版本")
    runner.run(suite)
