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
c=a+b
print("c=",c)
c+=a
print ("c=",c)
c*=a
print ("c=",c)
c/=a
print ("c=",c)

c=2
c%=a
print ("c=",c)
c**=a
print ("c=",c)
c//=a
print ("c=",c)