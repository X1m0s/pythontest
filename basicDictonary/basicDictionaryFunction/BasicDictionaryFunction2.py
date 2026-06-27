#-----6.key in dict-----
#该操作符用于判断键是否存在于字典中，如果存在返回True，否则False，not in相反
test_dict={"Name":"Runoob","Age":7}
if "Age" in test_dict:
    print("键Age存在")
else:
    print("键Age不存在")
if "Sex" in test_dict:
    print("键Sex存在")
else:
    print("键Sex不存在")
if "Age" not in test_dict:
    print("键Age不存在")
else:
    print("键Age存在")
#-----7.items()/keys()/values()-----
#这三个函数用于返回视图对象，视图对象本身不是列表，不支持任何索引和修改，但可通过list()转换为列表
print(f"test_dict.items={test_dict.items()}")
print(f"test_dict.keys={test_dict.keys()}")
print(f"test_dict.values={test_dict.values()}")
print(f"test_dict.items={list(test_dict.items())}")
print(f"test_dict.keys={list(test_dict.keys())}")
print(f"test_dict.values={list(test_dict.values())}")
#-----8.update()-----
#该函数用于把另一个字典的键值对更新到字典中，update(dict)中dict为添加到指定字典中的字典
dict1={"Name":"Runoob","Age":7}
dict2={"Sex":"Female"}
dict1.update(dict2)
print("更新后的dict1=",dict1)
#-----9.pop()-----
#该函数用于删除字典key所对应的值，返回被删除的值，如果键不存在可返回一个默认值
#dict.pop(key,default)key为要移除的键，default为见不存在时返回的默认值，如不提供且键不存在，会引发异常
site={"Name":"菜鸟教程","alexa":10000,"url":"www.runoob.com"}
element=site.pop("name")
print("删除的元素为:",element)
print("字典为:",site)
element=site.pop("nickname","不存在的key")
print("删除的元素为:",element)
print("字典为:",site)
#-----10.popitem()-----
#该函数用于返回并删除字典中的最后插入键值，按照LIFO(后进先出)顺序规则
#在python3.7版本前，字典属于无序结构，所以该函数会随机返回并删除
site={"Name":"菜鸟教程","alexa":10000,"url":"www.runoob.com"}
result=site.popitem()                   #当前最后插入的是"url"
print("返回值=",result,"site=",site)
site["nickname"]="Runoob"               #现在"nickname"是最后插入的元素
print("site=",site)
result=site.popitem
print("返回值=",result,"site=",site)