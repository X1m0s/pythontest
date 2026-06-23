#python支持多种运算符:
#算术运算符、比较运算符、赋值运算符、逻辑运算符、位运算符、成员运算符、身份运算符及运算符优先级
#-----1.算术运算符-----
a=21;b=10;c=0
c=a+b;print("a+b=",c)
c=a-b;print("a-b=",c)
c=a*b;print("a*b=",c)
c=a/b;print("a/b=",c)
c=a%b;print("a%b=",c)
#修改变量a、b、c
a=2;b=3;c=a**b
print("a**b=",c)
a=10;b=5;c=a//b
print("a//b=",c)
#-----2.比较运算符-----
a=21;b=10;c=0
if(a==b):
    print("a==b")
elif(a!=b):
    print("a!=b")
if(a>b):
    print("a>b")
elif(a<b):
    print(a<b)
#修改变量a、b、c
a=5;b=20
if(a>=b):
    print("a>=b")
else:
    print("a<b")
if(a<=b):
    print("a<=b")
else:
    print("a>b")
#-----3.赋值运算符-----
a=21;b=10;c=0
c=a+b;print("c=",c)
c+=a;print ("c=",c)
c*=a;print ("c=",c)
c/=a;print ("c=",c)

c=2
c%=a;print ("c=",c)
c**=a;print ("c=",c)
c//=a;print ("c=",c)
#python3.8中新引入了海象运算符(Walrus Operator)，符号为:=，主要用在表达式中同时进行赋值和返回赋值的值
#可用于简化循环条件和表达式中的重复计算
#传统写法如下
n=10
if n>5:
    print(n)
#使用海象运算符
if(n:=10)>5:            #海象运算符在表达式中进行赋值操作，将变量n赋值为10，同时返回赋值结果
    print(n)
#海象运算符会降低代码可读性，在使用时必须用括号包裹，在f-string中也一样