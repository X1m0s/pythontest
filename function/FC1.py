#函数代码块以def关键词开头，后接函数标识符名称和圆括号()
#所有传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义函数
#函数第一行语句可使用文档字符串-用于存放函数说明(相关笔记在CM1.py文件中)
#函数内容以冒号:起始，并且缩进；return[表达式]结束函数，选择性返回值，不带表达式的return等于返回None

def hello():
    print ("Hello World")
hello()

def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(a=4,b=5))

def area(width,height):
    return width*height
def print_welcome(name):
    print("Welcome",name)
print_welcome("Runoob")
print(f"width={4},height={5},area={area(4,5)}")

#函数调用
def printme(str):
    print(str)
    return
printme("我要调用用户自定义函数")
printme("我要再次调用同一个函数")

#参数传递
#python中类型属于对象，对象有不同类型的区分，变量是没有类型的
#a=[1,2,3]  a="runoob"      [1,2,3]是List类型，"runoob"是String类型，但变量a本身没有类型，仅为对象的引用(指针)

#可更改(mutable)与不可更改对象(immutable)
#python中strings,tuples,numbers是不可更改对象，list,dict等则是可以修改的对象
#不可变类型:变量赋值a=5后再赋值a=10，实际是新生成一个int值对象10，再让a指向它，丢弃5
#可变类型:变量赋值la=[1,2,3,4]后再赋值la[2]=5，则是将list la的第三个元素值更改，la不动

#python函数的参数传递:
#不可变类型:类似C++的值传递，如整数、字符串、元组。如fun(a)，传递的只是a的值，没有影响a对象本身。如果fun(a)内部修改a的值会新生成对象
#可变类型:类似C++的引用传递，如列表、字典。如fun(a)，则是将la真正的传过去，修改后fun外部的la也会受影响
#python中一切都是对象，严格来讲需要称为传不可变对象和传可变对象

#传不可变对象实例——通过id()函数来查看内存地址变化
def change(a):
    print(id(a))
    a=10
    print(id(a))
a=1
print(id(a))
change(a)

#传可变对象实例
def changeme(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值:",mylist,id(mylist))
    return
mylist=[10,20,30]
changeme(mylist)
print("函数外取值:",mylist,id(mylist))