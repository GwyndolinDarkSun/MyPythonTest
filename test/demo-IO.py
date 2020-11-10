#IO就是文件的读写操作
#打开文件对象
file = open('demo-txt1',mode='r',encoding='UTF-8')
print(file.readlines())
file.close()
"""
r 表示只读
w 表示只写
a 表示添加
b 以二进制打开
+ 以读写方式打开
"""
file = open("demo-txt1",mode="w",encoding="UTF-8")
file.write("是真的狗")
"""
read(size)指定长度
readline()读取一行
readlines()将每一行作为一个独立的字符串对象
writelines(list)将字符串列表写入文件,不换行
seek(a[,b])将光标移动到指定位置,a表示相对于b的位置
"""

#with语句(上下文管理器)
with open("demo-txt1",mode="r",encoding="UTF-8") as file:
    print(file.read())
    print(type(file))
"""
实现了__enter__()方法和__exit__()方法的类称为遵守了上下文管理协议,该类的实例化对象成为上下文管理器
实际上就是以一种 夹 的方式,上述两种方法夹住write()方法,这样就可以自动开启关闭了
不只这里可以用,只要是重复进行的"开启""结束"的动作都可以通过上下文管理器来减少代码的复写,同时可以防止错误
"""