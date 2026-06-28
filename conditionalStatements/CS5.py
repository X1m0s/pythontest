#if语句中常用的操作运算符:</<=/>/>=/==/!=,基本都是比较运算符，下面是一个简单案例
#该案例演示一个数字猜谜游戏
number=7;guess=-1
print("数字猜谜游戏!")
while guess != number:
    guess=int(input("请输入你猜的数字:"))
    if guess==number:
        print("恭喜,你猜对了!")
    elif guess<number:
        print("猜的数字小了...")
    elif guess>number:
        print("猜的数字大了...")
#if嵌套操作语句，可以把if...elif...else结构放在另外一个if...elif...else结构中，示例如下
num=int(input("输入一些数字:"))
if num%2==0:
    if num%3==0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2,但不能整除3")
else:
    if num%3==0:
        print("你输入的数字可以整除3,但不能整除2")
    else:
        print("你输入的数字不能整除2和3")
