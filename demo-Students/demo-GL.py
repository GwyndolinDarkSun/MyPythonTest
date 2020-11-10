"""
首先声明这个业务流程全部都是重新写入(除了insert)
首先分析本项目,具有三大模块:修改信息,查询信息,排序
在分析流程 用户---->主界面---->功能菜单---->选择功能---->是否选择(继续选择则返回功能菜单,若不继续则结束)
"""
import os.path
#需要一个保存的文件
filename = "students.txt"
#首先需要表现系统的主界面(因为是要不断地询问,直到为否.因此需要一个while循环)
def menum():#这里可以直接卸载while循环中,可是这样代码的可读性太差了,显得十分冗杂,且已造成复写
    print("========================学生信息管理系统========================")
    print("---------------------------功能菜单----------------------------")
    print("\t\t1.录入学生信息(INSERT)")
    print("\t\t2.查找学生信息(SELECT)")
    print("\t\t3.删除学生信息(DELETE)")
    print("\t\t4.修改学生信息(UPDATE)")
    print("\t\t5.排序学生信息(ORDER)")
    print("\t\t6.统计总人数(COUNT)")
    print("\t\t7.显示所有学生信息(SHOW)")
    print("\t\t0.退出系统(EXIT)")
    print("-------------------------------------------------------------")
    print("                                                             ")
#你的判断要if???太low了!当然是枚举啦(当然要用一个列表来排除小数也行)(这里是用一个字典来表示一个学生的信息)
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

#这是主程序
def main():
    while(True):
        menum()
        z = input("请输入您要选择的功能:")#因为可能直接是0而结束程序,因此这个input()只能写在外面了
        if(z == xz.EXIT.name):#名字尽量不一样
            answer = input("您确定要选择退出程序吗(确定/取消):")
            if(answer == "确定"):
                print("程序结束!感谢您的下次使用")
                break
            elif(answer == "取消"):
                continue
            else:
                print("您的选则不存在")
                continue
        elif(z == xz.INSERT.name):
            insert()
        elif(z == xz.SELECT.name):
            select()
        elif(z == xz.DELETE.name):
            delete()
        elif(z == xz.UPDATE.name):
            update()
        elif(z == xz.ORDER.name):
            order()
        elif(z == xz.COUNT.name):
            count()
        elif(z == xz.SHOW.name):
            show()
        else:
            print("您输入的选择不存在!请重新输入!")
            print("---------------------------")

#接下来时各个方法
def insert():#和其他有些不同
    student_list = []
    while(True):
        try:
            id = int(input("请输入id:"))
            name = input("请输入名字:")
            English = int(input("请输入英语成绩:"))
            python = int(input("请输入python成绩:"))
            java = int(input("请输入java成绩:"))
        except:
            print("输入无效,请重新输入")
            continue
        #信息放入字典中
        student = {"id" : id,"name" : name,"English" : English,"python" :python,"java" : java}
        #再将信息加入列表中
        student_list.append(student)
        answer = input("是否继续添加?是/否")
        if answer == "是":
            continue
        else:
            break
    #全部都准备好
    #这里保存列表的内容到文件
    save(student_list)
    print("信息录入完毕!")

def save(lst):
    try:#打开文件,指明是添加还是写
        stu_txt = open(filename,"a",encoding="UFT-8")
    except:
        stu_txt = open(filename,"w",encoding="UTF-8")
    for item in lst:#保存进去的是一个个字典
        stu_txt.write(str(item)+"\n")#一个个的写
    stu_txt.close()

def select():#因为是查找,因此必定不会修改数据,因此只需要读而不需要写
    student_query=[]
    while True:
        id = ""
        name = ""
        if os.path.exists(filename):
            mode = input("请选择查找方式(id/姓名)")
            if(mode == "id"):
                try:
                    id = int(input("请输入查询学生的id:"))
                except:
                    print("您输入的id无效")
            elif(mode == "姓名"):#这里input()函数+if语句不一定就非要try,如果判断条件是字符串,则可以不try
                name = input("请输入姓名")
            else:
                print("您选择的模式无效,请重新输入!")
                continue
            with open(filename,"r",encoding="UTF-8") as rfile:
                student=rfile.readlines()
                for item in student:#接住然后遍历
                    d = dict(eval(item))
                    if(id != ""):#二者返回的都是一个整体(因此代码格式相仿)
                        if d["id"] == id:
                            student_query.append(d)
                    elif(name != ""):
                        if d["name"] == name:
                            student_query.append(d)
            #显示查询结果(原本那样太难看了,因此需要格式化字符串)
            show_student(student_query)
            #清空列表
            student_query.clear()
            answer = input("是否继续查询?是/否")
            if (answer == "是"):
                continue
            else:
                break


        else:
            print("暂未保存学员")
            return

def show_student(lst):#这里不能像对象一样调用属性来格式化(方便)因此只能估算长度了!
    #这里要使用格式化字符串
    if(len(lst) == 0):
        print("没有查询到学生信息")
        return
    #定义标题显示格式
    format_title="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    print(format_title.format("id","姓名","英语成绩","python成绩","java成绩","总成绩"))
    #内容显示格式
    format_data="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    for item in lst:#这里是字典,因此使用get()方法
        print(format_data.format(item.get("id"),item.get("name"),item.get("English"),item.get("python"),item.get("java"),int(item.get("English"))+int(item.get("python"))+int(item.get("java"))))

def delete():#这种删除方式是全覆盖,将所有的信息拷贝唯独不拷贝删除信息,最后用这个信息把原信息覆盖了
    while True:
        try:
            id = int(input("请输入删除学生的id:"))
        except:
            print("您输入的id无效")

        if os.path.exists(filename):#这里得先判断一下文件是否存在(因为引用的是变量,因此一定不要加双引号)
            with open(filename,"r",encoding="UTF-8") as file:
                student_old = file.readlines()
        else:
            student_old = []

        flag = False #标记是否删除(这样就保证了内层的判断会影响外层,一个类似指针的作用)
        if student_old:
            with open(filename,"w",encoding = "UTF-8") as wfile:#要读取就必须先打开哈
                d = {}
                for item in student_old:#一排一排的录入(顶级理解,不录入就等于删除)
                    d = dict(eval(item))#字符串转化为字典
                    if d["id"] != id:#判断id是否在文件中存在
                       wfile.write(str(d) + "\n")
                    else:
                        flag = True
                if(flag):
                    print(f"id={student_old}的学生信息已经删除")
                else:
                    print(f"没有找到id={student_old}的学生")
        else:
            print("没有学生信息")
            break
        show()
        answer = input("是否继续删除?是/否")
        if(answer == "是"):
            continue
        else:
            break

def update():#这个直接读取然后修改就行了(key改value)
    show()
    if os.path.exists(filename):
        with open(filename,"r",encoding="UTF-8") as rfile:
            student_old = rfile.readlines()
    else:
        return
    try:
        student_id = int(input("请输入要修改的学生的id:"))
    except:
        print("您输入的id无效")

    with open(filename,"w",encoding="UTF-8") as wfile:
        for item in student_old:#一个一个的修改
            d = dict(eval(item))
            if d["id"] == student_id:#从中间截断
                print("找到当前学生信息,可以修改了!")
                while True:
                    try:
                        d["name"] = input("请重新输入名字:")
                        d["English"]= int(input("请重新输入英语成绩:"))
                        d["python"]= int(input("请重新输入python成绩:"))
                        d["java"]= int(input("请重新输入java成绩:"))
                    except:
                        print("输入无效,请重新输入")
                        continue
                    wfile.write(str(d)+"\n")
                    print("修改成功")
                    break
                else:
                    wfile.write(str(d) + "\n")#如果不需要修改则正常写入就行了
            answer = input("是否继续修改?是/否")
            if (answer == "是"):
                update()#这里没有循环,因此需要递归(循环当然也行)
            else:
                break

def order():
    show()
    if os.path.exists(filename):
        with open(filename,"r",encoding="UTF-8") as rfile:
            student_list = rfile.readlines()
        student_new = []
        for item in student_list:#遍历的目的是转换格式(字符串和字典之间的转换)
            d = dict(eval(item))
            student_new.append(d)

    else:
        return
    asc_or_desc=input("请选择升序还是降序(asc/desc)")
    if asc_or_desc == "asc":
        asc_or_desc_bool = False
    elif asc_or_desc == "desc":
        asc_or_desc_bool = True
    else:
        print("您的输入有误,请重新输入")
        order()
    mode = input("请选择排序的方式(1.英语 2.python 3.java 4.总成绩)")
    if(mode == "1"):#函数式!!!!
        student_new.sort(key=lambda x : int(x["English"]),reverse=asc_or_desc_bool)#前者决定是谁后者决定升降
    elif(mode == "2"):
        student_new.sort(key=lambda x : int(x["python"]),reverse=asc_or_desc_bool)
    elif (mode == "3"):
        student_new.sort(key=lambda x : int(x["java"]),reverse=asc_or_desc_bool)
    elif (mode == "4"):
        student_new.sort(key=lambda x : int(x["English"] + int(x["python"]) + int(x["java"])),reverse=asc_or_desc_bool)
    else:
        print("您输入的方式有误,请重新输入!!!!!")
    show_student(student_new)

def count():
    if os.path.exists(filename):
        with open(filename,"r",encoding="UTF-8") as rfile:
            students = rfile.readlines()
            if(students):
                print(f"一共有{len(students)}名学生")
    else:
        print("暂未保存数据信息!!!!!!!!")

def show():#读取到信息一个一个添加到列表中,分别输出出来
    student_lst=[]
    if os.path.exists(filename):
        with open(filename,"r",encoding="UTF-8") as rfile:
            students = rfile.readlines()#读出来
            for item in students:
                student_lst.append(eval(item))#一行一行的放进我们的列表中(这样不用key去查询因此可以是列表)
            if student_lst:
                show_student(student_lst)
    else:
        print("暂未保存信息!!!!!!!!")

main()

#这里是学生类(可以用一个集合来装一个类,甚至可以用一个字典来装一个类(id来作为key))
#排序就调用属性,赋值就可以调用get()方法,因为是可变序列,就可以使用append()来追加(虽然这样十分的灵活但是同样的内存占用更大)
#因为是用了文件储存,因此就可以回收列表,可以直接释放内存(打印时也更加方便,因此过于追求灵活性有时候也是没必要的)
class Student:
    id = 0;
    name = None
    English = 0
    python = 0
    java = 0
    def get(self,id,name,English,python,java):
        self.id = id
        self.name = name
        self.English = English
        self.python = python
        self.java = java