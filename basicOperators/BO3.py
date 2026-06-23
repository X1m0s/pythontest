#-----7.身份运算符-----
a=b=20
if(a is b):
    print("a和b有相同标识")
else:
    print("a和b没有相同标识")
if(id(a)==id(b)):      #id函数用于返回对象内存地址
    print("a和b有相同标识")
else:
    print("a和b没有相同标识")

b=30
if(a is b):            #is判断两个标识符是否引用自一个对象，如果是同一个返回True，否则返回False
    print("a和b有相同标识")
else:
    print("a和b没有相同标识")
if(a is not b):        #is not判断是否引自不同对象，不同返回True，相同返回False
    print("a和b没有相同标识")
else:
    print("a和b有相同标识")
#is用于判断两个变量引用对象是否相同，==判断引用变量的值是否相等
a=[1,2,3];b=a
print(b is a,b==a)
b=a[:]
print(b is a,b==a)
#由于python缓存机制，小整数和短字符串会被缓存，导致is指向同一对象，因此is仅在x is None的判断背景下最稳定
#-----8.运算符优先级-----
#优先级表格见BO-EX1.md文件，本处不做赘述
#乘方 > 乘除 > 加减 > 移位 > 按位(与>异或>或) > 比较 > not > and > or
#口诀四句：算术先于比较，比较先于逻辑，not高于and，and高于or。记不住时加括号。
a,b,c,d,e=20,10,15,5,0
e=(a+b)*c/d
print("(a+b)*c/d=",e)
e=((a+b)*c)/d
print("((a+b)*c)/d=",e)
e=(a+b)*(c/d)
print("(a+b)*(c/d)=",e)
e=a+(b*c)/d
print("a+(b*c)/d=",e)

#and优先级更高
print("x=",x:=True," y=",y:=False," z=",z:=False,"\n计算x or y and z",sep="")
print("1.默认优先级(先算and)")
if x or y and z:        #等同于x or (y and z)
    print("yes")        #会输出
else:
    print("no")
print("2.强制改变优先级(先算or)")
if (x or y) and z:      
    print("yes")        #不会输出
else:
    print("no")         #会输出         