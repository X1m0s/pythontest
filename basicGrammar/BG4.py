#等待用户输入
input("按下enter键后退出。")
#python支持在同一行内使用多条语句，语句间用;分割
import sys;x="runoob";sys.stdout.write(x+"\n")   
#sys.stdout.write为精确控制输出的print，返回值为字符个数，只接受字符串输入，默认不换行

#多语句构成代码组
#缩进相同的一组语句构成一代码块，称为代码组，例如if、while、def、class等复合语句，首行以关键字
#开始，以:结束，该行后的代码构成代码组，成为子句（clause）

#print换行
#print默认输出换行，如果实现不换行需要在变量尾部加上end=""
#该参数默认值为"\n"，表示换行，可重赋值为空格或其他符号或者字符串          
x=3;y=9
print(x)  #输出：3
print(y)  #      9
print(x,y)       #输出：3 9
print(x);print(y)#输出：3
                 #      9

print(x,end="")
print(y)         #输出：39

print("this is a line",end="")
print("this is a line")         #输出：this is a linethis is a line

