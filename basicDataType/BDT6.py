#字典(dictionary)是一种映射类型，用{}标识，是键(key):值(value)的集合。键必须使用不可变类型且必须唯一
#字典的元素为键值对，此外python3.7起，字典保持元素插入顺序
my_dict={}
my_dict['one']="1-菜鸟教程"
my_dict[2]="2-菜鸟工具"

tinydict={"name":"runoob","code":1,"site":"www.runoob.com"}
print(my_dict["one"])               #输出键为"one"的值
print(my_dict[2])                   #输出键为2的值
print(tinydict)                     #输出完整的字典
print(tinydict.keys())              #输出所有键
print(tinydict.values())            #输出所有值

#构造函数dict()可直接从键值对序列(需为可迭代对象，如元组列表)(key1,value1),(key2,value2)...中构建字典:
test_dict1=dict([("Runoob",1),("Google",2),("Taobao",3)])
print(test_dict1)
#字典推导式
test_dict2={x:x**2 for x in (2,4,6)}
print(test_dict2)
#关键字参数构造
test_dict3=dict(Runoob=1,Google=2,Taobao=3)
print(test_dict3)

#此外字典类型也内置了一些函数:
#-----1.访问-----
#.get(key,default=None)返回key对应的值，不存在时返回default(默认为None)，不报错
d={"a":1}
d["a"]                  #1      d[key]     键存在返回值，不存在报KeyError
print(d.get("a"))       #1      键存在，返回对应值
print(d.get("x"))       #None   键不存在，省略default返回None
print(d.get("x",0))     #0      键不存在，返回指定的默认值0
#-----2.增/改-----
#.setdefault(key,default=None)键存在时返回对应值(不做调整)，键不存在插入key:default并返回default
d={"a":1}                       
d["a"]=1                        #d[key]=value       键存在则修改，不存在则新增
print(d.setdefault("a",100))    #1      键存在，返回原值，不修改
print(d.setdefault("b",200))    #200    键不存在，插入"b":200并返回200
print(d)
#.update(other)将other(字典或键值对序列)批量写入字典，重复键会被覆盖
d={"a":1}
d.update({"b":2,"c":3})
print(d)                #{"a":1,"b":2,"c":3}
d.update([("c",300),("d",4)])   #接受键值对序列
print(d)                #{"a":1,"b":2,"c":300,"d":4}
#-----3.删除-----
#.pop(key,default)删除key并返回其值，不存在key时，提供default时返回default，未提供时返回KeyError
d={"a":1,"b":2}
print(d.pop("a"))            #1         删除并返回值
print(d)                     #{"b":2}
print(d.pop("x","没找到"))   #没找到    键不存在，返回default
#print(d.pop("x"))           #返回KeyError
#.popitem()移除并返回最后插入的一个键值对(key,value);空字典调用报KeyError
#python3.7+按插入顺序移除"最新"的
d={"a":1,"b":2}
print(d.popitem())           #("b",2)   返回最后插入键值对
print(d)                     #("a":1)
#.clear()清空字典所有元素，无返回值(返回None)
d={"a":1,"b":2}
print(d.clear())             #None
print(d)                     #{}
d={"a":1,"b":2}
del d["a"]                   #删除键，不返回值，键不存在报KeyError
print(d)                     #{"b":2}
#-----4.查询-----
d={"a":1,"b":2}
print(len(d))                #2     len(d)键值对个数
print("a" in d)              #True  key in d        检查键是否存在
print("x" in d)              #False
#d.copy()返回浅拷贝(新字典，嵌套的可变对象共享引用，修改该内容时两者都受到影响)
d2=d.copy()
print(d2)                   #{"a":1,"b":2}
print(d is d2)              #False
print(d==d2)                #True
#-----5.合并-----
d1={"a":1};d2={"a":999,"b":2}
print(d1|d2)                #{"a":999,"b":2}   d1|d2      返回合并后新字典，重复键取d2的值
d1|=d2                      #d1|=d2 原地合并，修改d1
print(d1)                   #{"a":999,"b":2}
#-----6.遍历-----
d={"a":1,"b":2}
print(list(d.keys()))       #["a","b"]  d.keys()查看所有键视图,返回值为视图对象，该对象可迭代
print(list(d.values()))     #["1","2"]  d.values()查看所有值视图，返回值为视图对象
print(list(d.items()))      #[("a",1),("b",2)]  d.items()所有键，值的视图，返回值为视图对象
for k in d:
    print(k)                #a \n b 遍历键
for v in d.values():
    print(v)                #1 \n 2 遍历值
for k,v in d.items():
    print(k,v)              #a 1 \n b 2