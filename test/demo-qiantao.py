for i in range(1,9+1):
    for i1 in range(1,i+1):#因为是左开右闭区间,因此右边必须多一个(3个参数才会有步长)
        print(str(i) + "*" + str(i1) + "=" +str(i*i1),end="\t")#这样可以保证不换行输出

    print("   ")

