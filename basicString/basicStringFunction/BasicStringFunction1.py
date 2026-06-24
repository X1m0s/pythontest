#-----1.capitalize()-----
#该函数将字符串的第一个字母大写，其他字母小写，没有参数，返回值为字符串
#仅在首字符为字母时将第一个字母大写，其余字符全部强制转为小写
test_str1="all Roads leAD TO mE"
test_str2="1st iS mInE"
test_str3="新年好啊"
print("str1=",test_str1.capitalize(),"str2=",test_str2.capitalize(),"str3=",test_str3.capitalize())
#-----2.center()-----
#该函数返回一个指定宽度居中的字符串，fillchar为填充的字符，默认为空格
#参数为str.center(width,fillchar)，当width小于字符串宽度时直接返回字符串，否则使用fillchar填充
str="[runoob]"
print("str.center(40,'*')=",str.center(40,'*'))
print("str.center(9,'*')=",str.center(9,'*'))       #奇数优先在左侧填充
#-----3.count()-----
#该函数用于统计字符串中某个字符出现次数，返回值为整型
#count(sub,start=0,end=len(string))，sub为搜索的子字符串，start为字符串开始搜索位置
#end为字符串结束搜索的位置，字符中第一个字符索引为0，默认为字符串中最后一个位置
str="www.runoob.com"
sub="o"
print("str.count('o')=",str.count(sub))
print("str.count('run',0,10)=",str.count("run",0,10))
#-----4.decode()&encode()-----
#bytes.decode()以指定编码格式解码bytes对象，返回值为解码后的字符串
#bytes.decode(encoding="utf-8",errors="strict")encoding为要使用的编码，默认utf-8
#error为设置不同错误的处理方案，默认为"strict"，意为编码错误引起UnicodeError
#encode()以指定编码格式编码字符串，返回值为编码处理后的bytes对象，参数设计与decode()类似
str="菜鸟教程"
str_utf8=str.encode("UTF-8")
str_gbk=str.encode("GBK")
print("str=",str,"\nUTF-8编码=",str_utf8,"\nGBK编码=",str_gbk)
print("UTF-8解码=",str_utf8.decode("UTF-8","strict"))
print("GBK解码=",str_gbk.decode("GBK","strict"))
#-----5.endswith()-----
#该函数用于判断字符串是否以指定后缀结尾，返回值为bool类型-True/False
#str.endswith(suffix,start,end)suffix为判断参数，可以是字符串或元素，start和end为开始和结束位置
str="Runoob example....wow!!!"
suffix="!!"
print(str.endswith(suffix))
print(str.endswith(suffix,20))
suffix="Run"
print(str.endswith(suffix))
print(str.endswith(suffix,0,19))
print(str.endswith(suffix,0,3))         #索引方式与字符串索引保持一致
#-----6.expandtabs()-----
#用于将字符串中的制表符\t转为空格,使下一个字符对齐到tab列边界，str.expandtabs(tabsize=8)
#默认每8位一个tab位（0、8、16...）,\t用空格填充到下一个边界
'''这里是tab运行原理介绍
使用\t以及expandtabs采用默认值时
列：0  1  2  3  4  5  6  7  8  9
    a  b  c \t  d                   \t位于列3，下一tab为列8，填充了5(8-3)个空格
    a  b  c  空 空 空 空 空 d 
使用expandtabs(tabsize=4)时
列：0  1  2  3  4  5  6  7  8  9
    a  b  c \t  d                   \t位于列3，下一tab为列4，填充了1(4-3)个空格
    a  b  c  空 d 
'''
#tabsize为将\t转为空格的字符数，当取值为8时，视觉效果与直接使用\t相同，但本质不同
#\t占用空间为一个字节，该函数所占空间为实际空格数，len()值上\t为5，该函数为17
#但适应性与可移植性上，\t依赖目标环境的tab设置，当终端修改tab宽度时自动适配，该函数完全不变
#以下是示例
str="runoob\t12345\tabc"
print("原始字符串:",str)
#默认8个空格，runoob6个字符，\t填充2空格，12345有5个字符，\t填充3空格
print("替换\\t符号:",str.expandtabs())
#2个空格，runoob6个字符，\t填充2空格，12345有5个字符，\t填充1空格
print("使用2个空格替换\\t符号:",str.expandtabs(2))
#3个空格，runoob6个字符，\t填充3空格，12345有5个字符，\t填充1空格
print("使用3个空格替换\\t符号:",str.expandtabs(3))
#4个空格，runoob6个字符，\t填充2空格，12345有5个字符，\t填充3空格
print("使用4个空格替换\\t符号:",str.expandtabs(4))
#5个空格，runoob6个字符，\t填充4空格，12345有5个字符，\t填充5空格
print("使用5个空格替换\\t符号:",str.expandtabs(5))
#6个空格，runoob6个字符，\t填充6空格，12345有5个字符，\t填充1空格
print("使用6个空格替换\\t符号:",str.expandtabs(6))

#AI整理的计算公式
#填充空格数=tabsize-(col%tabsize),col为制表符\t的等效已展开列号，具体见运行原理图中
