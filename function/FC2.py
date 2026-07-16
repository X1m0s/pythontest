#调用函数时可使用的正式参数类型包括:必需参数、关键字参数、默认参数、不定长参数

#必需参数需要按正确的顺序传入函数，调用时的数量必须和声明时的一样。
def printme(str):
    print(str)
    return
printme("HelloFunction")    #调用该函数时，不加参数会报错

#关键字参数与函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值
#使用关键字参数允许函数调用时参数的顺序与生命是不一致，因为python解释器可用参数名匹配参数值
def printme1(str):
    print(str)
    return
printme1(str="菜鸟教程")

def printinfo(name,age):
    print("名字:",name)
    print("年龄:",age)
    return
printinfo(age=24,name="Runoob")

#默认参数在调用函数且没有传递参数时使用，但如果函数有参数未设置默认参数留空，程序仍然无法运行
def printinfo1(name,age=20):
    print("名字:",name)
    print("年龄:",age)
    return
printinfo1(age=50,name="runoob")
print("-----------------------------")
printinfo1(name="test")

#不定长参数可用在需要函数能处理比声明时更多的参数的情况下，这些参数叫做不定长参数，声明时不会命名，基本语法如下
#def functionname([formal_args,]*var_args_tuple):
#   "函数_文档字符串"
#   function_suite
#   return [expression]
#加了型号*的参数以元组(tuple)的形式导入，存放所有未命名的变量参数
#如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量
def printinfo2(arg1,*vartuple):
    "打印任何传入的参数"
    print("输出:")
    print(arg1)
    print(vartuple)
printinfo2(10)
printinfo2(70,60,50)
#还有一种情况，参数名前带两个星号**，加了两个星号的参数会以字典的形式导入
def printinfo3(arg1,**vardict):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    print(vardict)
printinfo3(1,a=2,b=3,c=4)

#声明函数时，参数中星号*可以单独出现，如下所示
#def f(a,b,*,c):
#   return a+b+c
#如果需要单独出现星号*，那么星号*后的参数必须使用关键字传入

#星号单独出现在参数中通常用于以下情况
#作为分隔符，强制关键字传参，可用于防止调用时传参顺序错误、保证API设计的稳定性
# def draw_rect(*, width, height, color):
#     pass
# draw_rect(100, 200, "red")     #会被拦下
# draw_rect(width=100, height=200, color="red")  #意图清晰，不会搞混
# def connect(host, port, *, timeout=10, ssl=False):
#     pass

# connect("localhost", 8080, timeout=5)        #
# connect("localhost", 8080, ssl=True)         #
# connect("localhost", 8080, 5, True)          #被 * 挡住——你不确定 5 是 timeout 还是别的什么
# 前两个参数 host、port 意义明确可以位置传，后面的可选项强迫写关键字

#此外星号*也有一个反例，左斜杠/的效果与星号*相反，左斜杠/前的参数禁止使用关键字传参，左斜杠/后的参数无所谓


