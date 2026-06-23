#元组(Tuple)与列表类似，但不同点在于元组的元素不能修改，元组使用小括号()，元素间仍用逗号,隔开
#元组中的元素类型同样可以不相同，此外分割与索引方式与字符串和列表类似，不再赘述
my_tuple=("abcd",486,2.23,"runoob",70.2)
tiny_tuple=(123,"runoob")

print(my_tuple,len(my_tuple))
print(my_tuple[0])
print(my_tuple[1:3])
print(my_tuple[2:])
print(tiny_tuple*2)
print(my_tuple+tiny_tuple)

#元组的元素不可变，但可以包含可变的对象如list列表
test_list=[1,2,3]
test_tuple=(12,"abc",test_list)
print(test_tuple,len(test_tuple))
test_list[2]=4
test_list[0:-1]=["abc",42]
print(test_tuple)

#构造包含0个或1个元素的元组较为特殊，需要额外注意如下的语法规则
tup0=()     #空元组
tup1=(20,)  #只有一个元素的元组
not_a_tuple=(42)  #这是整数42，不是元组
print(type(tup0),type(tup1),type(not_a_tuple),len(tup0),len(tup1)) #因为整数不能放入len()中作为参数