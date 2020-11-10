try:
    a = int(input("1"))
    b = int(input("2"))
    print(a/b)
except ZeroDivisionError:
    print("除数不许为0")
else:
    print("程序无误")
finally:
    print("程序结束")
#java种是try catch语句来捕获异常
#同样可以多个except结构(同样是先小后大)
#同样具有else结构,同样的如果没有捕获就会执行else
#还是那个味道,还是用来释放资源的finally

#常见的异常
"""
ZeroDivisionError  被零除
IndexError  没有索引
KeyError   没有键  
NameError   未初始化对象
SyntaxError   语法错误
ValueError   输入无效的参数
"""

#traceback模块(打印错误信息)
import traceback
try:
    0("--------------")
    print(1/0)
except:
    traceback.print_exc()
#与线程相关