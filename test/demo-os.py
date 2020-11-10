#os是python内置的操作系统功能和文件系统功能祥光的模块
import os
#打开一个记事本
os.system("notepad.exe")
#打开一个计算器
os.system("calc.exe")
#直接调用可执行文件
os.startfile("E:\\ff14插件\\ACT国服整合\\CafeACT.exe")
"""
getcwd()返回当前工作目录
listdir(path)返回指定路径下文件的目录和信息
mkdir(path[,mode])创建目录
makedirs(path1/path2/...[,mode])创建多级目录
rmdir(path)删除目录
removedirs(path2/path2...)删除多级目录
chdir(path)将path设置为当前工作目录
"""

