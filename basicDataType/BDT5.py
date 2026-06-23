#python中的集合(set)为无序、可变的数据类型，用于存储唯一的元素，集合中元素不会重复，可以进行常见集合操作
#唯一指集合中每个值只能出现一次，重复值会被自动忽略
#集合使用哈希值+等值进行重复判断，当数值相等时视为相同，例如：
#{1，1.0}->{1}-int 1和float 1.0哈希相同\{1，True}->{1}-True和1哈希值相同
#{"a","A"}->{"a","A"}-字符串区分大小写，不同\{(1,2),(1,2)}->{(1,2)}-元组内容相同
#不可哈希的不能放入集合，如列表和字典
#集合使用大括号{}表示，元素之间使用逗号,分隔，也可以使用set()函数创建集合
#创建空集合必须使用set()，使用{}创建的是空字典
sites={"Google","Taobao","Runoob","Facebook","Zhihu","Baidu"}
print(sites)

if "Runoob" in sites:
    print("Runoob在集合中")
else:
    print("Runoob不在集合中")
#set可进行集合运算
a=set("abracadabra")
b=set("alacazam")

print(a)      #a中唯一字符

print(a-b)    #a和b的差集(在a中不在b中)
print(a|b)    #a和b的并集(在a或b中)
print(a&b)    #a和b的交集(同时在a和b中)
print(a^b)    #a和b的对称差集(在a或b中，但不同时存在)