#字符串用引号包围，使用\转移特殊字符，字符串截取语法格式->变量[头下标:尾下标]
#示例：
#从后索引: -6  -5  -4  -3  -2  -1
#从前索引:  0   1   2   3   4   5
#         | R | u | n | o | o | b |
#从前截取:    1   2   3   4   5   :
#从后截取:   -5  -4  -3  -2  -1   :
#加号+是字符串连接符，星号*表示复制当前字符串，数字表示复制次数
my_str="Runoob"
print(my_str)        #打印整个字符串
print(my_str[0:-1])  #打印索引0到倒数第二个字符(不含最后一个)
print(my_str[0])     #打印第一个字符:R
print(my_str[2:5])   #打印索引2、3、4的字符(不含索引5)
print(my_str[2:])    #打印从索引2开始到末尾:noob
print(my_str*2)      #重复打印两次
print(my_str+"TEST") #字符串拼接:RunoobTEST

#反斜杠(\)可以作为续行符，表示下一行是上一行的延续，也可以使用三引号跨越多行
#python的字符串不能被改变，向索引位置赋值会导致错误

#bool(布尔类型)，即True或False。bool是int的子类，因此可被看作整数使用，True等价于1，False等价于0
#布尔类型可与其他数据类型比较，如数字、字符串，比较时将True视为1，False视为0
#布尔类型可与逻辑运算符使用组合布尔表达式，也可以被转换为其他数据类型
#可使用bool()函数将其他类型值转换为布尔值，以下值转换时为False:None、False、各种零(0\0.0\0j)、
#空字符串、空列表、空元组、空序列(如''、()、[])和空映射(如{})。其他所有值转换为布尔值时均为True。

#布尔类型值与类型
a=True;b=False
print(type(a));print(type(b))
print(int(True));print(int(False))
#布尔函数转换
print(bool(0))
print(bool(42))
print(bool(''))
print(bool('python'))
print(bool([]))
print(bool([1,2,3]))
#布尔逻辑运算
print(True and False)
print(True or False)
print(not True)
#布尔比较运算
print(5>3)
print(2==2)
print(7<4)
#布尔值在控制流中应用
if True:
    print("this will always print")
if not False:
    print("this will also always print")
x=10
if x:
    print("x是非零值，在布尔上下文中为True")