#python种一切都是对象,java种基本数据类型不是对象
#python中类也是一个对象
class Student:
    native_pace = "达州" #类的属性
    age = None
    name = None
    __lsp = "sdafadf"#这样就封装了,相当于java中的private
    #初始化方法(仅仅是用来初始化的)
    def __init__(self,name,age):#啊这,不就是构造方法的变形嘛(实际上是把java中的构造方法分为了构造方法和初始化方法)
        self.name = name;
        self.age = age;#代替了this关键字

    # 实例方法
    def eat(self):
        print("胡小龙在吃麻辣鞭")
#在类之外定义的称为函数(可以不用.的方式引用)
#相比于java多了一个函数和类方法...
    @staticmethod
    def method():
        print("静态方法")
#还有类方法(可以使用类名直接访问的方法)
    @classmethod
    def cm(cls):
        print("类方法")


print(id(Student))
print(type(Student))
print(Student)
#这里是默认new了一个对象

#创建一个对象
stu = Student("胡小龙",18)#直接少了new
s1 = str("dd")
s2 = str("dd")
print(id(s1))
print(id(s2))
print(Student.name)#还可以不new对象就直接输出类中具有的属性
#实例方法无论是类名还是实例名.都可以调用(不过类一般需要传递一个对象)
stu.eat()#只能实例对象调用


#重点来了,python是动态语言,可以动态的绑定属性方法
stu.xg = "打呼噜"
print(stu.xg)
def dh():
    print("胡小龙在打呼噜了")

#封装
stu.dh = dh()
stu.dh
print(dir(stu))#查看当前类的属性方法
print(stu._Student__lsp)#这也可以使用啊(靠自觉)





#继承(重写可以调用父类的方法)(重写和java中的一样)
class HuXiaoLong(Student):#就是这样继承的(还是那个味道)
    pass
    def __init__(self,name,age):
        super().__init__(self,name,age)#java中是直接在括号里面

class Person:
    name = None;
    age = 0;
    def __init__(self,name,age):
        print("初始化方法调用")
    def sj(self):
        print("开始睡觉")


class Teacher(Person):#创建对象输入的对象是类对象,初始化对象所输入的对象是new出来的对象
    teacherOfYear = 0;
    def sj(self):
        print("胡小龙")
        super().sj()#可以使用这种方式调用父类的方法(java中则直接在括号中添加新参,从而让虚拟机自动匹配相应的构造器)(python没有this和super关键字)
    def __init__(self,name,age,teacherOfYear):#java中是以一个同名的方法的方式创建构造方法的
        super().__init__(name,age)#(java中需要对应参数类型的构造,但是这里不写就会默认一个同样的参数构造)这里和java一样如果形参没有那么就不会在new对象的时候给予相应的赋值(这样不会指定调用的构造方法,默认无参)

        """
        如果是super()那么就不会调用初始化方法,那么你的初始化方法就会变得没有意义,
        这里最好指定调用的初始化方法
        因为java中两者是一体的
        python中分开相当于自动有一个 默认的构造方法,不必担心java中没有默认构造方法的情况
        因此需要区分这点上和java的区别
        """
        self.teacherOfYear = teacherOfYear;


teacher = Teacher("张三",65,60)
print(teacher.teacherOfYear)
teacher.sj()
#__str__方法相当于java中的toString()方法




#多态(不知道引用变量是什么类型,任然可以调用方法,再根据运行过程来决定调用谁的方法)
#在和继承结合的时候其实差不多(但是python中是没有数据类型的,因此多态性没有java那么明显)
class Animal:
    def eat(self):
        print("动物在吃东西")
class Dog(Animal):
    def eat(self):
        print("狗儿在啃骨头")
class HXL:
    def eat(self):
        print("胡小龙在吃shi")

class Person:
    def feed(obj,animal):
        animal.eat()

person = Person()
person.feed(HXL())#java可不敢这样没有继承关系的调用方法(因为你不知道是否具有该方法)

#一个只关心行为的面向对象语言,只要具有动作就可以看作一个类型
"""
静态语言实现多态三种条件(java)
继承
方法重写
父类引用指向子类对象(主要还是看对象,父类只是会让超出范围的属性方法报错,这就需要向下转型)
"""

#一些特殊的属性
print(dir(object))
print(Teacher.__dict__)#就类似于toString方法
print(person.__class__)#输出类对象类型(只有这位是直接类的引用)
dog = Dog()
print(Dog.__bases__)#类的父类的类型
print(Dog.__base__)#倒过来最近的父类的类型
print(Dog.__mro__)#输出类的层次(从obj类开始向下继承的结构)
print(Dog.__subclasses__())#找到它的子类

#特殊的方法(因为万物皆是对象,因此基本数据类型也可以用)
a  = 20;
b = 17;
print(a.__add__(b))
c = [1,2,3,12]
print(c.__len__())#长度,和len()函数不一样
#方法前面传入的对象其实就是一个检测过程

#变量的赋值操作
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)
disk1 = Disk()
computer = Computer(cpu1,disk1)#其实内存中指向的形式和Java中一样,主要是多了一个类对象
import copy
computer1 = copy.copy(computer)#这就是浅拷贝,内部属性指针指向的都是同一个对象
computer2 = copy.deepcopy(computer)#这就是深拷贝,太方便了