#集合的定义,
#一个内置的数据结构
#与列表,字典一样都是属于可变类型的序列
#集合是没有value的字典(value才可以是一个元组)

#来创建一个集合
s = {12,123,5454,1,2}#仅仅是让value少了的字典(字典是中括号,列表也是中括号)元组是大括号
print(s)
print(set(range(6)))#把range的整数序列转化为集合
print(set(range(6,10,2)))#这里复习一下range函数(开始,结束,步数)默认0开始
print(set("python"))#可以拆解字符串
print(set([6-9]))#元组是小括号
print(s.add("afaf"))#一次添加一个元素
print(s.update("121212"))#添加多个元素
s.update("121212")
s.update((1512,23113,21313))#要以元组的形式
s.update([12,11,1111111])#或者是列表的方式
print(s)
s.pop#随机删除一个元素
s.remove(12)
s.remove(123)#和discard()相比,该方法需要抛出异常
print(s)
s.clear()#还是clear还是清空操作

#集合间的关系
s1 = {12,1,2,3}
s2 = {3,2,1,12}
print(id(s1),id(s2))#地址不同
print(s1 == s2)#内容都会自动排序、
print(s1.issubset(s2))#判断s1是否是s2的子集
print(s1.issuperset(s2))#判断s1是否是s2的超集
print(s1.isdisjoint(s2))#判断s1和s2是否有交集

#数学操作
s3 = {21,2121,2555}
print(s1.intersection(s3))#求交集
print(s1 & s2)#这和and操作都是等价的
print(s1.difference(s3))#二者的差集
print(s1.symmetric_difference(s3))#二者对称差集

#集合生成式
s4 = {i * i for i in range(1,20)}#就是一个迭代出来然后在拿这个迭代物来生成集合元素这和列表一样的