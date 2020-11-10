lst1 = [1,2,3]
lst2 = [1,2,3]
print(id(lst1))
print(id(lst2))#两个列表的地址明显不一致,因此指向的是不同的对象

lst1[1] = 3;
print(id(lst1))#改变1的值,地址并未发生变化,证明了改变的是对象而不是一个新的引用
print(lst2)

str1 = "longer"
str2 = "longer"
print(id(str1))
print(id(str2))#地址一样,和java中String常量池的存储方式类似