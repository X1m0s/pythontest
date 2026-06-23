#python中数字数据类型用于存储数值，数据类型不允许改变，如果改变将会重新分配内存空间
#当为变量赋值时Number对象被创建，可以使用del删除一些数字对象的引用
#python在接收到其他进制数据时会自动转换进制，例如:
a=0xA0F;b=0o67;c=0b1001     #2575 55 9
print(a,b,c)
#浮点型数据支持使用科学计数法，复数数据可以用a+bj或complex(a,b)表示，实部a和虚部b均为浮点型
#此外，复数数据不支持直接转换为整型或浮点型，可以使用.real和.imag属性将实部和虚部分别提取出来
#数字类型的转换可以使用对应数据类型的构造函数(调用类名:int()\float()\complex())
print("a=",a:=7," b=",b:=2,sep="")
print("a/b=",a/b)               #作除法运算时，总是会返回一浮点数，如果需要得到整数可使用//
print("a//b=",a//b)     
print("浮点a//b=",float(a)//b)  #但//得到的不一定是整数类型，与分子和分母的数据类型有关
print("a//浮点b=",a//float(b))
print("浮点a//浮点b=",float(a)//float(b))
print("a=",a:=5," b=",b:=2,sep="")
print("a的b次方=",a**b,"a的b次方+1=",a**b+1,"a的(b+1)次方",a**(b+1))
#当不同类型数混合计算时会统一转换为更"宽"的类型：bool->int->float->complex
#仅在交互式命令行编程(REPL)中，最后被输出的表达式结果被赋值给变量_，通常该变量作为只读变量

#python的math模块中中也规定了两个数学常量，使用print默认输出时输出到小数点后15位
import math
print(math.pi,math.e)
