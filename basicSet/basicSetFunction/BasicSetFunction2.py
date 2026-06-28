#-----6.集合运算函数们(下)-----
#symmetric_difference(set)用于返回两个集合的对称差，即两个集合中不重复的元素集合
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
z=x.symmetric_difference(y)
print(f"x.symmetric_difference(y)={z}")
#和直接使用^运算符的效果相近
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
print(f"x^y={x^y}")
#update版则为移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同元素插入当前集合
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
x.symmetric_difference_update(y)
print(f"x.symmetric_difference_update(y)={x}")
#union(set1,set2...)用于返回几个集合的并集，同样也会自动去重
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
z=x.union(y)
print(f"x.union(y)={z}")
#多集合示例
x={"a","b","c"}
y={"b","d","e"}
z={"a","f","g"}
result=x.union(y,z)
print(result)
#-----7.isdisjoint()-----
#该函数用于判断两个集合是否包含相同的元素，如果没有返回True，否则返回False
x={"apple","banana","cherry"}
y={"google","runoob","facebook"}
if (x.isdisjoint(y)):
    print("两个集合不包含相同元素")
else:
    print("两个集合包含相同元素")
y.add("apple")                          #加入一个相同元素
if (x.isdisjoint(y)):
    print("两个集合不包含相同元素")
else:
    print("两个集合包含相同元素")
#-----8.issubset()-----
#该函数用于判断集合的所有元素是否都包含在指定集合中，如果是返回True，否则返回False
x={"a","b","c"}
y={"f","e","d","c","b","a"}
if (x.issubset(y)):
    print("x所有元素包含在y中")
else:
    print("x的元素没有全包含在y中")
y={"f","e","d","b","c"}                 #修改一下，删除一个相同元素
if (x.issubset(y)):
    print("x所有元素包含在y中")
else:
    print("x的元素没有全包含在y中")
#-----9.issuperset()-----
#该函数用于判断指定集合的所有元素是否都包含在集合中，如果是返回True，否则返回False
x={"f","e","d","c","b","a"}
y={"a","b","c"}
if (x.issubset(y)):
    print("y所有元素包含在x中")
else:
    print("y的元素没有全包含在x中")
x={"f","e","d","b","c"}                 #修改一下，删除一个相同元素
if (x.issubset(y)):
    print("y所有元素包含在x中")
else:
    print("y的元素没有全包含在x中")
#issuperset()函数其实本质就是issubset()的反版
#也就是说issubset()中，大集合在参数列表中，小集合作为引用函数的对象，issuperset()则是小集合作为参数
