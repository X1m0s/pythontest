#Python使用lambda创建匿名函数
#匿名函数意为不再使用def语句这样标准的形式定义一个函数
#lambda只是一个表达式，而不是一个代码块，函数体比def简单很多，因此只能封装有限的逻辑
#lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数
#虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少开销，提高代码执行速度
#lambda函数语法如下所示
#lambda [arg1[,arg2,....argn]]:expression
#设置参数a加上10
x=lambda a:a+10
print(x(5))

sum=lambda arg1,arg2:arg1+arg2
print("相加后的值为:",sum(10,20))
print("相加后的值为:",sum(-10,-20))

#此外也可以将匿名函数封装在一个函数内，可通过同样代码创建多个匿名函数
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)

print(mydoubler(11))
print(mytripler(11))
#这里涉及到了函数的闭包，简单来说就是一个函数打包带走了它依赖的外部变量，让这些变量比创建它的函数生存时间更长
#普通函数执行完，内部的局部变量就销毁了。但匿名函数在诞生时引用了n，Python检测到这个依赖关系，就把n的值打包寄存在函数体内一起带出。
#哪怕myfunc早就结束退出了，匿名函数依然能摸到那个n

#return语句用于退出函数，选择性地向调用方返回一个表达式
def sum(arg1,arg2):
    total=arg1+arg2
    print("函数内:",total)
    return total
total=sum(10,20)
print("函数外:",total)

#强制位置参数
#python3.8中新增了一个函数形参语法/来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式
#如下所示，形参a和b必须使用指定位置参数，c或d可以是位置形参或关键字形参，而e和f要求为关键字形参
def f(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
f(10,20,30,d=40,e=50,f=60)            #该调用方式正确
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式