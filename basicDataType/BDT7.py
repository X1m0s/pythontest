#bytes类型表示的是不可变的二进制序列(byte sequence)，与字符串类型不同，bytes类型中元素为整数值
#(范围在0-255之间)而非Unicode字符，该类型通常用于处理二进制数据，如图像文件、音频文件、视频文件
#创建bytes对象最常见的方式为使用b前缀
x=b"hello"
print(x)
print(type(x))
print(x[0])         #104，为"h"的ASCII值，bytes元素为整数
#同样可以使用bytes()函数将其他类型对象转换为bytes类型，第二个参数指定编码方式
x=bytes("hello",encoding="utf-8")
print(x)
print(x[-1])
#与字符串类型类似，该类型同样支持切片、拼接、查找、替换操作，由于bytes类型不变，修改操作需要创建新对象
x=b"hello"
y=x[1:3]            #切片操作，得到b"el"
z=x+b"world"        #拼接操作，得到b"helloworld"
print(y)            #b"el"
print(z)            #b"helloworld"
#因为bytes类型中元素为整数值，进行比较操作时需要使用相应整数值，使用ord()函数将字符转化为整数
if x[0]==ord("h"):
    print("第一个元素是'h'")
if x[-1]==ord("o"):
    print("最后一个元素是'o'")