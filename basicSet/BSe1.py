#集合(set)是一个无序的不重复元素序列，可以使用set()或{}创造一个集合
#创建空集合时只能使用set()，因为{}是空字典,但需注意set()函数只接受一个可迭代参数
basket={"apple","orange","apple","pear","orange","banana"}
print(basket)       #演示集合的自动去重功能
print("orange" in basket,"crabgrass" in basket)         #快速判断元素是否再集合内
#集合运算演示
a=set("abracadabra")
b=set("alacazam")
print(f"a={a},b={b}")
print(f"a-b={a-b},a|b={a|b}")   #集合a包含同时b不包含   集合a或b中包含的所有
print(f"a&b={a&b},a^b={a^b}")   #集合a和b中都包含的     不同时包含于集合a和b
#集合同样支持集合推导式(Set comprehension)
a={x for x in "abracadabra" if x not in "abc"}
print(a)

#集合的基本操作
#-----1.添加元素-----
test_set=set(("Google","Runoob","Taobao"))
test_set.add("Facebook")
print(test_set)
#此外也可以使用另外一个函数update()
test_set=set(("Google","Runoob","Taobao"))
test_set.update({1,3})
print(test_set)
test_set.update([1,4],[5,6])
print(test_set)
#-----2.移除元素-----
test_set=set(("Google","Runoob","Taobao"))
test_set.remove("Taobao")
print(test_set)
#test_set.remove("Facebook")        #当尝试移除不存在元素时会报错
#此外也可以使用另外一个函数discard()
test_set=set(("Google","Runoob","Taobao"))
test_set.discard("Taobao")          #不存在时不会报错
print(test_set)
#也可以用pop()随机删除集合中元素
test_set=set(("Google","Runoob","Taobao"))
x=test_set.pop()
print(x)
#-----3.计算集合元素个数-----
test_set=set(("Google","Runoob","Taobao"))
print(f"len(test_set)={len(test_set)}")
#-----4.清空集合-----
test_set=set(("Google","Runoob","Taobao"))
test_set.clear()
print(test_set)
#-----5.判断元素是否在集合中存在-----
test_set=set(("Google","Runoob","Taobao"))
print("Runoob" in test_set,"Facebook" in test_set)