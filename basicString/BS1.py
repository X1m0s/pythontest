#python中，在需要使用特殊字符时，python使用反斜杠\转义字符，下面是一些示例
print("nihao\
      beijing")         #行尾的\用作续航符
print("\\")             #\\表示单个反斜杠\
print('\'','\"')        #\'表示单引号,\"表示双引号
print("\a")             #\a表示响铃
print("Hello \bWorld")  #\b表示退格(backspace)
print("\000")           #\000表示空
print("Hello\nWorld")   #\n表示换行
print("Hello \vWorld")   #\v表示纵向制表符
print("Hello \tWorld")   #\t表示横向制表符
#\r表示回车，将\r后面内容移至字符串开头，逐一替换为开头部分的字符，直到完全替换完成
print("Hello\rWorld!")
print("google runoob taobao\r123456")
print("Goodmorning\rVietnam")
print("Hello \fWorld!")  #\f表示换页
#\yyy表示八进制数，y代表0-7的字符，每个数字对应ASCII码表中的一个字符
print("\110\145\154\154\157\40\127\157\162\154\144\41")
#\xyy表示十六进制数，以\x开头，y代表0-9，A-F的字符
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")

#重点:一个百分比进度的实现示例
import time
for i in range(101):
    bar="["+"="*(i//2)+" "*(50-i//2)+"]"
    print(f"\r{bar}{i:3}%",end='',flush=True)
    time.sleep(0.05)
print()

#教程中其他的展示案例
print('\'Hello, world!\'')  # 输出：'Hello, world!'

print("Hello, world!\nHow are you?")  # 输出：Hello, world!
                                        #       How are you?

print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?

print("Hello,\b world!")  # 输出：Hello world!

print("Hello,\f world!")  # 输出：
                           # Hello,
                           #  world!

print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65

print("\x41 为 A 的 ASCII 代码")  # 输出：A 为 A 的 ASCII 代码

decimal_number = 42
binary_number = bin(decimal_number)  # 十进制转换为二进制
print('转换为二进制:', binary_number)  # 转换为二进制: 0b101010

octal_number = oct(decimal_number)  # 十进制转换为八进制
print('转换为八进制:', octal_number)  # 转换为八进制: 0o52

hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
print('转换为十六进制:', hexadecimal_number) # 转换为十六进制: 0x2a