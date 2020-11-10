#字符串的驻留机制(这和java中一样)(若不是pycharm则驻留机制只会对长度为0或1的有效果)
a = "python"
b = "python"
c = "python"
print(id(a))
print(id(b))
print(id(c))#地址是相同的

#字符串的查找
print(a.index("on"))#第一次出现的位置(没有会报错)
print(a.find("l"))#没有会返回-1不会报错
print(a.rindex("on"))#最后一次出现的位置(没有会报错)
print(a.rfind("on"))#不会报错

#字符串的大小写转化
print(a.upper())#全部大写(地址发生变化了,因此证明了字符串是不可变序列)
print(a.lower())#全部转化为小写
print(a.swapcase())#大小写取反
print(a.capitalize())#首字母大写其余小写
print(a.title())#每个单词首字符大写其余小写

#字符串内容的对齐操作(格子的演示问一下!)
print(b.center(20,"*"))#居中对齐
print(b.ljust(20,"*"))#左对齐
print(b.rjust(20,"*"))#右对齐
print(b.zfill(20))#用零填充的右对齐(小于10返回原字符串)

#字符串的劈分操作
s = "hello|world Python"
print(s.split())#默认分隔符为空格,返回一个列表
print(s.split(sep="|",maxsplit=1))
#还可以用rslipt()来从右开始劈分

#字符串的判断方法
print("1.",s.isidentifier())#判断是否是合法的标识符,还可以给予序号
print(s.isspace())#是否是全由空白字符组成
print(s.isalpha())#是否全由字母组成
print(s.isdecimal())#是否全由十进制组成
print(s.isnumeric())#是否全由数字组成
print(s.isalnum())#由数字和字母组成

#字符串的替换合并
print(s.replace("Python","Java"))#替换
print(s.replace("Python","Java",1))#还可以设定替换次数
print(s.join(s))#合并字符串

#字符串的比较
#is比较的是地址
#==比较的是值

#字符串的切片操作(每一次切片都相当于创建了一个新的字符串)(可不可变都一样)
#把它当成一个列表就行了
s1 = s[2:3]
print(s1)
print(s[2:3:1])#完美版

#格式化字符串(可以避免拼接字符串所造成的浪费)
name = "张三"
age = 20.000
print("my name is %s,%f years old"%(name,age))
print("my name is {0},{1} years old".format(name,age))#这样便于识别
print(f"my name is {name},{age} years old")#这样也是可行的
print("{:10.3f}".format(age))#可以同时设置长度宽度

#字符串的编码转换
#编码就是将字符串转化为二进制数据(bytes)
#解码就是将二进制数据转化为字符串类型
s = "天涯共此时"
print(s.encode(encoding = "UTF-8"))#编码格式
byte = s.encode(encoding = "UTF-8")
print(byte.decode(encoding="UTF-8"))#解码格式必须和编码一样