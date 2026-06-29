#一些测试示例
#使用while计算1-100的总和
n=100;sum=0;counter=1
while counter<=n:
    sum+=counter
    counter+=1
print("1到%d之和为:%d"%(n,sum))
#打印字符串中的所有字符
print("-----------------------------------")
word="runoob"
for letter in word:
    print(letter)
#整数范围值可以配合range()函数使用
print("-----------------------------------")
for number in range(1,6):
    print(number)
#结合range()和len()函数遍历一个序列的索引
print("-----------------------------------")
a=["Google","Baidu","Runoob","Taobao","QQ"]
for i in range(len(a)):
    print(i,a[i])
#循环查询质数的示例
print("-----------------------------------")
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"等于",x,"*",n//x)
            break
    else:
        print(n,"是质数")
#斐波那契数列(Fibonacci Series)的简易示例
a=0;b=1
while b<=10:
    print(b,end=" ")
#   tmp=a;a=b;b+=tmp        #常规计算方式
    a,b=b,a+b               #python特有的元组解包，右侧先整体求值并打包成元组，再同时解包赋给左侧变量
else:
    print()
#使用for实现的版本
a=0;b=1
for x in range(10):
    print(b,end=" ")
    a,b=b,a+b
