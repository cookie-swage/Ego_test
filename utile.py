'''
1.导包
2.定义初始化日志函数  可以查找错误
    1.创建日志器
    2.创建处理器
    3.创建格式化器
    4.将格式化器条件到处理器中
    5.将处理器添加到日志器中

'''
# 1.导包
import logging
import app
from logging import handlers
import time
# 2.定义初始化日志函数
def init_log():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # 设置日志的级别 一共六级
    # 创建处理器
    sh = logging.StreamHandler()# 控制台处理器
    log_file = app.BASE_DIR + "/log/ego.log_{}".format(time.strftime("%Y%m%d-%Y%M%S")) # 文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(log_file,        # 日志文件
                                                   when='midnight', # 开始记录时间
                                                   interval=1,      # 记录频率
                                                   backupCount=7,   # 备份日志时间
                                                encoding='utf-8')# 编码方式
    # 3.创建格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    # 4.将格式化器条件到处理器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #5.将处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)

if __name__ == '__main__':
    init_log()
    logging.info("这是一个测试函数")

'''
fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s" 对应的信息
           |              |             |          |        |              |               |
输出结果:  2021-05-29 10:22:11,968 INFO [root] [utile.py  (<module>:       41)] -              这是一个测试函数
'''



