#-----7.find()&rfind()-----
#find()函数用于检测字符串中是否包含子字符串，如果包含返回索引值在字符串中的起始位，否则返回-1
#str.find(str,beg=0,end=len(string))
#str为指定检索的字符串，beg和end分别为检索的开始索引和结束索引
#开始索引默认值为0，结束索引默认值为字符串长度
#索引方式与字符串标准索引一致，支持负数索引
str1="Runoob example....wow!!!"
str2="exam"
print(str1.find(str2))
print(str1.find(str2,5))
print(str1.find(str2,10))
#rfind()则是将检索方式修改为从字符串右侧向左侧检索，即从字符串尾部开始,但返回值的索引仍为正向
str1="this is really a string example....wow!!!"
str2="is"
print(str1.rfind(str2))
print(str1.rfind(str2, 0, 10))
print(str1.find(str2))
print(str1.find(str2,0,10))
print(str1.find(str2,10,0))
#8-----index()&rindex()-----
#index()和rindex()函数同样用于检测字符串中是否包含子字符串，使用方式与find一致，但未检索到时报异常
#rindex()函数则是从右向左开始检测
str1="Runoob example....wow!!!"
str2="exam"
print(str1.index(str2))
print(str1.index(str2,5))
str1="this is really a string example....wow!!!"
str2="is"
print(str1.rindex(str2))
print(str1.rindex(str2, 0, 10))
print(str1.index(str2))
print(str1.index(str2,0,10))
#9-----isalnum()&isalpha()&isdigit()&islower()&isupper-----
#isalnum()用于检查字符串是否仅由字母或数字组成
#当至少有一个字符且所有字符都是字母或数字时返回True否则False，空字符串返回False，特殊字符也返回False
str1="runoob2016"
str2="www.runoob.com"
print("str1.isalnum()=",str1.isalnum(),"str2.isalnum()=",str2.isalnum())
#isalpha()用于检查字符串是否仅有字母或文字
str1="runoob"
str2="runoob菜鸟教程"
str3="Runoob example....wow!!!"
print("str1.isalpha()=",str1.isalpha(),"str2.isalpha()=",str2.isalpha(),"str3.alpha()=",str3.isalpha())
#isdigit()用于检查字符串是否仅包含数字(仅能检测正整数)
str1="123456"
str2="Runoob example....wow!!!"
print("str1.isdigit()=",str1.isdigit(),"str2.isdigit()=",str2.isdigit())
#尝试使用isdigit()检测浮点数和小数的示例
def is_number(s):
    try:                                    #如果能运行float，返回True(字符串s为浮点数)
        float(s)
        return True
    except ValueError:                      #ValueError为标准异常，表示传入无效参数
        pass                                #如果引发这种异常，不做任何事情
    try:
        import unicodedata                  #处理ASCII码的模块
        unicodedata.numeric(s)              #用于把表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError,ValueError):
        pass
        return False
print(is_number(1))
print(is_number(1.0))
print(is_number(0))
print(is_number(-2))
print(is_number(-2.0))
print(is_number("abcd"))
#islower()用于检测字符串是否由小写字母组成，仅当字符串中至少包含一个区分大小写的字符时有效
#如果所有字符均为小写，返回True，否则返回False，字符串可以包含数字或字符，不影响函数使用
#isupper()与islower()类似，但检测的内容为大写字母
str1="RUNOOB example";str2="RUNOOB EXAMPLE";str3="runoob example"
print("str1.islower()=",str1.islower(),"str2.islower()=",str2.islower(),
      "str3.islower()=",str3.islower())
print("str1.isupper()=",str1.isupper(),"str2.isupper()=",str2.isupper(),
      "str3.isupper()=",str3.isupper())