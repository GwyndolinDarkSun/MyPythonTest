#始终记住返回的是一个迭代器,它和java一样不去迭代你是不知到其中元素到底是谁的!!

#创建方式1
r = range(10);
print(r);#居然可以直接输出一个序列(并不能直接看到其中的元素)
#一个数的时候就是0开始有10个数的序列
print(list(r))#查看

#创建方式2
r = range(1,2)
#1开始走2步

#创建方式3
r = range(1,10,5)
print(list(r))
#步长就是相邻的两个元素之间相差的元素是多少

#10不在其中
print(10 in r)