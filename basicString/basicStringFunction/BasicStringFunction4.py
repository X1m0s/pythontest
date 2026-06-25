#-----16.maketrans()&translate()-----
#该函数用于创建字符映射的转换表，从python3.4开始str.maketrans()被移除,取而代之的是bytearray.maketrans()
#maketrans()返回的是dict数据类型的映射表，对字符串进行转换操作需要用translate()执行
#string.maketrans(x,y,z),x为字符串中要替代的字符组成的字符串,y为相应的映射字符的字符串,z为要删除的字符
#处理顺序为优先处理参数z,即删除对应字符,然后处理x->y的映射
txt="Runoob!"
my_table=txt.maketrans("R","N")
print(txt.translate(my_table))
#使用字符串设置替换字符，两个字符串的长度必须相同,要求能进行一一对应
intab="aeiou"
outtab="12345"
transtab=str.maketrans(intab,outtab)
str="this is string example....wow!!!"
print(str.translate(transtab))
#bytes和bytesarray模块下的translate()函数的参数及用法略有扩展，本处不做赘述,仅提供一个参考示例
bytes_tabtrans=bytes.maketrans(b"abcdefghijklmnopqrstuvwxyz",b"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(b"runoob".translate(bytes_tabtrans,b'o'))     #删除字母o后，将剩余字母小写转大写
#设置要删除的字符参数
txt="Google Runoob Taobao!"
x="mSa";y="eJo";z="odnght"
my_table=txt.maketrans(x,y,z)
print(txt.translate(my_table))
#-----17.max()&min()-----
#max()用于返回字符串中最大的字母，min()则返回最小的字母
#这两个函数均为python内置函数，无需调用str对象
#该函数在BasicMathFunction节提过，本节只介绍字符串比较时的情景
str1="runoob"
str2="RUNoob"
print("max(str1)=",max(str1),"min(str1)=",min(str1))
print("max(str2)=",max(str2),"min(str2)=",min(str2))
#本质是比较字符的ASCII码值，因此小写字母普遍大于大写字母，大小写相同的情况下则是a<z
#-----18.replace()-----
#该函数用于把字符串中的旧字符串替换成新字符串，在指定max参数时，替换max次
#replace(old,new,max)old为将被替换的子字符串，new为新字符串，max为最大替换次数
str="www.w3cschool.cc"
print("菜鸟教程旧地址:",str)
print("菜鸟教程新地址:",str.replace("w3cschool.cc","runoob.com"))
str="this is string example....wow!!!"
print(str.replace("is","was",1))
print(str.replace("is","was",2))
#-----19.split()-----
#该函数通过指定分隔符对字符串切片，将字符串分割成子字符串并返回一个由这些子字符串组成的列表
#split(str,num)str为分隔符，默认为所有的空白字符(空格\n\t等)，
#num为分割次数，最多分隔成num+1个子字符串，默认为-1，即分割所有
str="this is string example....wow!!!"
print(str.split())          #默认以空格为分隔符
print(str.split("i",1))     #以i为分隔符
print(str.split("w"))       #以w为分隔符
#另外一个示例如下
txt="Google#Runoob#Taobao#Facebook"
x=txt.split("#",1)          #num参数为1，仅分割为两个参数列表
print(x)
#-----20.splitlines()-----
#该函数按照行("\r","\r\n","\n")分割字符串,返回一个包含各行作为元素的列表
#splitline(keepends)，keepends默认为False，不保留换行符，如果为True则保留换行符
str="ab c\n\nde fg\rkl\r\n"
print("str.splitines()=",str.splitlines(),"str.splitlines(True)=",str.splitlines(True))
#-----21.startswith()-----
#该函数用于检查字符串中是否以指定子字符串开头，是返回True，否则False，在参数beg和end指定范围内检查
#startswith(str,beg,end)str为检测的字符串，beg为字符串检测起始位，默认为0，end为结束位，默认为字符串长度
str="this is string example....wow!!!"
print(str.startswith("this"))           #字符串是否以this开头
print(str.startswith("string",8))       #从第九个字符开始的字符串是否以string开头
print(str.startswith("this",2,4))       #从第二个字符开始到第四个字符结束的字符串是否以this开头
#-----22.title()-----
#返回一个"标题化"处理过的字符串，即将所有单词的首字母大写，其余字母小写
str="this is string example from runoob....wow!!!"
print("str.title()=",str.title())
#非字母后的第一个字母也会转化为大写字母
txt="hello b2b2b2 and 3g3g3g"
print("txt.title()=",txt.title())
#-----23.zfill()-----
#str.zfill(width)用于返回指定长度的字符串，原字符串右对齐，前面填充0
#width为指定字符串的长度
str="this is string example from runoob....wow!!!"
print("str.zfill:",str.zfill(40))
print("str.zfill:",str.zfill(50))