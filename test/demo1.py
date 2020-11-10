from decimal import Decimal
from enum import Enum
class xz(Enum):#和java有所不同,这里还需要点一下name
    INSERT = 1
    SELECT = 2
    DELETE = 3
    UPDATE = 4
    ORDER = 5
    COUNT = 6
    SHOW = 7
    EXIT = 0
age = 18;
name = '胡小龙';
print(Decimal('1.1') + Decimal('2.2'))#具有一定的不准确性质
print(True + 1);#在python中布尔类型是可以转化为1或者0的
print("'三引号是可以在不同的"#也可以直接当作多行注释使用
      "行来输出的哦'");
print(name + '今年' + str(age));#相对于java这里必须加上一个 强制转换(括号位置不一样)
# 而不是java会自动转化为String
i = '13';
print(float(i))#整数不可以转化为整数,末尾处会自动添加一个.0
a = input()
print(a == xz.INSERT.name)