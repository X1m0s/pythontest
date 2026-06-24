#python字符串运算符
a="Hello";b="python"
print("a+b=",a+b)
print("a*2",a*2)
print("a[1]",a[1])
print("a[1:4]",a[1:4])
if("H" in a):
    print("H在变量a中")
else:
    print("H不在变量a中")

if("M" not in a):
    print("M不在变量a中")
else:
    print("M在变量a中")
print(r'\n')
print(R'\n')

#Python字符串格式化，语法类似于C中sprintf函数，例：
print("我叫%s今年%d岁!"%("小明",10))
#格式化相关内容存放至文件BS-EX1.py中

#python三引号允许一个字符串跨多行，该字符串内可包含换行符、制表符及其他特殊字符
#也就是说三引号内不用处理转义，代码里怎么排版字符串就长什么样子
para_str="""这是一个多行字符串
多行字符串可以使用制表符
Tab( \t )
也可以使用换行符\n就像这样
"""
print(para_str)
#f-string(f字符串)是python3.6后添加的，正式名称为字面量格式化字符串，在之前的格式化字符串中通常使用%
name="Runoob"
print("Hello %s"%name)
#但f-string格式化字符串以f开头，后面跟着字符串，字符串内表达式用{}包裹，会将变量或表达式计算值替换进去
name="Runoob"
print(f"Hello {name},{1+2+3}")
w={'name':'Runoob','url':'www.runoob.com'}
print(f"{w["name"]}:{w["url"]}")
#在python3.8及以上版本中，可以使用=符号拼接运算表达式与结果
x=1
print(f"{x+1}")             #2
print(f"{x+1=}")            #x+1=2

#python2中，普通字符串以8位ASCII码进行存储，Unicode字符串存储为16为Unicode字符串，使用语法是加上前缀u
#但python3中，所有字符串均为Unicode字符串