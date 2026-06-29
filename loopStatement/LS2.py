#for是python中最常用的循环语句，可用于遍历可迭代对象(序列、字典、集合等)
#python的for循环比C系语言的for循环更简洁强大，无序手动管理循环变量，直接遍历元素
#基础格式为:    for 变量 in 可迭代对象:
#                   代码块                  #循环体必须缩进
#其中变量为每次循环从可迭代对象中取出的元素，可迭代对象包含列表/元组/字符串/字典/集合/range等
#基础用法1-遍历列表
fruits=["苹果","香蕉","橙子"]
for fruit in fruits:
    print(fruit)
print(fruit)
#附带索引的遍历
for i,fruit in enumerate(fruits):           #enumerate()同时提供索引和值
    print(f"{i}:{fruit}")
#基础用法2-遍历字符串和元组
#遍历字符串
for char in "Python":
    print(char,end=" ")
print()                                     #用于换行
#遍历元组
point=(10,20,30)
for value in point:
    print(value,end=" ")
print()
#基础用法3-遍历字典
#可通过使用字典的内置方法来遍历不同部分内容
person={"name":"tom","age":20,"city":"Beijing"}
for key in person:                          #遍历字典时默认遍历键
    print(key)
print("---")
for key,value in person.items():            #用于遍历键值对
    print(f"{key}:{value}")                 
print("---")
for value in person.values():               #用于仅遍历值
    print(value)
#基础用法4-带else的for循环
for i in range(3):
    print(i)
else:
    print("循环正常结束")
print("---")
#break时else不执行
for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("这行不会打印")
print("---")
#基础用法5-嵌套循环
#打印九九乘法表
for x in range(1,10):           
    for y in range(1,x+1):                  #python中针对区间的设计统一为左闭右开
        print(f"{y}*{x}={x*y}",end="\t")
    print()        