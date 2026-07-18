#元组由若干逗号分隔的值组成，如下所示
t=12345,54321,'Hello!';print(t[0],t)
u=t,(1,2,3,4,5);print(u)
#元组在输出时总是有括号的，以便正确表达嵌套结构，在输入时可能有或没有括号，但括号通常是必须的(如果元组是更大的表达式的一部分)

#集合是一个无序不重复元素的集，基本功能包括关系测试和消除重复元素
basket={'apple','orange','apple','pear','orange','banana'}
print(basket)
print('orange' in basket,'crabgrass' in basket)
#以下演示了两个集合的操作
a=set('abracadabra')
b=set('alacazam')
print("a=",a,"b=",b);print(a-b);print(a|b);print(a&b);print(a^b)
#集合也支持推导式的使用
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)

#另一个非常有用的python内建数据类型为字典，序列以连续整数为索引，字典则是以关键字作为索引，关键字可以是任意不可变类型，通常用字符串或数值
#下面是一个字典运用的简单例子
tel={'jack':4098,'sape':4139};tel['guido']=4127
print(tel)
del tel['sape'];tel['irv']=4127
print(tel)
print(list(tel.keys()));print(sorted(tel.keys()))
print('guido' in tel);print('jack' not in tel)
#构造函数dict()直接从键值对元组列表中构建字典，如果有固定模式，列表推导式指定特定的键值对:
print(dict([('sape',4139),('guido',4127),('jack',4098)]))
#此外字典推到可以用来创建任意键和值的表达式词典
print({x:x**2 for x in (2,4,6)})
#如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
print(dict(sape=4139,guido=4127,jack=4098))

#下面是一些遍历技巧的介绍
#1.在字典中遍历时，关键字和对应的值可以使用items()方法同时解读出来:
knights={'gallahad':'the pure','robin':'the brave'}
for k,v in knights.items():
    print(k,v)
#2.在序列中遍历时，索引位置和对应值可以使用enumerate()函数同时得到:
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)
#3.同时遍历两个或更多的序列，可以使用zip()组合:
questions=['name','quest','favorite color']
answers=['lancelot','the holy grail','blue']
for q,a in zip(questions,answers):                      #zip函数让两个列表逐对咬合，返回一个迭代器，每次next()吐出一对元素打包成的元组
    print('What is your {0}? It is {1}.'.format(q,a))   #.format函数实现字符串格式化,{0}和{1}作为占位符，数字对应括号内的参数位置
#4.如果需要倒序遍历一个序列，首先指定整个序列，然后调用reversed()函数
for i in reversed(range(1,10,2)):
    print(i)
#5.如果需要按顺序遍历一个序列，使用sorted()函数返回一个已排序的序列，并不修改原值
basket=['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
    print(f)
    