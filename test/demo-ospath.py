#os.path也可以操作目录
import os.path
print(os.path.abspath("demo1.py"))
print(os.path.exists("demo2.py"))
print(os.path.join())#拼接文件名
print(os.path.split())#分割文件名
print(os.path.splitext())#分割文件名字和后缀名
"""
basename(path)提取文件名
dirname(path)提取文件路径
isdiar(path)判断是否为路径
"""