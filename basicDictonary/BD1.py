#字典是另一种可变容器模型，可用于存储任意类型对象，每个键值对用冒号分隔，对之间用逗号分隔
#格式为d={key1:value1,key2:value2.....}
#字典中键必须唯一且必须可哈希，如数字/字符串/None/内部元素均可哈希的元组/不可变集合/bytes
#唯一的判断由哈希决定，1和1.0和True哈希相同，会被视为同一个键，当键值重复时，后键会覆盖前键
test_dict={1:"C++",2:"python",1.0:"C#",True:"C"}
print(test_dict)
#创建空字典时，使用大括号{}或构造函数dict()
empty_dict={}
print(empty_dict,f"Length={len(empty_dict)},type={type(empty_dict)}")

#如果想使用dict()函数构造字典，需要注意参数的格式
#1.无参
print(test_dict:=dict())
#2.键值对序列(要求可迭代，每个元素恰好两个子元素)
print(test_dict:=dict([("a",1),("b",2)]))               #列表套元组
print(test_dict:=dict((("a",1),("b",2))))               #元组套元组
print(test_dict:=dict([["a",1],["b",2]]))               #列表套列表
print(test_dict:=dict(zip(["a","b"],[1,2])))            #zip返回的元组迭代器
#zip(*iterables,strict)用于将多个可迭代对象"拉链"，返回元组迭代器，
#当strict=True时，如果可迭代对象不等长报错
print("zip()用法示例",list(zip("abc",[1,2,3],(4,5,6))))
#3.关键字参数(键必须是合法标识符)
print(test_dict:=dict(a=1,b=2,c=3))
#4.从已有映射拷贝
print(test_dict:=dict({"a":1,"b":2}))
#5.字典推导式(不是构造函数，但效果相同)
print({k: v for k,v in[("a",1),("b",2)]})

#访问字典内的值时，把相应的键放入方括号中即可
test_dict={"Name":"Runoob","URL":"www.runoob.com","code":"Python"}
print(f'test_dict["Name"]={test_dict["Name"]},test_dict["URL"]={test_dict["URL"]}')
#向字典添加新内容时直接添加新的键值对
test_dict["Name"]="RUNOOB"
test_dict["User"]="XMS"
print('test_dict["Name"]:',test_dict["Name"])
print('test_dict["User"]:',test_dict["User"])
#删除字典元素使用del删除对应键即可，也可以用于显式删除整个字典
del test_dict["User"]
print("删除User后的字典:",test_dict)
test_dict.clear()
print("使用clear()清空后的字典:",test_dict)
del test_dict                               #此时字典已完全删除，若再使用print打印报错

#此外常规数据类型中，字典在直接迭代时，只会迭代键，值会直接丢失
d={"a":1,"b":2}
for x in d:
    print(x)                #仅迭代出"a"和"b"
for x in d.items():
    print(x)                #迭代完整内容