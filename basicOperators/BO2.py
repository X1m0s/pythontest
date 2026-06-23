#-----4.位运算符-----
#按位运算符是把数字看作二进制进行计算，在进入计算时自动转换为二进制数字，无需提前转换
a=60
b=13
print(bin(a),bin(b))      #a和b的二进制
print("a&b=",a&b)         #按位与运算符，如果相应位都为1，结果为1否则为0，结果12:00001100
print("a|b=",a|b)         #按位或运算符，只要相应位有1，结果位就为1，结果61:00111101
print("a^b=",a^b)         #按位异或运算符，对应位相异时，结果为1，结果49:00110001
print("~a=",~a)           #按位取反运算符，对数据的每个二进制位取反，把1变为0，类似于-x-1，结果-61:11000011
print("a<<2=",a<<2)       #左移运算符，所有二进制位向左移动x位，高位丢弃低位补0，结果240:11110000
print("a>>2=",a>>2)       #右移运算符，所有二进制位向右移动x位，低位丢弃高位补0，结果15:00001111
#-----5.逻辑运算符-----
a=10;b=20
if(a and b):
    print("a and b=",a and b)
else:
    print("a and b=",not(a and b))
if(a or b):
    print("a or b=",a or b)
else:
    print("a or b=",not(a or b))
#修改变量a的值
a=0
if(a and b):                            #and 布尔"与"，如果x为False，返回x的值，否则返回y的值
    print("a and b=",a and b)   
else:
    print("a and b=",a and b)
if(a or b):
    print("a or b=",a or b)             #or 布尔"或"，如果x为True，返回x的值，否则返回y的值
else:
    print("a or b=",a or b)
if not(a and b):
    print("not(a and b)=",not(a and b)) #not 布尔"非"，如果x为True，返回False，只返回True/False
else:
    print("not(a and b)=",not(not(a and b)))
#Python 的设计带来了一个常用技巧——短路赋值：
#name = user_input or "默认名称"    #输入为空时用默认值
#result = obj and obj.method()      #obj 非空才调用方法
#-----6.成员运算符-----
a=10;b=20
list=[1,2,3,4,5]
if(a in list):                      #in 在指定序列中找到值返回True，否则返回False
    print("a在给定的列表中")
else:
    print("a不在给定列表中")
if(b not in list):                  #not in 在指定序列中没有找到值返回True，否则返回False
    print("b不在给定列表中")
else:
    print("b在给定列表中")
a=2
if(a in list):
    print("a在给定的列表中")
else:
    print("a不在给定列表中")