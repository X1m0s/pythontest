#-----16.maketrans()-----
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