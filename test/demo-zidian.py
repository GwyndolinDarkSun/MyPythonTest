#字典也是一个数据结构,是一个可变数列
#字典的key和value就和java中的map集合中的key和value类似,
#字典中的key会自动按照一定顺序排列(同java中的hash map的排序的hash函数计算相同)(无序不可变)
# (但是key不可重复这点和hash map不同)

#字典的实现原理:
#可以根据key查询value
zd1 = {"longer" : "gou" , "longer1" : "taigoule"};
zd2 = {"longer" : "gou" , "longer1" : "taigoule"};
print(id(zd1))
print(id(zd2))

zd3 = dict(name = "胡小龙" , like = "gou")
zd4 = dict(name = "胡小龙" , like = "gou")
print(id(zd3))
print(id(zd4))

#字典元素的获取:
str1 = zd1.get("longer")
str2 = zd1["longer"]
print(str1)
print(str2)

print(zd1.get("dongge",233))#233就是当不存在key时默认的value

#判断 增删改
print("longer" in zd1)
zd1["longer2"] = "jugou"
del zd2["longer"];
print("longer" not in zd2)

#字典中的视图操作
keys = zd1.keys();#获取所有的key
print(keys)
print(zd1.values())#获取所有的value
print(zd1.items())#获取所有的key和value

#遍历以下字典吧
for item in zd1:
    print(item)

#总结下字典的特点吧
#元素都是以对形式,key不可重复,value可以重复
#元素都是无序的
#key不可变化对象
#可以动态的伸缩
#会浪费大量内存(有空余的空间)

#字典生成式
prise = ["sadfadf","dasfdf","dasfadfasf"]
keysss = [1,2,3]
aaaa = {a:b for a,b in zip(keysss,prise)}
print(aaaa)