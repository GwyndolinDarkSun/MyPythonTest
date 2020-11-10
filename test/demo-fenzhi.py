print(bool(0))
print(bool(0.0))
#无论是浮点类型还是整数的0都可以转化为布尔类型,java中则都不可以
print(bool(None))#None相当于java中的null
print(bool(''))
print(bool(""))
print(bool([]))#空列表
print(bool(list))#空列表
print(bool(()))#空元组
print(bool(tuple()))#空元组
print(bool({}))#空字典
print(bool(dict()))#空字典
print(bool(set()))#空集合
#对于python中这些都相当于对象,因此bool非常的灵活,不想java中boolean必须以判断的形式体现
#只要是 空 就可以转化为false, 非空 就是true,因此python可以用bool来判断是否非空,不像
#java中必须用null来判断引用或者为空,很多时候还要转化为bool,因此pytho0在这方面有时可以省略
#这就是其具备的优点了
