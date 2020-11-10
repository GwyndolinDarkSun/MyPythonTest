#while循环和java中换汤不换药,同样是大括号换成了:而已
i = 10;
while(i < 100):
    print(i)
    i += 1;

j = 0;
m = 0;
while(j <= 100):
    m += j;
    j += 2;
print(m)

j1 = 0;
m1 = 0;
while(j1 <= 100):
    if((j1%2) == 0):
        m1 += j1;
    j1 += 1;
print(m1)

#for in 循环,对应java中的foreach循环
r = range(0,10)
for item in r :
    print(item)
    #每次循环都是将r中的序列依次取出来交给item
    #对比java就是少了一个声明变量的过程,并且in代替了:   :代替了大括号

#如果不需要用到自定义变量,则可以用 _ 这样虽然不能迭代,但是循环次数是不变的,这样就变形成为了for循环
x = 0;
i = 0;
for _ in range(100):
    x += i;
    i += 1;

print(x)
#可以直接规定循环次数可真是太方便了  123


#水仙花数判断
for i in range(100,1000):
    if(i == (i%10)**3 + (i//10%10)**3 + (i//100)**3):#分别获取个位十位百位数(一定要区分java中默认整除而这里用//)
        print(i)#用%10的思想来获取个个位数


#break和continue和java中效果是差不多的
#break结束循环,continue是终止本次循环

#else在python中有一些特殊的用法,在和非if搭配的时候,除非break否则在循环结束的时候就会运行(补充说明的作用)
i = 0;
for _ in range(10):
    i += 1;
    print(i)
else:
    print("循环执行了" + str(i) + "次")
    #连体婴




