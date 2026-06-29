#python3的range()函数返回一个可迭代对象(类型为对象而不是列表类型)
#list()函数作为对象迭代器可以将返回的可迭代对象转为一个列表
#range(stop)/range(start,stop,step),start和stop为计数的开始和结束，step为步长，默认为1
for number in range(1,6):
    print(number,end=" ")
print()
for number in range(6):
    print(number,end=" ")
print()
for number in range(1,6,2):
    print(number,end=" ")
print()
#也可以使用负数步长，以从结束值开始倒序生成序列，但如果使用负数步长，开始值必须大于结束值
for number in range(6,1,-1):
    print(number,end=" ")
print()
#如果只需要生成一个整数序列，不需要遍历，可以将返回值转换为列表或元组
numbers=list(range(1,6))            #生成一个整数列表
print(numbers)              
numbers=tuple(range(1,6))           #生成一个整数元组
print(numbers)

#enumerate()函数用于在遍历可迭代对象同时获取索引和值，可避免使用额外计数器变量
#enumerate(iterable,start=0)iterable为可迭代对象，start为返回索引的起始值，返回一个对象(迭代器)
#每次迭代返回(index,value)元组
#基础用法1
fruits=["苹果","香蕉","橙子"]
for index,fruit in enumerate(fruits):
    print(f"{index}:{fruit}")
print("---")
for index,fruit in enumerate(fruits):
    print(fruit)
#基础用法2-指定起始索引
print()
fruits=["苹果","香蕉","橙子"]
for i,fruit in enumerate(fruits,start=1):       #从1开始计算索引
    print(f"{i}:{fruit}")
print("---")
for i,fruit in enumerate(fruits,start=10):      #从10开始计算索引
    print(f"{i}:{fruit}")
#基础用法3-转换为列表/字典
fruits=["苹果","香蕉","橙子"]
result=list(enumerate(fruits))
print(result)
#也可以转换为字典
result=dict(enumerate(fruits))
print(result)
#配合列表推导式时
squares=[x**2 for x in range(5)]
indexed_squares=[(i,v) for i,v in enumerate(squares)]
print(indexed_squares)
#基础用法4-实际应用
fruits=["苹果", "香蕉", "橙子", "香蕉", "苹果"]
target="香蕉"
for index,fruit in enumerate(fruits):
    if fruit==target:
        print(f"找到{target}在索引{index}")
        break
#配合条件查找所有匹配项
print("\n所有香蕉的位置:")
for index,fruit in enumerate(fruits):
    if fruit=="香蕉":
        print(index,end=" ")
#字符串中查找字符位置
text="hello"
for i,c in enumerate(text):
    print(f"{c}在位置{i}")
#基础用法5-与字典配合
person={"name":"Tom","age":20,"city":"Beijing"}
for index,(key,value) in enumerate(person.items()):
    print(f"{index}:{key}={value}")
items=["a","b","c"]
numbered={i+1:v for i,v in enumerate(items)}
print(numbered)
#因为字典的迭代特性，在使用时需要配合.items()方法