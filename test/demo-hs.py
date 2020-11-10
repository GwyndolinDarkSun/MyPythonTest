#函数要调用才能使用(完成特定功能的代码)就是java中的方法(有返回值的)

def cale(a,b):
    return a*b;
print(cale(2,3))#还是把java中括号改成了冒号(可以不声明返回值类型)

#实参的传递分为两种
print(cale(b=10,a=20))#不按照顺序传递的话就必须声明实参名字(关键字参数)
print(cale(10,20))

#函数参数传递的内存地址
def fun(arg1,arg2):
    print(arg1)
    print(arg2)
    arg1 = 100;
    arg2.append(10)
    print(arg1)
    print(arg2)

n1 = 11;
n2 = [22,33,44]
print(n1)
print(n2)
print("---------------------")
fun(n1,n2)
print(n1)
print(n2)#和java一样,新参只是一个代替的值
#如果是可变对象,那么函数体的修改会影响实参的值
#这其实和java中是一样的,因为传递过去的是对象的保存地址,如果是可变序列,
#那么他修改的就会是指向的哪个对象,如果是不可变的,那么函数体中的参数就会是指向一个新的对象
#当返回值为多个时,就会返回元组,这个java中返回数组是一个道理

lst = list([1,2,3,4,4])
def luck(lst):
    lst[0] = 10;
    return lst
print(luck(lst))

#默认值参数
def lkk(a,b=10):
    print(a,b)
lkk(100)#不指定就是默认,也可以指定,print()函数就是一个很好的默认值参数的例子

#可变长参数
def hxl(*args):
    print(args)
#java中则是以数组或者是...的方式实现这一点的
#只能定义一个
#而关键字参数返回的是字典


print("asdfasdf")