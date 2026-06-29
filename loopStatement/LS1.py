#python中的循环语句有for和while，常用的循环控制关键词与方法如下所示
#for()迭代循环，用于遍历序列或可迭代对象
#while条件循环，条件为True时持续执行
#break用于立即终止当前循环
#continue用于跳过本次循环剩余代码，进入下一次迭代
#else循环正常结束时执行
#pass经典占位符
#range()用于生成整数序列，常与for循环配合使用
#enumerate()遍历，并同时获取索引和值

#while是python中的条件循环语句，只要条件为True，就会持续执行循环体
#与for不同的是，while通常适用于不确定循环次数，需要根据条件退出的场景
#格式类似于:    while 条件:
#                   语句        #循环体部分必须缩进
#               else:    
#                   语句        #else为可选部分，当循环正常结束(条件变为False时)执行
#基础用法1
count=0
while count<5:
    print(count)
    count+=1
print("循环结束")
#基础用法2-用户输入验证
secret=42;guess=0
while guess!=secret:                        #while循环常用于需要重复直到满足条件的场景
    guess=int(input("请输入数字:"))
    if guess<secret:
        print("太小了")
    elif guess>secret:
        print("太大了")
print("恭喜,猜对了!")
#基础用法3-计算阶乘
#计算阶乘
n=5;result=1
while n>0:
    result*=n
    n-=1
print(f"5!={result}")
#累加求和
total=0;i=1
while i<=100:
    total+=i
    i+=1
print(f"1+2+...+100={total}")
#基础用法4-while-else结构
count=0
while count<3:
    print(count)
    count+=1
else:
    print("循环正常结束")
print("---")
#while-else在break时else不执行
count=0
while count<5:
    if count==3:
        break
    print(count)
    count+=1
else:
    print("这行不会打印")
#基础用法5-无限循环与退出
#无限循环需要小心使用，下例使用break退出循环
#模拟菜单系统
while True:
    print("\n===菜单===")
    print("1.查看余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    choice=input("请选择:")
    if choice=="1":
        print("余额:1000元")
    elif choice=="2":
        print("存款功能")
    elif choice=="3":
        print("取款功能")
    elif choice=="4":
        print("感谢使用")
        break               #退出循环
    else:
        print("无效选择")
print("程序结束")
