#import 模组名称 [as 别名]
#from 模组名称 import 函数/变量/类

#以主程序的形式运行
"""
当以主程序方式运行:有些时候我们希望有些程序不会总是运行时
if __name__ == '__main__'
    程序内容
"""
#可以用  import 包名.模组名称 导入包
#总有一个__init__.py 文件

#一些常用的模块
import sys
print(sys.getsizeof(24))
print(sys.getsizeof(45))#获取字节

import time
print(time.time())
print(time.localtime(time.time()))#转化为本地时间
"""
os访问操作系统服务功能
calender提供日期相关各种函数
urllib读取服务器的数据
json使用序列化和反序列化
re字符串中正则表达式的匹配和替换
math算数
decimal具有极高精度的十进制运算
logging提供日志记录
"""

import urllib.request
print(urllib.request.urlopen("http://www.baidu.com").read())
"""
这种在线安装一定要保证解释器是自己安装的而不是python自带的
#第三方模块的安装(在线安装)
#pip install 模块名

import schedule
def job():
    print("胡小龙太狗了")

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
"""


