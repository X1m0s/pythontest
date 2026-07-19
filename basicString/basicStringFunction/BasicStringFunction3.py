#-----10.isdecimal()&isnumeric()&isspace()&istitle()-----
#isdecimal()用于检测字符串是否仅包含十进制字符
str1="0x2016"
str2="23443434"
print("str1.isdecimal()=",str1.isdecimal(),"str2.isdecimal()=",str2.isdecimal())
#isnumeric()用于检测字符串是否仅有数字组成(可以为unicode数字，全角数字，罗马数字，汉字数字)
#指数类似于²和分数类似于½也属于数字
print("'²'.isnumeric()=",'²'.isnumeric(),"'½'.isnumeric()=",'½'.isnumeric())
print("'1234'.isnumeric()=",'1234'.isnumeric(),"'一二三四'.isnumeric()=",'一二三四'.isnumeric())
print("'\u0030'.isnumeric()=",'\u0030'.isnumeric(),"'１２３４'.isnumeric()=",'１２３４'.isnumeric())
#isspace()用于检测字符串是否仅包含空格\空白字符
str1="          "
str2="\n\t\r\v\f"
print("str1.isspace()=",str1.isspace(),"str2.isspace()=",str2.isspace())
#istitle()用于检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写
#函数仅检查单词部分，非字母字符自动划分单词
#字符分为cased(大小写字母)和uncased(数字、标点、空格、行首等)
#函数的判定中，要求大写字母前一个字符必须为uncased，小写字母前一个字符必须为cased
str1="This Is String Example...Wow!!!"
str2="this is sthing example...wow!!!"
str3="Th2is I1s 123String Exam5ple...Wow!!!"
str4="This Is String 123Example...Wow"
print(str1.istitle(),str2.istitle(),str3.istitle(),str4.istitle())
#-----11.join()-----
#join()函数用于将序列中元素以指定的字符链接，生成一个新的字符串
#使用方式为"分隔符".join(可迭代对象)
print(",".join(["a","b","c"]),"".join(["a","b","c"]))
print(",".join("abc"),"/".join(["usr","bin"]))
#print(",".join([1,2,3]))   数字不可迭代，报错，需要使用生成器将列表内元素转换为str
#-----12.len()-----
#len()函数用于将具有长度信息的数据类型的长度或元素个数返回，此外参数也支持其他可迭代对象
#len()函数为内置函数，不是字符串类方法，因为通常用于字符串操作因此放在本处
#返回值为参数的长度，为整形数据
text="Hello,World!"
print(f"text:{text}的长度为{len(text)}")
test_list=[1,2,3,4,5]
print(f"test_list:{test_list}的长度为{len(test_list)}")
test_tuple=(10,20,30)
print(f"test_tuple:{test_tuple}的长度为{len(test_tuple)}")
test_set={10,20,30,40,50}
print(f"test_set:{test_set}的长度为{len(test_set)}")
test_dict={"apple":3,"banana":2,"cherry":4}
print(f"test_dict:{test_dict}的长度为{len(test_dict)}")
#对于字符串，返回字符个数；对于字典，返回键值对个数；对于其他可迭代对象返回元素个数
#-----13.ljust()&rjust()-----
#ljust()函数返回一个原字符串左对齐，使用空格填充至指定长度的新字符串，如果指定长度小于原长返回原字符串
#str.ljust(width,fillchar),width为新字符串指定长度，fillchar为填充字符，默认为空格
#rjust()函数与ljust()函数没有过多区别，唯一不同点是rjust()函数返回的字符串向右对齐
str1="Runoob example....wow!!!"
print(str1.ljust(50,"*"),str1.rjust(50,"*"))
#-----14.lower()&upper()&swapcase()-----
print("Runoob EXAMPLE....WOW!!!".lower())       #只是个把大写字母全部转成小写字母的函数
print("runoob example....wow!!!".upper())       #相反，把小写全转大写
print("RUNOOB example....WOW!!!".swapcase())    #把大写字母转成小写字母，小写字母转成大写字母       
#-----15.lstrip()&rstrip()&strip()-----
#lstrip()用于截掉字符串左边的字符，rstrip()相反，strip()则是两侧
#strip(chars)chars为要移除的字符集合(字符串形式),参数为空时默认移除空白字符(空格、\t、\n、\r、\v、\f)
#返回值为新字符串，不会修改原字符串
text="      Hello,World!"
result=text.lstrip()
print(result)
#移除左侧指定字符
text="www.example.com"
result=text.lstrip("wcmo.")
print(result)
#字符集合顺序无关
text="123abc"
result=text.lstrip("321")
print(result)
#遇到不在集合中的字符即停止
text="123abc"
result=text.lstrip("12")
print(result)
#原字符串不变
text="      Hello"
result=text.lstrip()
print(text)
print(result)
#如果想要提取网站中的二级域名，最好不要使用strip()函数，可以使用.removeprefix()/.removesuffix()
#自3.9版本添加
# ── removeprefix(prefix) ──
url = "www.example.com"

url.removeprefix("www.")        # 'example.com'    匹配则删除
url.removeprefix("http://")     # 'www.example.com' 不匹配原样返回
url.removeprefix("WWW.")        # 'www.example.com' 区分大小写
"".removeprefix("abc")          # ''                空字符串安全

# ── removesuffix(suffix) ──
url.removesuffix(".com")        # 'www.example'     匹配则删除
url.removesuffix(".com/")       # 'www.example.com' 不匹配原样返回
url.removesuffix(".COM")        # 'www.example.com' 区分大小写
"".removesuffix(".com")         # ''                空字符串安全